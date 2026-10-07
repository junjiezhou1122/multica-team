"""Validate the plugin package and example instance without network access."""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []
manifest = json.loads((root / '.claude-plugin/plugin.json').read_text())
marketplace = json.loads((root / '.claude-plugin/marketplace.json').read_text())
entries = marketplace['plugins']
if len(entries) != 1 or entries[0].get('name') != 'multica-team' or entries[0].get('source') != './':
    errors.append('Expected one multica-team marketplace entry at the root')
if manifest.get('name') != 'multica-team' or manifest.get('version') != '0.2.0' or any(entry.get('version') != manifest.get('version') for entry in entries):
    errors.append('Root plugin and marketplace identity/version mismatch')
if manifest.get('license') != 'MIT AND Apache-2.0':
    errors.append('Manifest must describe both component licenses')
for path in root.rglob('plugin.json'):
    if '.git' not in path.parts and path != root / '.claude-plugin/plugin.json':
        errors.append(f'{path.relative_to(root)}: nested plugin manifest')
for path in root.rglob('marketplace.json'):
    if '.git' not in path.parts and path != root / '.claude-plugin/marketplace.json':
        errors.append(f'{path.relative_to(root)}: nested marketplace')
ops = root / 'operations'
for name in ('LICENSE', 'LOCAL_COMPANIES.md', 'COMPANY_KNOWLEDGE.md'):
    if not (ops / name).is_file():
        errors.append(f'Missing operations resource: {name}')
memory_skills = {'setup', 'team-memory', 'dreaming', 'feedback'}
operation_skills = {'audit', 'bug', 'cli', 'consult', 'feature', 'fire', 'hire', 'import', 'init', 'join', 'mops', 'next', 'quick', 'recover', 'report', 'ship', 'skill', 'status', 'upgrade'}
expected_skills = memory_skills | operation_skills
if {p.name for p in (root / 'skills').iterdir() if p.is_dir()} != expected_skills:
    errors.append('Expected exactly 23 root skill directories')
for name in sorted(expected_skills):
    path = root / 'skills' / name / 'SKILL.md'
    if not path.is_file():
        errors.append(f'Missing skill body: skills/{name}/SKILL.md')
        continue
    text = path.read_text()
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    fields = dict(re.findall(r'^(name|description): (.+)$', match[1], re.M)) if match else {}
    if fields.get('name') != name or not fields.get('description'):
        errors.append(f'{path.relative_to(root)}: invalid skill frontmatter')
    if '/team-ops:' in text:
        errors.append(f'{path.relative_to(root)}: obsolete command namespace')
    if name in memory_skills and 'multica-integration.md#discover-a-company-binding' not in text:
        errors.append(f'{path.relative_to(root)}: missing company binding discovery pointer')
    if name in operation_skills - {'mops'} and '(../mops/SKILL.md)' not in text:
        errors.append(f'{path.relative_to(root)}: missing Mops procedure link')
    if name == 'mops' and ('../../operations/LOCAL_COMPANIES.md' not in text or 'version: 0.2.0' not in text):
        errors.append('Mops must point to relocated discovery and match package version')

# Validate every skill plus package-owned integration documents. Inherited
# operations reference material retains historical examples and external schemes.
references = list((root / 'skills').glob('*/SKILL.md')) + [
    ops / name for name in ('LOCAL_COMPANIES.md', 'COMPANY_KNOWLEDGE.md', 'README.md', 'INSTALL.md', 'MAINTENANCE.md')]
references += [p for p in root.rglob('*.md') if '.git' not in p.parts and not p.is_relative_to(ops) and not p.is_relative_to(root / 'skills')]
for path in references:
    for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)', path.read_text()):
        if re.match(r'^[a-zA-Z][a-zA-Z0-9+.-]*:', target) or target.startswith('#'):
            continue
        resolved = (path.parent / target.split('#')[0]).resolve()
        if not resolved.is_relative_to(root) or not resolved.exists():
            errors.append(f'{path.relative_to(root)}: missing or external link {target}')

knowledge = (ops / 'COMPANY_KNOWLEDGE.md').read_text()
if '../skills/team-memory/SKILL.md' not in knowledge or '../SPEC.md' not in knowledge:
    errors.append('Company knowledge must directly reference canonical memory in this package')
if '~/.config/multica-ops/companies.json' not in (ops / 'LOCAL_COMPANIES.md').read_text():
    errors.append('Company discovery must preserve the compatible registry path')

hooks = json.loads((root / 'hooks/hooks.json').read_text())['hooks']
if set(hooks) != {'SessionStart', 'PreToolUse', 'PostToolUse'}:
    errors.append('Unexpected hook event expansion')
commands = [hook['command'] for groups in hooks.values() for group in groups for hook in group['hooks']]
expected_hooks = {'migration-state.sh', 'outward-gate.sh', 'rule-home.sh', 'dispatch-nudge.sh'}
if len(commands) != 4 or {command.rsplit('/', 1)[-1] for command in commands} != expected_hooks:
    errors.append('Expected the four inherited hook commands')
for command in commands:
    relative = command.replace('"${CLAUDE_PLUGIN_ROOT}"/', '')
    if not relative.startswith('hooks/') or not (root / relative).is_file():
        errors.append(f'Unresolved root hook command: {command}')
# Default hooks/hooks.json discovery avoids registering these hooks twice.
if 'hooks' in manifest:
    errors.append('Use default root hook discovery, without duplicate manifest registration')

memory = root / 'templates/memory'
for path in memory.rglob('*.md'):
    for target in re.findall(r'\[\[([^\]]+)\]\]', path.read_text()):
        destination = memory / target
        if not destination.suffix:
            destination = destination.with_suffix('.md')
        if not destination.resolve().is_relative_to(memory) or not destination.is_file():
            errors.append(f'{path.relative_to(root)}: invalid memory link {target}')

binding = json.loads((root / 'templates/binding.example.json').read_text())
if binding['schema_version'] != 1 or not Path(binding['memory']['local_path']).is_absolute():
    errors.append('Invalid example binding version or local path')
for mapping in ('members', 'projects'):
    keys = list(binding[mapping].values())
    if len(keys) != len(set(keys)) or any(not re.fullmatch(r'[a-z0-9]+(?:-[a-z0-9]+)*', key) for key in keys):
        errors.append(f'Invalid or duplicate {mapping} directory keys')
if binding['maintainer_agent_id'] not in binding['members']:
    errors.append('Example maintainer must be a registered member')
if any(agent not in binding['members'] for agent in binding['dreaming'].get('agent_ids', [])):
    errors.append('Example dreamers must be registered members')
if binding['feedback']['mode'] != 'preview' or binding['dreaming']['trigger'] != 'manual':
    errors.append('Example must retain preview feedback and manual dreaming')
if binding['feedback'].get('issue_grant') is not None:
    errors.append('Example issue grant must remain null')
if binding['memory']['push_authorized'] or binding['feedback']['pr_authorized']:
    errors.append('Example must not grant remote publication')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print('PASS: one plugin, 23 skills, installed references, four root hooks, licenses, memory links, and example binding')
