# Version 0.1.0 design decisions

These decisions describe the initial plugin, not a user's operational grants.

| Decision | Chosen approach | Reason | Revisit when |
|---|---|---|---|
| Scope | Multica teams, memory first | Keep a clear integration target while supporting arbitrary roles and projects | Another platform needs a supported adapter |
| Format | Agent Memory Repo with optional status metadata | Keep ordinary Git and Markdown usable | A demonstrated format limitation appears |
| Instances | One separate repository per workspace | Keep ownership and routing explicit | Shared knowledge across companies needs attributed export |
| Members | Own folders and isolated branches | Let members learn without simultaneous checkout writes | Integration overhead warrants automation |
| Shared knowledge | Maintainer accepts candidates | Prevent one member's guess becoming team authority | Trials show safe decentralized writes |
| Dreaming | Manual invocation, justified local edit batches | Learn the workflow before scheduling consumption | Owner opts into a tested trigger |
| Operations | Eight documented primitives | Make edits attributable and reviewable | Repeated tasks need another distinct operation |
| Feedback | Preview by default, scoped auto-issue opt-in | Support public and private instances | Evidence demonstrates a better publication workflow |
| Authority | Guides and live platform state remain canonical | Knowledge cannot silently change rules | Owner deliberately migrates a source of truth |

The first version has offline structural checks. Agent behavior and Multica attachment have not been evaluated. Such trials are separate authorized work, and outcomes should drive subsequent changes rather than assuming documentation guarantees compliance.
