# Multica integration

This guide connects a skill-based instance to an existing workspace. It does not implement a memory service.

## Binding

Keep a binding outside the memory Git repository, in the workspace's persistent operational directory. Start from `templates/binding.example.json`. Replace example IDs and paths. `memory.visibility` is `local`, `private`, or `public`; `push_authorized` is an independent grant. `feedback.mode` is `preview` or `auto_issue`; `pr_authorized` is separate. `capture.mode` defaults to `explicit`; automated capture needs an explicit grant. `dreaming.trigger` is `manual` in version 0.1.0. No scheduler is provided.

No fixed coordinator, engineer, reviewer, or retrospective roles are required. All registered members receive read, own-memory-write, and candidate capabilities. Select any registered member as shared maintainer, and list authorized shared dreamers in `dreaming.agent_ids`. Job titles do not imply permission. Console Mops reads the same instance via its binding; owner-authorized console maintenance records its authority separately rather than impersonating a member.

The instance identity is server URL plus workspace UUID. Members and projects map IDs to directory keys. A directory key is a stable lowercase slug; no path separators or `..`. Credentials stay in the platform's credential stores. This mapping is routing, not authentication.

## Attach to workers

1. Inspect live `multica skill --help`, `skill create --help`, `skill files --help`, and `agent skills --help`. Use explicit workspace selection for every call.
2. Import each required skill body and preserve its relative references. A body-only import breaks its links. Include SPEC, docs, templates, and referenced sibling skills as supporting files, or configure a persistent accessible plugin checkout and explicit absolute pointers. Verify where imported supporting files are materialized before relying on relative links.
3. Attach the resulting skill IDs to the intended agents, preserving existing assignments. Read back content, supporting files, and assignments.
4. Give each worker a persistent pointer to the local binding and the accessible memory instance. State its member/project scope. Installing the console plugin alone does not do this.
5. Verify a read-only lookup and a bounded write on a trial instance before claiming integration works. Any model run requires the user's existing or explicit grant. Do not use a live memory instance for destructive tests.

## Shared and remote runtimes

Members need distinct task branches/checkouts. The maintainer integrates candidates serially. A console path is not guaranteed to exist in a remote runtime. Remote workers need an authorized clone of the instance and a runtime-local binding. All instance credentials and remotes remain scoped to that workspace. Never make unavailable memory writable in a different workspace as a fallback.

## Existing operations systems

Multica Ops can retain its guides, decision log, and task workflow. Add memory lookup and candidate handoffs rather than migrating all ops files. Current assignments, resources and statuses come from live Multica. Guides retain permissions and acceptance criteria. Cross-project knowledge transfer needs a documented applicability check. Memory cannot override these sources.

Version 0.1.0 was authored against Multica CLI 0.6.1 help. CLI integration was researched, not installed or evaluated on a running team. Check current help before executing setup commands.
