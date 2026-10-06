"""Validate the plugin package and example instance without network access."""
import json
import re
import sys
from pathlib import Path

root = Path(__file__).resolve().parents[1]
errors = []
manifest = json.loads((root / '.claude-plugin/plugin.json').read_text())
marketplace = json.loads((root / '.claude-plugin/marketplace.json').read_text())
if manifest['name'] != 'multica-team' or marketplace['plugins'][0]['name'] != manifest['name']:
    errors.append('Plugin and marketplace names disagree')
if marketplace['plugins'][0]['version'] != manifest['version']:
    errors.append('Plugin and marketplace versions disagree')

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
if {p.name for p in (root / 'skills').iterdir() if p.is_dir()} != {'setup', 'team-memory', 'dreaming', 'feedback'}:
    errors.append('Expected four skills')

for path in root.rglob('*.md'):
    if '.git' in path.parts:
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
if binding['feedback']['mode'] != 'preview' or binding['dreaming']['trigger'] != 'manual':
    errors.append('Example must retain preview feedback and manual dreaming')
if binding['memory']['push_authorized'] or binding['feedback']['pr_authorized']:
    errors.append('Example must not grant remote publication')

if errors:
    print('\n'.join(errors), file=sys.stderr)
    raise SystemExit(1)
print('PASS: plugin manifests, four skills, documentation links, memory links, and example binding')
