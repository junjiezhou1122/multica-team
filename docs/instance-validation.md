# Validate a created instance

This procedure checks the actual instance, not the packaged example. Run it before setup completion and before a memory commit. The package checker does not take an instance argument in version 0.1.0.

1. Resolve the binding's memory path and run `git -C <memory-path> rev-parse --show-toplevel`. Its resolved result must equal that path, and root MEMORY.md must exist. Before editing, `git status --porcelain` must be empty. Record HEAD and ensure it has not changed before staging.
2. Parse the binding as JSON. Verify schema_version is 1, server URL and workspace UUID match the intended live company, maintainer_agent_id and all dreaming.agent_ids occur in members, and member/project directory keys are unique lowercase slugs within each mapping. Verify every mapped folder has MEMORY.md. Inspect grants against their recorded owner authorization; booleans alone do not create authority.
3. Enumerate Markdown files under the instance. For every `[[path]]`, resolve from the instance root, append .md only when the path has no extension, and verify the target exists inside the root. Reject external symlinks, absolute targets, and traversal outside the root. Links in member indexes use the same root.
4. For changed knowledge entries, inspect source/date metadata, attribution, scope, and uncertainty. Follow the source for disputed corrections. Check that moved/retired entries retain evidence and updated references. Confirm the public/private publication policy separately; link validation is not a privacy or truth check.
5. Inspect `git diff` and status, stage only intended paths, commit the batch, and read back the commit. Report these checks, paths, and unresolved gaps. Structural failures stop the commit; factual uncertainty is marked explicitly instead of claiming verification.

Use the real runtime's filesystem. A successful local inspection cannot establish that a cloud worker can access the instance.
