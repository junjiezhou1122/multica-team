# Team Ops

Company operations workflows maintained by Multica Team. This component derives from multica-ops 0.4.19 under Apache-2.0, with original attribution retained. It is independently maintained and is not endorsed by the original project.

Install through the parent multica-team marketplace:

```sh
claude plugin install team-ops@multica-team
```

Use `/team-ops:mops` to operate an existing company or discuss a new one. The advisor resolves registered local companies using [LOCAL_COMPANIES.md](LOCAL_COMPANIES.md) only when invoked. Explicit targets take precedence over defaults. Registration does not grant action permissions.

The component includes 19 skills and the original operations hooks. Installing it does not create company members. Memory workflows remain in the separate multica-team plugin. An optional local `memory_binding_path` connects the selected company to that plugin through installed skill invocation. Follow [company knowledge](COMPANY_KNOWLEDGE.md) for task lookup, decision drafts and grill-with-doc, owner observation investigations, and retrospective candidate proposals. Memory semantics remain canonical in Multica Team; observations and pending experiments stay in company operations. Company records, credentials and registrations remain outside the package.

See [MAINTENANCE.md](MAINTENANCE.md) for provenance and update policy, [COMMANDS.md](COMMANDS.md) for commands, and [LICENSE](LICENSE) for terms. Optional upstream evaluation fixtures and reserved artwork are not distributed here. Historical test claims in inherited documents describe the original version, not validation of this derivative.
