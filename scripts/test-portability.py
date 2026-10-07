"""Offline native discovery checks. Runtime configurations stay in temporary directories."""
import json
import os
import shutil
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXPECTED = sorted(path.parent.name for path in (ROOT / 'skills').glob('*/SKILL.md'))


def run(args, **kwargs):
    result = subprocess.run(args, text=True, capture_output=True, timeout=90, **kwargs)
    if result.returncode:
        raise AssertionError(f'{args[0]} exited {result.returncode}\n{result.stdout}\n{result.stderr}')
    return result.stdout


with tempfile.TemporaryDirectory(prefix='multica-portability-') as scratch:
    temp = Path(scratch)
    package = temp / 'renamed-checkout'
    shutil.copytree(ROOT, package, ignore=shutil.ignore_patterns('.git', '__pycache__'))
    run(['python3', str(package / 'scripts/check.py')])
    home = temp / 'inventory-home'
    settings = home / '.pi/agent/settings.json'
    settings.parent.mkdir(parents=True)
    settings.write_text(json.dumps({'packages': [str(package)]}))
    hermes_config = home / '.hermes/config.yaml'
    hermes_config.parent.mkdir()
    hermes_config.write_text('skills:\n  external_dirs:\n    - ' + json.dumps(str(package / 'skills')) + '\n')
    output = run(['bash', str(package / 'operations/scripts/find-installs.sh')],
                 env=dict(os.environ, HOME=str(home)))
    assert 'package, Pi' in output and str(package) in output, output
    assert 'mount, hermes' in output and str(package / 'skills') in output, output
    assert 'installs of multica-team' in output, output
    print('PASS: relocated full package and Pi/Hermes inventory under an unrelated checkout name')

    if shutil.which('claude'):
        run(['claude', 'plugin', 'validate', str(package)])
        print('PASS: Claude native marketplace validation')
    else:
        print('SKIP: Claude is not installed')

    if shutil.which('codex'):
        (temp / 'codex').mkdir()
        env = dict(os.environ, CODEX_HOME=str(temp / 'codex'))
        run(['codex', 'plugin', 'marketplace', 'add', str(package), '--json'], env=env)
        installed = json.loads(run(['codex', 'plugin', 'add', 'multica-team@multica-team', '--json'], env=env))
        path = Path(installed['installedPath'])
        assert installed['version'] == json.loads((package / 'plugin.json').read_text())['version']
        assert sorted(p.parent.name for p in (path / 'skills').glob('*/SKILL.md')) == EXPECTED
        run(['python3', str(path / 'scripts/check.py')])
        native = temp / 'codex-native-only'
        shutil.copytree(package, native)
        shutil.rmtree(native / '.claude-plugin')
        (native / 'plugin.json').unlink()
        (temp / 'codex-native-home').mkdir()
        env = dict(os.environ, CODEX_HOME=str(temp / 'codex-native-home'))
        run(['codex', 'plugin', 'marketplace', 'add', str(native), '--json'], env=env)
        result = json.loads(run(['codex', 'plugin', 'add', 'multica-team@multica-team', '--json'], env=env))
        native_path = Path(result['installedPath'])
        assert result['version'] == installed['version']
        assert sorted(p.parent.name for p in (native_path / 'skills').glob('*/SKILL.md')) == EXPECTED
        assert (native_path / 'SPEC.md').read_text() == (package / 'SPEC.md').read_text()
        print('PASS: Codex native-only metadata installs without Claude or portable manifest fallback')
    else:
        print('SKIP: Codex is not installed')

    if shutil.which('pi'):
        agent_dir = temp / 'pi'
        env = dict(os.environ, PI_CODING_AGENT_DIR=str(agent_dir), PI_OFFLINE='1', PI_TELEMETRY='0')
        run(['pi', 'install', str(package)], env=env)
        source = json.loads((agent_dir / 'settings.json').read_text())['packages'][0]
        assert (agent_dir / source).resolve() == package.resolve()
        cli = Path(shutil.which('pi')).resolve()
        module = cli.parents[1] / 'core/skills.js'
        assert module.is_file(), f'Cannot locate Pi native skill loader beside {cli}'
        script = '''const {loadSkillsFromDir} = await import(process.argv[1]);
const result = loadSkillsFromDir({dir: process.argv[2], source: "portability-test"});
console.log(JSON.stringify({names: result.skills.map(s => s.name).sort(), diagnostics: result.diagnostics}));'''
        loaded = json.loads(run(['node', '--input-type=module', '-e', script, module.as_uri(), str(package / 'skills')], env=env))
        assert loaded['names'] == EXPECTED, loaded
        assert not loaded['diagnostics'], loaded
        print('PASS: Pi native package install and skill loader discover all 23 skills')
    else:
        print('SKIP: Pi is not installed')

    if shutil.which('hermes'):
        import re
        runtime = json.loads(run(['hermes', '--print-runtime-command']))
        match = re.search(r"sys.path.insert\(0, ('[^']*'|\"[^\"]*\")\)", runtime[-1])
        assert match, 'Cannot locate Hermes source in native runtime command'
        hermes_root = Path(match[1][1:-1])
        python = Path(runtime[0])
        code = '''import json,sys
from pathlib import Path
import os
probe_home = os.environ.pop("HERMES_PROBE_HOME")
import hermes_bootstrap
os.environ["HERMES_HOME"] = probe_home
from hermes_cli.agent_plugins import load_agent_plugin
package = load_agent_plugin(Path(sys.argv[1]), Path(sys.argv[2]))
assert not package.diagnostics, package.diagnostics
assert not package.mcp_servers
print(json.dumps(sorted(skill.name for skill in package.skills)))'''
        hermes_home = temp / 'hermes'
        hermes_home.mkdir()
        (hermes_home / 'config.yaml').write_text('skills:\n  external_dirs:\n    - ' + json.dumps(str(package / 'skills')) + '\n')
        env = dict(os.environ, HERMES_PROBE_HOME=str(hermes_home), PYTHONPATH=str(hermes_root), HERMES_DISABLE_LAZY_INSTALLS='1')
        loaded = json.loads(run([str(python), '-c', code, str(package), str(temp / 'hermes-data')], env=env, cwd=temp))
        assert loaded == EXPECTED, loaded
        code = '''import json,sys
from pathlib import Path
import os
probe_home = os.environ.pop("HERMES_PROBE_HOME")
import hermes_bootstrap
os.environ["HERMES_HOME"] = probe_home
from tools.skills_tool import _skill_catalog, skill_view
catalog = _skill_catalog()
names = sorted(item['name'] for item in catalog)
view = json.loads(skill_view("mops", preprocess=False))
assert not view.get("error"), view
assert "Team Advisor" in json.dumps(view), view
assert "# Memory instance format" in (Path(sys.argv[1]) / "SPEC.md").read_text()
print(json.dumps(names))'''
        loaded = json.loads(run([str(python), '-c', code, str(package)], env=env, cwd=temp))
        assert loaded == EXPECTED, loaded
        print('PASS: Hermes portable manifest, external directory discovery, and skill_view loading')
    else:
        print('SKIP: Hermes is not installed')
