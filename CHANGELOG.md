# Changelog

## 0.3.0

Follow-up adds explicit Codex-native plugin and marketplace metadata, tests installation with compatibility manifests removed, and puts all four client installation routes directly in the README.

Added native packaging and installation guidance for Codex, Pi, and Hermes alongside Claude Code. All clients discover the same 23 skills and retain the full supporting tree. Pi declares skills only; Hermes uses Agent Plugins v1 metadata. The existing four hooks remain Claude Code adapters.

Replaced stale claims that other clients have no slash commands and removed Claude-only argument placeholders. Added runtime capability and collision guidance, coherent manifest checks, relocated package checks, isolated native discovery tests, and current Multica Team installation inventory including Pi local packages. Hermes portable manifest and discovery pass, while catalog security scanning still rejects inherited fixtures and examples. No model calls, automatic services, or grants are added.

## 0.2.0

Consolidated company operations and memory into one `multica-team` plugin with 23 root skills and the unified `/multica-team:*` namespace. Operations documents, templates, scripts, and Apache-2.0 attribution remain under `operations/`; inherited hooks are discovered from root `hooks/hooks.json`. Removed nested plugin manifests and the separate marketplace entry.

Company discovery retains `~/.config/multica-ops/companies.json`. Optional bindings connect task knowledge lookup, decision drafts and grill-with-doc, owner observations, and retrospective memory proposals to canonical memory skills in the same package. Hook ownership recognizes both legacy and current operator declarations. Added single-package reference validation and relocated discovery checks to CI. No capture, scheduling, or grants are enabled.

## 0.1.0

Initial skill-based version: setup, scoped team memory, manual dreaming, feedback previews and authorized submissions, instance templates, structural checks, and Multica integration instructions. No automated scheduler or live deployment included.
