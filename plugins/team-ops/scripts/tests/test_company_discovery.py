"""Offline routing smoke tests using temporary company files, never live state."""
import importlib.util
import json
from pathlib import Path
import tempfile
import unittest

spec = importlib.util.spec_from_file_location(
    'company_check', Path(__file__).resolve().parents[1] / 'check-company.py')
company = importlib.util.module_from_spec(spec)
spec.loader.exec_module(company)


class DiscoveryTests(unittest.TestCase):
    def setUp(self):
        self.temp = tempfile.TemporaryDirectory()
        self.addCleanup(self.temp.cleanup)
        self.root = Path(self.temp.name).resolve()
        self.entry = self.root / 'ENTRY.md'
        self.entry.write_text('Temporary company entry\n')
        self.record = {
            'name': 'Example', 'server_url': 'https://example.invalid',
            'workspace_id': '00000000-0000-4000-8000-000000000001',
            'entry_path': str(self.entry),
        }
        self.registry = {'schema_version': 1, 'companies': {'example': self.record}}
        self.binding = self.root / 'binding.json'
        self.binding.write_text(json.dumps({
            'schema_version': 1, 'multica': {
                key: self.record[key] for key in ('server_url', 'workspace_id')},
            'capture': {'mode': 'explicit'},
        }))

    def test_single_company_without_memory(self):
        self.assertEqual(company.select_company(self.registry)[0], 'example')
        self.assertIsNone(company.check_binding(self.record))

    def test_explicit_selection_precedes_default(self):
        self.registry['companies']['other'] = dict(self.record, name='Other')
        self.registry['default_company'] = 'other'
        self.assertEqual(company.select_company(self.registry, 'Example')[0], 'example')
        with self.assertRaisesRegex(ValueError, 'no default fallback'):
            company.select_company(self.registry, 'missing')

    def test_bad_default_and_ambiguous_registry_fail(self):
        self.registry['default_company'] = 'missing'
        with self.assertRaisesRegex(ValueError, 'invalid declared default'):
            company.select_company(self.registry)
        del self.registry['default_company']
        self.registry['companies']['other'] = dict(self.record)
        with self.assertRaisesRegex(ValueError, 'explicitly'):
            company.select_company(self.registry)

    def test_binding_resolves_from_entry_and_preserves_bytes(self):
        before = self.binding.read_bytes()
        self.record['memory_binding_path'] = 'binding.json'
        self.assertEqual(company.check_binding(self.record, str(self.binding)), self.binding)
        self.assertEqual(self.binding.read_bytes(), before)

    def test_entry_only_binding_and_conflict(self):
        self.assertEqual(company.check_binding(self.record, 'binding.json'), self.binding)
        self.record['memory_binding_path'] = 'other.json'
        with self.assertRaisesRegex(ValueError, 'pointers conflict'):
            company.check_binding(self.record, 'binding.json')

    def test_wrong_workspace_and_unreadable_binding_fail(self):
        self.record['memory_binding_path'] = 'binding.json'
        self.record['workspace_id'] = '00000000-0000-4000-8000-000000000002'
        with self.assertRaisesRegex(ValueError, 'identity disagrees'):
            company.check_binding(self.record)
        self.binding.unlink()
        with self.assertRaises(OSError):
            company.check_binding(self.record)

    def test_invalid_server_fails(self):
        for server in ('https://', 'file:///tmp/example', 'https://user:secret@example.invalid'):
            with self.subTest(server=server):
                self.record['server_url'] = server
                with self.assertRaisesRegex(ValueError, 'server_url'):
                    company.select_company(self.registry)

    def test_unreadable_entry_and_short_uuid_fail(self):
        self.record['entry_path'] = str(self.root / 'missing.md')
        with self.assertRaisesRegex(ValueError, 'entry_path'):
            company.select_company(self.registry)
        self.record['workspace_id'] = 'short-id'
        with self.assertRaises(ValueError):
            company.select_company(self.registry)


if __name__ == '__main__':
    unittest.main()
