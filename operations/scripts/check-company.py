#!/usr/bin/env python3
"""Read-only local company selection and optional binding identity check."""
import argparse
import json
from pathlib import Path
from uuid import UUID
from urllib.parse import urlsplit


def workspace_id(value):
    if not isinstance(value, str) or str(UUID(value)) != value.lower():
        raise ValueError('workspace_id must be a full UUID')
    return value.lower()


def identity(record):
    server = record['server_url']
    if not isinstance(server, str):
        raise ValueError('server_url must be an HTTP(S) URL')
    url = urlsplit(server)
    if url.scheme not in ('https', 'http') or not url.hostname or url.username or url.password:
        raise ValueError('server_url must be an HTTP(S) URL with a host and no credentials')
    return server.rstrip('/'), workspace_id(record['workspace_id'])


def select_company(registry, target=None):
    if registry.get('schema_version') != 1 or not isinstance(registry.get('companies'), dict):
        raise ValueError('invalid company registry schema')
    companies = registry['companies']
    if target is not None:
        matches = [key for key, value in companies.items()
                   if key == target or value.get('name') == target]
        if target in companies:
            matches = [target]
        if len(matches) != 1:
            raise ValueError('explicit company is unknown or ambiguous; no default fallback')
        key = matches[0]
    elif 'default_company' in registry:
        key = registry['default_company']
        if not isinstance(key, str) or key not in companies:
            raise ValueError('invalid declared default company')
    elif len(companies) == 1:
        key = next(iter(companies))
    else:
        raise ValueError('select a company explicitly')
    record = companies[key]
    identity(record)
    entry = Path(record['entry_path'])
    if not entry.is_absolute() or not entry.is_file():
        raise ValueError('selected entry_path must be an existing absolute file')
    return key, record


def check_binding(record, entry_binding=None):
    """entry_binding is a pointer read from the selected entry by the caller."""
    base = Path(record['entry_path']).parent
    pointers = [value for value in (record.get('memory_binding_path'), entry_binding)
                if value is not None]
    resolved = []
    for value in pointers:
        if not isinstance(value, str) or not value.strip():
            raise ValueError('memory_binding_path must be a nonempty path')
        path = Path(value)
        resolved.append((path if path.is_absolute() else base / path).resolve())
    if not resolved:
        return None
    if len(set(resolved)) != 1:
        raise ValueError('registration and entry memory binding pointers conflict')
    binding = json.loads(resolved[0].read_text())
    if binding.get('schema_version') != 1 or identity(binding['multica']) != identity(record):
        raise ValueError('memory binding identity disagrees with selected company')
    return resolved[0]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--registry', type=Path,
                        default=Path.home() / '.config/multica-ops/companies.json')
    parser.add_argument('--company', help='explicit registry key or company name')
    parser.add_argument('--entry-binding', help='optional pointer read from the selected entry')
    args = parser.parse_args()
    try:
        key, record = select_company(json.loads(args.registry.read_text()), args.company)
        binding = check_binding(record, args.entry_binding)
    except (OSError, ValueError, KeyError, TypeError, AttributeError) as exc:
        parser.exit(1, f'FAIL: {exc}\n')
    print(f'PASS: selected {key}; entry readable; memory binding '
          + ('identity agrees' if binding else 'not configured'))
    print('Entry identity, live platform state, memory links, grants and runtime access require separate verification.')


if __name__ == '__main__':
    main()
