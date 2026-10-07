# Install company operations

Company operations and memory ship as one `multica-team` plugin. In Claude Code:

```sh
claude plugin marketplace add junjiezhou1122/multica-team
claude plugin install multica-team@multica-team
```

Use `/multica-team:mops` for the company front door and `/multica-team:setup` for explicitly requested memory setup. Claude Code exposes all 23 commands under `/multica-team:*`. Other clients use the invocation names in the runtime guide. [Commands](COMMANDS.md) lists operations flows. Install Multica itself using its official instructions, then inspect current `multica --help` before live calls.

For an existing separate `team-ops` installation, preserve its company files, local registry, and bindings. Remove that plugin with `--keep-data` when migrating the installation, then update the single `multica-team` plugin and reload plugins. The compatible registry path remains `~/.config/multica-ops/companies.json`. Update company command pointers to `/multica-team:*`; inherited hooks still recognize `Operated by team-ops` declarations.

Codex uses `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json` for the same plugin catalog, Pi uses the root `package.json`, and Hermes can load the root portable `plugin.json` or an external skills directory. Follow the [runtime guide](../docs/runtimes.md) for installation and the current validation limits. Keep the [root skills](../skills) and their supporting `operations/`, `docs/`, templates, and specification together. A body-only import breaks references. Imported Multica worker skills require explicit attachment and readback as described in [Multica integration](../docs/multica-integration.md#attach-to-workers). Console installation does not install worker skills or grant model runs.

Installation and worker behavior must be verified separately. This package's offline validation does not establish that imported skills were executed by a model.
