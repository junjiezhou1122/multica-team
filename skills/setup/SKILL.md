---
name: setup
description: Set up or inspect a Multica workspace memory instance and its local binding. Use when onboarding an existing team to Multica Team; does not start task runs or enable automatic capture.
---

# Set up workspace memory

1. Follow [company binding discovery](../../docs/multica-integration.md#discover-a-company-binding) to find an existing instance before preparing one. Resolve the target Multica server and full workspace UUID from the user or an existing binding. Inspect live CLI help and read workspace/project/agent state using explicit `--workspace-id`. If the user selects another company, respect that selection. Stop on ambiguous identity rather than using a switchable CLI default.
2. Read [the specification](../../SPEC.md) and [integration instructions](../../docs/multica-integration.md). Locate an existing instance first. Choose a persistent directory outside plugin code, contribution repos, and task checkouts. Verify runtime access. A remote runtime cannot use a console-only local path.
3. Prepare local operational binding from [the example](../../templates/binding.example.json). Place it outside the memory repository. Map actual agent/project IDs to stable safe keys. Resolve the maintainer. Preserve existing grants; default to local storage, explicit capture, preview feedback, and manual dreams. Public hosting or pushing needs an explicit target and grant. Do not put credentials in the binding.
4. Inspect the destination. For a nonexistent or empty directory, copy [the memory template](../../templates/memory), adjust member/project keys and indexes, initialize a separate Git repository, inspect the changes, and make an initial local commit. Reuse a clean existing repository whose Git top-level is exactly the destination and contains MEMORY.md. For any other nonempty destination, stop without overwriting. Do not set global Git identity.
5. Follow [actual instance validation](../../docs/instance-validation.md) to validate memory links and the binding. Confirm the workspace mapping and intended files. Report paths, grants, reachable runtimes, and remaining setup gaps. Installing these skills for Multica workers is a separate step under the user's authorization; use current `skill` and `agent skills` help, retain existing assignments, and read back attachments.

When Team Ops company registration is part of the authorized setup, discover its existing entry and registry record first. Offer `memory_binding_path` in that local registration or entry, resolving relative paths from the entry directory. Verify the registration, entry, and binding identify the same server/workspace; preserve defaults, unrelated records, and existing grants. Use installed `/multica-team:mops` company discovery or an explicitly configured accessible Team Ops source, without assuming sibling plugin roots. Report an unwired company pointer as a setup gap.

Completed setup means an identifiable instance and valid binding, not automatic reads in new sessions. Add a persistent instruction pointer to the binding for each authorized worker. Do not schedule dreams or run evaluation sessions during setup.
