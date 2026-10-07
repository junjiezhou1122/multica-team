# Memory instance format

This specification is for agents and maintainers of Multica Team memory instances. It retains the Agent Memory Repo format and adds workspace routing and collaboration conventions.

## Package and procedure routing

Version 0.3.0 ships 23 shared skills for Claude Code, Codex, Pi, and Hermes. Follow [runtime installation and invocation](docs/runtimes.md); `/multica-team:*` examples use Claude Code syntax. Company operations references live in `operations/`; canonical memory semantics remain in this specification and the four memory skills. Follow [company binding discovery](docs/multica-integration.md#discover-a-company-binding) before memory access. The machine-local registry path remains `~/.config/multica-ops/companies.json`; packaging grants no new authority.

## Storage and identity

An instance is a separate Git repository in a workspace's persistent directory, outside contribution code and run checkouts. One instance belongs to one `(Multica server URL, workspace UUID)` pair. A local binding outside that repository maps project and agent UUIDs to stable directory keys. Names are display labels, not authority. Resolve the actual workspace before reading or writing; ambiguous routing stops writes.

Different instances have separate ownership and history. Directories classify knowledge; they do not restrict access. Public instances are readable by everyone. A repository credential is not a project-level access boundary.

## Layout

```text
memory/
  MEMORY.md
  team/
    MEMORY.md
  projects/
    <project-key>/
      MEMORY.md
  members/
    <member-key>/
      MEMORY.md
  candidates/
    <candidate-key>.md
  dreams/
    <report-key>.md
  archive/
```

Only the root `MEMORY.md` is required by the upstream spec. Other indexes and directories are our conventions. Create topic files as knowledge accumulates; avoid empty catalogues. General workspace knowledge goes under `team/`. Project-specific knowledge goes under `projects/`. Member-specific working experience goes under `members/`. Store each fact once and link to it.

## Indexes and entries

Keep each index short. Put knowledge needed for every relevant task above `## Index`, and topic links below it. A knowledge entry is one bullet on one line:

```markdown
- A reproducible observation with its applicability [source: https://example.org/evidence; added: 2026-10-06; status: verified]
```

Metadata follows `[key: value; key: value]`. `source` and `added` are required for new knowledge in this profile. Dates use YYYY-MM-DD. Optional `status` values are `verified`, `unverified`, `disputed`, and `retired`. Verified means the cited evidence supports the stated claim; it does not imply universal validity. Record limitations in the entry. Other metadata keys remain allowed. Local source paths are suitable only for local/private instances; public entries use public evidence or a publishable explanation that the owner approved.

Use `[[path]]` relative to the memory repository root. Omit `.md` for Markdown files and retain extensions otherwise. A member index still links as `[[members/<member-key>/topic]]`. Links cannot escape the repository or point through external symlinks.

## What to remember

Keep reusable lessons, decisions and their reasons, terminology, and explicitly approved preferences. Keep task progress, current assignments, permissions, credentials, and local configuration in their authoritative stores. Link to a guide instead of copying rules. Memory cannot authorize actions or change acceptance criteria.

## Capabilities

Memory access follows instance capabilities, not job titles or a prescribed team structure. Every registered member can read applicable knowledge, maintain its own folder, and propose shared knowledge. `maintainer_agent_id` selects the member responsible for shared acceptance and serial integration; that member may have any job. `dreaming.agent_ids` selects members allowed to perform shared-memory dreams. An authorized dreamer can consolidate existing shared knowledge, but promoting member knowledge to shared scope still requires maintainer acceptance. Other members can dream over their own folders and propose shared changes. The maintainer can perform shared-memory dreams; an empty dreamer list grants no additional members this capability. These are procedural permissions, not filesystem access controls.

## Candidates and shared writes

Members maintain their own folders on isolated task branches/checkouts. Shared team/project knowledge is accepted by the maintainer identified in the binding. A candidate records the proposed one-line entry, scope, evidence, uncertainty, and origin. Acceptance checks existing knowledge, source coverage, public suitability, and the proper destination. Preserve attribution when combining entries.

The maintainer serializes integration of candidate branches. A dirty checkout, changed HEAD, or conflicting concurrent edit stops the write. Do not reset another writer's work. Each completed edit batch gets a local commit of only intended files. Pull uses fast-forward only; unresolved merges stop and retain the branch. Push requires an explicit instance grant. Automatic write capture and recurring Dreaming require separate consent.

## Dream operations

| Operation | Meaning | Evidence or condition |
|---|---|---|
| add | Save a missed durable lesson | Source and scope |
| revise | Correct or update an entry | Reason the earlier claim changed |
| merge | Consolidate overlapping knowledge | Preserve sources and distinct conditions |
| move | Change location or scope | Preserve meaning and update references; shared promotion requires maintainer acceptance |
| link | Relate separate knowledge | Root-relative resolvable link |
| mark | Record uncertainty or disagreement | Explain what remains unknown |
| retire | Remove invalid knowledge from active use | Explicit invalidity evidence; preserve in archive/history |
| index | Maintain navigation | No lost knowledge or broken references |

A Dreaming report records input references, reviewed commit, operations with before/after paths, evidence, unresolved questions, and separate method proposals. Low use alone does not justify retirement. Reorganization does not make an unverified entry verified. Rule or skill changes are proposals, not dream operations.
