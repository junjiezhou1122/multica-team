"""Validate the plugin package and example instance without network access."""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []
manifest = json.loads((root / '.claude-plugin/plugin.json').read_text())
marketplace = json.loads((root / '.claude-plugin/marketplace.json').read_text())
entries = {entry['name']: entry for entry in marketplace['plugins']}
if set(entries) != {'multica-team', 'team-ops'} or manifest['name'] != 'multica-team':
    errors.append('Expected memory and team-ops marketplace entries')
for name, relative in (('multica-team', '.'), ('team-ops', 'plugins/team-ops')):
    component = root / relative
    data = json.loads((component / '.claude-plugin/plugin.json').read_text())
    entry = entries.get(name, {})
    if data['name'] != name or entry.get('version') != data['version'] or entry.get('source') != ('./' if relative == '.' else './' + relative):
        errors.append(f'{name}: marketplace identity, version or source mismatch')
ops = root / 'plugins/team-ops'
if not (ops / 'LICENSE').is_file() or not (ops / 'LOCAL_COMPANIES.md').is_file():
    errors.append('Missing team-ops license or company discovery reference')
for path in (ops / 'skills').glob('*/SKILL.md'):
    text = path.read_text()
    if not text.startswith('---\n') or not re.search(r'^name: .+$', text, re.M) or not re.search(r'^description: .+$', text, re.M):
        errors.append(f'{path.relative_to(root)}: invalid skill frontmatter')
if len(list((ops / 'skills').glob('*/SKILL.md'))) != 19:
    errors.append('Expected 19 team-ops skills')
if 'LOCAL_COMPANIES.md' not in (ops / 'skills/mops/SKILL.md').read_text():
    errors.append('Missing team-ops company discovery pointer')
# Check component-owned integration references as well as skill bodies. Each
# must resolve within its own installed plugin root.
ops_references = list((ops / 'skills').glob('*/SKILL.md')) + [
    ops / name for name in ('LOCAL_COMPANIES.md', 'COMPANY_KNOWLEDGE.md', 'README.md')]
for path in ops_references:
    for target in re.findall(r'\[[^\]\n]+\]\(([^)]+)\)', path.read_text()):
        if target.startswith(('https://', 'http://', '#')):
            continue
        resolved = (path.parent / target.split('#')[0]).resolve()
        if not resolved.is_relative_to(ops) or not resolved.exists():
            errors.append(f'{path.relative_to(root)}: broken component reference {target}')

for name in ('setup', 'team-memory', 'dreaming', 'feedback'):
    path = root / 'skills' / name / 'SKILL.md'
    if not path.is_file():
        errors.append(f'Missing skill body: skills/{name}/SKILL.md')
        continue
    text = path.read_text()
    match = re.match(r'\A---\n(.*?)\n---\n', text, re.S)
    fields = dict(re.findall(r'^(name|description): (.+)$', match[1], re.M)) if match else {}
    if fields.get('name') != path.parent.name or not fields.get('description'):
        errors.append(f'{path.relative_to(root)}: invalid skill frontmatter')
    if 'multica-integration.md#discover-a-company-binding' not in text:
        errors.append(f'{path.relative_to(root)}: missing company binding discovery pointer')
if {p.name for p in (root / 'skills').iterdir() if p.is_dir()} != {'setup', 'team-memory', 'dreaming', 'feedback'}:
    errors.append('Expected four skills')

for path in root.rglob('*.md'):
    if '.git' in path.parts or path.is_relative_to(root / 'plugins'):
        continue
    for target in re.findall(r'(?<!!)\[[^\]\n]+\]\(([^)]+)\)', path.read_text()):
        if target.startswith(('https://', 'http://', '#', 'mailto:')):
            continue
        resolved = (path.parent / target.split('#')[0]).resolve()
        if not resolved.is_relative_to(root) or not resolved.exists():
            errors.append(f'{path.relative_to(root)}: missing or external link {target}')

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

# Memory skill references must survive installation apart from Team Ops.
for path in (root / 'skills').glob('*/SKILL.md'):
    for target in re.findall(r'\[[^\]\n]+\]\(([^)]+)\)', path.read_text()):
        if target.startswith(('https://', 'http://', '#')):
            continue
        resolved = (path.parent / target.split('#')[0]).resolve()
        if resolved.is_relative_to(ops):
            errors.append(f'{path.relative_to(root)}: cross-plugin filesystem pointer {target}')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print('PASS: two marketplace plugins, 4 memory skills, 19 operations skills, references, memory links, and example binding')
