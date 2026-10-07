---
name: upgrade
description: Move to a newer version — re-screened, backed up, migrated, and reversible.
---

Load and follow the [Mops skill](../mops/SKILL.md), executing
its `/multica-team:upgrade` flow. Upgrade the project's installed skills safely: dry-run impact report → commit current to _ops/skill-backups/ (git = history, SHA in UPGRADES.md) → apply → reconcile dependents → verify/rollback. Use the invocation arguments and accompanying user message as the request.
