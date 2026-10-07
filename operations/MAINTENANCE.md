# Multica Team maintenance

The operations workflows are maintained as part of the single `multica-team` plugin, using `/multica-team:*`. Operations resources live here, the 19 operations skills live in root `skills/`, and inherited hooks live in root `hooks/`. No automatic upstream synchronization is configured. Reserved upstream branding and avatars are excluded.

The baseline is multica-ops 0.4.19, original commit 1cf9184c6165703e9d9b9b3c2a1393c141958730, by Jamil Lazarev. Original source: https://github.com/jamillazarev/multica-ops. Retain [LICENSE](LICENSE), attribution, and existing notices. Operations resources, the 19 operations skills, and inherited hooks remain Apache-2.0; the four memory skills and root workflow remain MIT. Packaging does not relicense either component.

Install through the [single plugin route](INSTALL.md). Preserve existing company files and the machine-local registry at `~/.config/multica-ops/companies.json`. Registrations, company bindings, memory, credentials, and local overrides stay outside this repository.

Increment the root `.claude-plugin/plugin.json` and its single marketplace entry together. Run `python3 scripts/check.py` and `python3 -m unittest discover -s operations/scripts/tests -p test_company_discovery.py` from the repository root, then native `claude plugin validate .` and `claude plugin validate .claude-plugin/marketplace.json`. Hook regression suites are under `operations/scripts/` and use root hooks. Inherited upstream preflight/coverage tools refer to omitted evaluation fixtures and historical layouts; they are not package acceptance checks. Report structural validation, installation, and actual worker behavior separately.
