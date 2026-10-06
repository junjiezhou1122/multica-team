# multica-team

Skills and workflows for Multica teams, starting with shared memory, dreaming, and feedback.

A workspace gets its own memory Git repository. Members keep personal working knowledge in their own folders, propose shared lessons, and read project knowledge when it is relevant. Dreaming consolidates that knowledge. Feedback helps improve this plugin without exporting an entire user's memory.

Version 0.1.0 is a skill-based workflow. It has no database, background daemon, automatic scheduler, or native Multica memory API. Installing the console plugin does not install skills for Multica agents.

## Two repositories

- This repository contains reusable procedures, templates, and documentation.
- An instance repository contains one workspace's knowledge. It can be public or private by explicit owner choice. Each workspace should use a separate instance.

Bindings stay in local operational configuration outside the memory repository. They identify the Multica server, workspace, agents, projects, memory path, and permissions. Credentials never belong in either repository.

## Install in Claude Code

Register this repository as a marketplace and install its plugin:

```sh
claude plugin marketplace add junjiezhou1122/multica-team
claude plugin install multica-team@multica-team
```

The plugin exposes `/multica-team:setup`, `/multica-team:team-memory`, `/multica-team:dreaming`, and `/multica-team:feedback`. Other skill-capable agents can consume the `skills/` directories. No Devin plugin or CLI implementation is included.

## First workspace

Invoke setup with an existing workspace and a persistent workspace directory:

```text
/multica-team:setup
Use my existing Multica workspace. Create its memory repository in the
workspace's persistent directory. Keep it local until I choose a remote.
```

Setup resolves the workspace explicitly, prepares a binding using [the example](templates/binding.example.json), and copies [the instance template](templates/memory). It verifies the Git root and links. It does not move existing guides, change permissions, install dependencies, or start paid runs.

Read [Multica integration](docs/multica-integration.md) before attaching skills to agents or using remote runtimes. Local paths only work for runtimes that can reach them.

## Daily work

```text
/multica-team:team-memory
Read the memory relevant to this task and member. Save this verified
lesson in my member folder and propose it for the team.
```

Members can update their own folders on task branches. The configured maintainer accepts candidates into shared team or project knowledge. A source is evidence, not an executable instruction. Workflow rules, permissions, and acceptance criteria remain in the team's authoritative guides.

## Dreaming

```text
/multica-team:dreaming
Review these completed tasks and their evidence. Consolidate the related
memory, explain the operations, and make a local commit.
```

Dreaming supports `add`, `revise`, `merge`, `move`, `link`, `mark`, `retire`, and `index`. It preserves sources, unresolved disagreements, and explicit preferences. It proposes changes to skills or company rules separately. It runs when invoked; scheduling requires a separate opt-in.

## Feedback

```text
/multica-team:feedback
The member index did not lead me to a relevant project lesson.
```

Feedback defaults to a local preview. An instance can authorize automatic issue submission to the configured plugin repository. Fixes need validation and independent review before a PR. Plugin problems go upstream; incorrect instance knowledge stays with the instance. See [feedback policy](docs/feedback.md).

## Format and checks

[The specification](SPEC.md) preserves Agent Memory Repo's short `MEMORY.md`, one-line bullets, source/date metadata, and root-relative `[[path]]` links. Member indexes are a Multica Team convention, not separate link roots.

Run the offline structural check:

```sh
python3 scripts/check.py
```

It checks plugin JSON, skill frontmatter, local documentation links, template bindings, and template memory links. It does not prove model compliance, factual correctness, access isolation, or absence of secrets.

## Status and origins

This first version is a documented workflow with structural validation. No live Multica installation, paid agent evaluation, or production Dreaming run has been performed as part of authoring it.

The format and base workflow are adapted from [Agent Memory Repo](https://github.com/AgentMemoryRepo/agentmemoryrepo), originally developed by Cognition. Dreaming's behavior is informed by [Devin's public documentation](https://docs.devin.ai/product-guides/memory). This project does not contain Devin's proprietary implementation. See [NOTICE](NOTICE).

Contributions follow [CONTRIBUTING.md](CONTRIBUTING.md). Licensed under [MIT](LICENSE).
