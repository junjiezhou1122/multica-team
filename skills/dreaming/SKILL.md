---
name: dreaming
description: Consolidate a Multica team's existing memory using specified task evidence. Use when explicitly asked to dream, reconcile notes, or review memory quality; produces local commits and separate method proposals, without scheduling itself.
---

Follow the [runtime guide](../../docs/runtimes.md) for client invocation, tool equivalents, and hook limits.

# Dream over team knowledge

1. Follow [company binding discovery](../../docs/multica-integration.md#discover-a-company-binding), then resolve the instance and maintainer role through [team-memory](../team-memory/SKILL.md). Read [the operation definitions](../../SPEC.md). Run only when invoked or under a separately authorized schedule. An invocation permits a bounded local memory edit; remote pushes still require the instance grant. Check `dreaming.agent_ids` for shared-memory dreaming capability. If the caller is neither the configured maintainer nor a listed dreamer, restrict direct edits to its member folder and submit shared changes as candidates. The caller's job title does not establish a capability.
2. Establish the input window from supplied tasks, reports, and source links. Read the current memory and starting commit. Do not ingest all session history automatically. Request access to unavailable sources or record the gap. A first dream may seed knowledge only from the authorized input window.
3. Compare evidence with existing entries. Look for missed reusable lessons, duplicates, contradictions, outdated claims, scope mistakes, broken links, and excessive indexes. Examine evidence that knowledge helped or misled later tasks. Without read/use traces, usage is unknown. Source verification may be read-only; do not run production experiments or new paid sessions to fill gaps without authorization.
4. Apply only justified operations: add, revise, merge, move, link, mark, retire, index. Preserve sources and explicit preferences. Mark unresolved disputes instead of choosing a convenient answer. A promotion into shared/project memory requires maintainer acceptance. Retire only with invalidity evidence and preserve the prior claim; never retire solely because no recent task used it.
5. Write a report using [the dream template](../../templates/dream-report.md). Record evidence for each operation, reviewed commit, paths, unresolved questions, and method proposals. Keep task transcripts and private source content out of public reports. Changes to skills, company permissions, review criteria, or workflows remain proposals; send plugin defects through [feedback](../feedback/SKILL.md) only under that workflow's grant.
6. Inspect and validate the diff, then commit only intended files using team-memory's concurrency checks. Report the resulting commit and exact operations. Push only when authorized and verify the remote result. End without creating another dream or scheduler.

A successful dream makes justified changes or reports that none are needed. Entry count, file count, and elapsed runtime are not evidence that memory became useful. Structural checks do not establish factual truth.
