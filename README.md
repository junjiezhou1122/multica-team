# Multica Team

Run an AI team on Multica, keep shared knowledge, and improve how the team works. One plugin connects company operations, evidence-backed decisions, team memory, Dreaming, and feedback.

Multica Team 0.3.0 provides **23 shared skills for Claude Code, Codex, Pi, and Hermes**. You direct the team through the company advisor. Members consult relevant knowledge, work within the company's permissions, and propose reusable lessons after a task.

## Install

Choose your client using the [runtime guide](docs/runtimes.md). It covers installation, invocation, collisions, and the capability matrix for all four clients. The commands below use Claude Code syntax. Codex uses `$mops` or `/skills`, Pi uses `/skill:mops`, and Hermes uses its discovered skill names.

### Claude Code

```sh
claude plugin marketplace add junjiezhou1122/multica-team
claude plugin install multica-team@multica-team
```

Reload plugins with `/reload-plugins`, or start a new session. Invoke `/multica-team:mops`.

### Codex

```sh
codex plugin marketplace add junjiezhou1122/multica-team
codex plugin add multica-team@multica-team
```

Codex uses its native `.codex-plugin/plugin.json` and `.agents/plugins/marketplace.json`. Start a new session. Select the Multica Team skill in `/skills`, or invoke `$mops` with your request. Installation retains the complete skill and reference tree. The Codex manifest explicitly declares skills and no hooks; Claude hook adapters remain separate.

### Pi

```sh
pi install git:github.com/junjiezhou1122/multica-team
```

Invoke `/skill:mops`. Pi reads the skills declared in the root `package.json`.

### Hermes

Clone this repository to a persistent directory. Add its `skills/` path to `skills.external_dirs` in your Hermes profile configuration, preserving existing entries:

```yaml
skills:
  external_dirs:
    - /absolute/path/to/multica-team/skills
```

Restart the session and invoke `/mops` or `/skill mops`. Keep the full checkout reachable. The [Hermes guide](docs/runtimes.md#hermes) explains supporting-file access and why native plugin installation remains pending its security scan.

### Migrate the former Claude Code plugin

If you previously installed `team-ops@multica-team`, uninstall it before updating to the unified plugin. This prevents duplicate operations hooks:

```sh
claude plugin uninstall team-ops@multica-team --keep-data
claude plugin update multica-team@multica-team
```

Installation adds skills to your console. Claude Code also loads the four inherited hooks. Codex, Pi, and Hermes currently use explicit skill workflows without adapted hooks. Creating Multica members and attaching worker skills are separate operations. The plugin does not start a company or enable automatic capture during installation.

## Start with your team

For an existing company, supply its entry or workspace:

```text
/multica-team:mops
Use my existing company at /absolute/path/to/company.
Inspect its current setup before changing anything.
```

For a new team, describe the goal and the control you want:

```text
/multica-team:mops
Build a team that contributes to an open-source project.
I choose when each contribution starts. Propose the workflow and team first.
```

To add memory to an existing workspace:

```text
/multica-team:setup
Use my existing workspace and create a separate memory Git repository
in its persistent directory. Keep it local.
```

Setup locates an existing instance before creating one. It prepares a binding, validates the instance, and reports runtime access and remaining gaps. See [worker integration](docs/multica-integration.md) before attaching skills to members.

## Find your company from any directory

Register company entry paths in `~/.config/multica-ops/companies.json`. The path is retained for compatibility. The advisor and memory skills read this file on invocation, so company details do not need to live in global instructions.

A registration contains a company name, server URL, workspace UUID, and entry path. An optional `memory_binding_path` connects the same company to its knowledge instance. Explicit targets take precedence over the registered default. Conflicting identities or binding paths stop access instead of silently selecting another company.

Follow [company discovery](operations/LOCAL_COMPANIES.md) for the registration format and [binding discovery](docs/multica-integration.md#discover-a-company-binding) for memory routing.

## Use the main commands

| Goal | Command |
|---|---|
| Discuss, build, or operate a company | `/multica-team:mops` |
| Inspect progress and decisions needing attention | `/multica-team:status` |
| Add memory to an existing workspace | `/multica-team:setup` |
| Find, save, correct, or propose knowledge | `/multica-team:team-memory` |
| Consolidate a specified set of memories and evidence | `/multica-team:dreaming` |
| Diagnose plugin feedback and prepare an issue | `/multica-team:feedback` |

The [operations command reference](operations/COMMANDS.md) covers the other commands, including joining a company, importing tasks, hiring, review, recovery, and delivery.

Read knowledge before work:

```text
/multica-team:team-memory
Find the lessons relevant to this task. Cite their sources and limits.
```

Save a lesson with evidence:

```text
/multica-team:team-memory
Save this observation from the completed task: …
Source: …
Propose it for shared knowledge if it applies beyond this member.
```

Members maintain their own folders on isolated branches. The configured maintainer accepts shared candidates. Capabilities come from registered identities and grants, rather than prescribed job titles.

## Improve the company through evidence

The [company knowledge method](operations/COMPANY_KNOWLEDGE.md) connects task intake, decisions, owner observations, and retrospectives.

When you report a problem, the advisor distinguishes your words from its interpretation of your intent. It gathers supporting and conflicting evidence, proposes a causal hypothesis, and records a bounded intervention with a prediction and validation plan. Investigations and interventions remain within existing authorization.

Each decision has a document linked from the company's `DECISIONS.md`. Grill-with-doc keeps confirmed choices, open questions, evidence, and later results together. Future sessions continue from that document.

A retrospective proposes reusable knowledge with its source, scope, and uncertainty. Pending experiments stay in company operations. Saving a candidate and accepting it into shared memory remain explicit steps.

This is an agent workflow and a set of templates. It does not install a background observation service or automatically run experiments.

## Consolidate memory and route feedback

Invoke Dreaming with a bounded set of inputs:

```text
/multica-team:dreaming
Review these completed tasks and their evidence: …
Consolidate related memory, preserve sources and disagreements,
and explain the proposed changes.
```

Dreaming supports `add`, `revise`, `merge`, `move`, `link`, `mark`, `retire`, and `index`. It preserves evidence and requires the applicable scope authorization. It runs on invocation. Recurring execution needs separate setup and consent.

Plugin feedback defaults to an issue preview. Incorrect knowledge belongs to the memory instance, company policy belongs to its decision process, and project defects follow that project's workflow. Publishing an issue or fix requires the recorded grant. See [feedback policy](docs/feedback.md).

## Keep the right information in each place

| Information | Home |
|---|---|
| Reusable methods, skills, and checks | This plugin repository |
| Permissions, workflow, and acceptance criteria | Company guides |
| Decision documents, observations, and experiments | Company operations directory |
| Reusable team, project, and member knowledge | Separate memory Git repository |
| Current assignments and runs | Live Multica state |
| Company paths and memory routing | Local registry and binding |

Each workspace owns a separate memory instance. Public or private hosting is an owner choice; pushing requires a separate grant. Registrations, credentials, bindings, and raw company conversations stay outside the public plugin repository.

The [memory specification](SPEC.md) defines short `MEMORY.md` indexes, one-line entries with source and date metadata, and links relative to the memory repository root. Memory supplies knowledge. It cannot change permissions or acceptance criteria.

## Repository layout

```text
skills/          23 company and memory skills
operations/      Company methods, templates, tools, and Apache-2.0 attribution
hooks/           Migration, outward-action, rule-placement, and dispatch hooks
docs/            Memory integration and validation references
templates/       Memory instance and binding templates
scripts/         Package validation
```

Claude Code loads the root hooks for `SessionStart`, `PreToolUse`, and `PostToolUse`. Read [hook behavior](operations/SECURITY.md#what-this-is-mechanically) before changing their scope. These checks do not provide filesystem isolation or guarantee agent compliance.

## Verify changes

Run the package check and company discovery tests:

```sh
python3 scripts/check.py
python3 scripts/test-portability.py
python3 -m unittest discover -s operations/scripts/tests -p test_company_discovery.py
```

The package check verifies coherent runtime manifests, all 23 shared skill bodies, maintained references, Claude hooks, licenses, example binding, and template memory links. The portability suite tests installed native clients offline in temporary configuration directories and reports missing clients as skipped. CI also runs regression suites for the inherited hooks. The [instance validation procedure](docs/instance-validation.md) separately checks an actual memory repository.

Passing structural and routing tests does not establish factual correctness, model compliance, secret absence, or remote-worker access. Version 0.3.0 has package, routing, native skill discovery, and Claude hook validation. Hermes catalog admission still fails its repository-wide scanner on inherited fixtures and examples; see the runtime guide. Full live agent evaluation of the unified workflow remains pending. There is no database, automatic scheduler, or native Multica memory service in this version.

## Origins and licenses

The memory format and base workflow adapt [Agent Memory Repo](https://github.com/AgentMemoryRepo/agentmemoryrepo), developed by Cognition. [Devin's public Memory documentation](https://docs.devin.ai/product-guides/memory) informed Dreaming's design. No proprietary Devin implementation is included.

The company operations component is a modified fork of [jamillazarev/multica-ops](https://github.com/jamillazarev/multica-ops) by Jamil Lazarev. We imported version **0.4.19**, at commit [`1cf9184`](https://github.com/jamillazarev/multica-ops/commit/1cf9184c6165703e9d9b9b3c2a1393c141958730), and integrated its 19 operations skills and hooks into this repository.

Our changes unify company operations and team memory under one plugin, add invocation-time company and binding discovery, and connect decision documents, owner observations, and retrospectives to the memory workflow. Multica Team maintains this fork independently. It does not automatically track upstream updates or imply upstream endorsement. Original Apache-2.0 licensing and attribution are retained.

Original memory material and root code use [MIT](LICENSE). Operations resources, the 19 operations skills, and inherited hooks retain [Apache-2.0](operations/LICENSE). See [NOTICE](NOTICE), [maintenance](operations/MAINTENANCE.md), and [contribution guidance](CONTRIBUTING.md).
