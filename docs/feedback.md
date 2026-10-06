# Feedback and publication policy

This policy is for instances submitting plugin feedback. The default is a local preview. Automatic issue submission requires the owner to authorize the target repository and publishable evidence scope, recorded in the local binding. A PR grant is separate. No grant means preview.

For auto_issue, `feedback.issue_grant` must contain `repository` matching the feedback target, `authorized_by`, `source` of the owner's authorization, and `publishable_scope` describing the permitted evidence. Optional `expires_at` is an ISO timestamp; an expired grant is inactive. A selected mode is not a grant. Inspect the proposed issue against the recorded scope; absent, ambiguous, expired, or insufficient grants fall back to preview. `pr_authorized` is only an indicator: PR work still needs a recorded owner grant in operational decisions and final-HEAD independent review.

Public and private instances both work. A public choice applies only to the material the owner meant to publish. Never include credentials or blindly upload raw sessions, personal memory, operational bindings, or local configuration. Inspect newly written notes and reports before an authorized push. Visibility is not a secret scanner.

Feedback is routed by ownership:

- Wrong or missing knowledge belongs to the instance.
- Broken retrieval, writing, dreaming, templates, or checks belongs to the plugin.
- Permissions or acceptance criteria belong to the company's owner.
- A business project's defect belongs to that project's workflow and authorization.

Issue previews include expected/actual behavior, version, reproducible steps, publishable evidence, and proposed scope. Search issues/PRs before submitting. Receipts belong to operational state, not durable knowledge. Automatic issue submission does not imply automatic repair, merge, release, or instance upgrade.
