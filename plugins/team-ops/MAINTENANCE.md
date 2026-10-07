# Multica Team maintenance

This component is maintained in this repository independently of the original multica-ops project. It uses the team-ops plugin identity and /team-ops command namespace while retaining the company operations workflows. The original project's reserved branding and avatars are not used for this derivative. No automatic upstream synchronization is configured.

The baseline is multica-ops 0.4.19, original commit 1cf9184c6165703e9d9b9b3c2a1393c141958730, by Jamil Lazarev. Original source: https://github.com/jamillazarev/multica-ops. Retain LICENSE, attribution and existing notices. This component is Apache-2.0; the root memory plugin is MIT. Initial team changes add on-demand company discovery through LOCAL_COMPANIES.md and the Mops skill entry.

Install from the parent repository marketplace:

```sh
claude plugin install team-ops@multica-team
```

If an earlier multica-ops marketplace installation exists, uninstall that plugin with --keep-data before installing this one. Preserve company files and registry. The registry at ~/.config/multica-ops/companies.json remains machine-local and is read only after Mops invocation. Do not publish real registrations, company bindings, memory, credentials or local overrides here.

Future changes belong in this component, with documented evidence and validation. Increment .claude-plugin/plugin.json and the parent marketplace entry together. Validate both parent marketplace and component. Reinstall/update the plugin and reload plugins after a change. Source control review and actual worker behavior are separate checks.
