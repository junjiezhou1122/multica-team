# Multica integration

This guide connects a skill-based instance to an existing workspace. It does not implement a memory service.

## Binding

Keep a binding outside the memory Git repository, in the workspace's persistent operational directory. Start from `templates/binding.example.json`. Replace example IDs and paths. `memory.visibility` is `local`, `private`, or `public`; `push_authorized` is an independent grant. `feedback.mode` is `preview` or `auto_issue`; `pr_authorized` is separate. `capture.mode` defaults to `explicit`; automated capture needs an explicit grant. `dreaming.trigger` is `manual` in version 0.1.0. No scheduler is provided.

No fixed coordinator, engineer, reviewer, or retrospective roles are required. All registered members receive read, own-memory-write, and candidate capabilities. Select any registered member as shared maintainer, and list authorized shared dreamers in `dreaming.agent_ids`. Job titles do not imply permission. Console Mops reads the same instance via its binding; owner-authorized console maintenance records its authority separately rather than impersonating a member.

The instance identity is server URL plus workspace UUID. Members and projects map IDs to directory keys. A directory key is a stable lowercase slug; no path separators or `..`. Credentials stay in the platform's credential stores. This mapping is routing, not authentication.

## Discover a company binding

Before any of the four memory skills uses a binding, respect an explicitly supplied binding or company target. An explicit binding and company must identify the same server/workspace; conflicts stop memory access and writes. For an explicit company without a supplied binding, read its entry and optional registration. Otherwise read `~/.config/multica-ops/companies.json` when present, using schema version 1 and the `companies` map. Select a valid `default_company`, or the sole company if no default is declared. Multiple companies require selection; an invalid default is an error. An unknown explicit target never falls back to a default.

Read the selected entry and resolve `memory_binding_path` from its registration or entry relative to the entry directory. Both pointers must agree when present. Verify binding identity against the company before memory access. Missing registry or absent optional pointer means memory is unconfigured; use setup only when requested or needed for the authorized memory task. Malformed configuration, unreadable selected files, and identity conflicts stop access rather than creating a replacement instance. Preserve existing grants. Discovery is read-only and requires no Team Ops installation.

## Attach to workers

1. Inspect live `multica skill --help`, `skill create --help`, `skill files --help`, and `agent skills --help`. Use explicit workspace selection for every call.
2. Import each required skill body and preserve its relative references. A body-only import breaks its links. Include SPEC, docs, templates, and referenced sibling skills as supporting files, or configure a persistent accessible plugin checkout and explicit absolute pointers. Verify where imported supporting files are materialized before relying on relative links.
3. Attach the resulting skill IDs to the intended agents, preserving existing assignments. Read back content, supporting files, and assignments.
4. Give each worker a persistent pointer to the local binding and the accessible memory instance. State its member/project scope. Installing the console plugin alone does not do this.
5. Verify a read-only lookup and a bounded write on a trial instance before claiming integration works. Any model run requires the user's existing or explicit grant. Do not use a live memory instance for destructive tests.

## Shared and remote runtimes

Members need distinct task branches/checkouts. The maintainer integrates candidates serially. A console path is not guaranteed to exist in a remote runtime. Remote workers need an authorized clone of the instance and a runtime-local binding. All instance credentials and remotes remain scoped to that workspace. Never make unavailable memory writable in a different workspace as a fallback.

## Existing operations systems

Team Ops retains its guides, decision log, and task workflow. The optional `memory_binding_path` in a local company registration or entry connects task lookup to the existing binding. Relative pointers resolve from the entry directory; dual pointers must agree. The binding's server/workspace must match the selected company. An absent binding leaves memory unconfigured, while a broken or conflicting pointer requires repair before memory access or company writes.

Use installed `/team-ops:mops` for company discovery and its company knowledge method. Team Ops invokes installed `/multica-team:team-memory` for canonical memory behavior. Separate plugin roots are supported; cross-plugin procedures use installed invocation or a runtime-configured accessible source with supporting files, never relative traversal into a sibling plugin. Invoke installed `/team-ops:mops` to load its company knowledge method; runtimes without slash commands use their configured accessible Team Ops skill source.

Task plans and handoffs cite applicable knowledge. Worker instructions carry the explicit binding and member/project IDs. Decision drafts and owner observation investigations stay in company operations. End-of-cycle retrospectives propose evidence-backed candidates; saving them and invoking Dreaming remain distinct authorized steps. Current assignments, resources and statuses come from live Multica. Guides retain permissions and acceptance criteria. Cross-project knowledge transfer needs a documented applicability check. Memory cannot override these sources.

Version 0.1.0 was authored against Multica CLI 0.6.1 help. CLI integration was researched, not installed or evaluated on a running team. Check current help before executing setup commands.
