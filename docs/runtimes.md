# Choose your agent client

Multica Team provides the same 23 skills to Claude Code, Codex, Pi, and Hermes. Keep the entire repository installed. Skills link to sibling skills and to `operations/`, `docs/`, and `templates/`. Copying only a `SKILL.md` breaks those references.

These instructions select the client for your advisor console. Multica worker runtimes still need their own reachable skill files, CLI access, and instance binding. See [worker integration](multica-integration.md).

## Capability matrix

| Client | Package discovery | Explicit invocation | Four inherited hooks |
|---|---|---|---|
| Claude Code | `.claude-plugin/plugin.json` and marketplace | `/multica-team:mops` | Claude event adapters and regression tests |
| Codex | Same marketplace and plugin metadata | `$mops`, or select the plugin skill in `/skills` | No adapted or verified Codex hooks |
| Pi | `package.json` with `pi.skills`, or `--skill` | `/skill:mops` | No Pi extension adapters |
| Hermes | Root Agent Plugins v1 `plugin.json`, or a skill directory mount | Discover the qualified plugin skill with `skills_list` and load it with `skill_view`; directory mounts also expose `/mops` and `/skill mops` | No Hermes hook adapters |

All clients can follow the skill procedures and run the supporting scripts through their own file and shell tools. A skill's instructions do not enforce a security boundary. On clients without hook adapters, the migration, outward-action, rule-placement, and dispatch checks remain explicit workflow steps. Read [security](../operations/SECURITY.md) and inspect company state before acting. Do not claim that an action was blocked by a hook on those clients.

The `/multica-team:*` strings in inherited procedures identify flows using Claude syntax. Translate them for the active client. Treat invocation arguments and the user's accompanying message as the request. If a client leaves `$ARGUMENTS` literally in a skill body, it is a placeholder, not a command or environment variable to evaluate. Use the actual user request instead. Use the client's available tools for reading files, shell commands, questions, and delegation. Missing tools are a capability gap; they do not grant permission to install software or launch another agent service.

## Claude Code

```sh
claude plugin marketplace add junjiezhou1122/multica-team
claude plugin install multica-team@multica-team
```

Start a new session or run `/reload-plugins`, then invoke `/multica-team:mops` with your request. For a temporary local checkout, use `claude --plugin-dir /absolute/path/to/multica-team`.

The root `hooks/hooks.json` belongs to Claude Code. Installation does not create a company, enable memory capture, or schedule Dreaming.

## Codex

```sh
codex plugin marketplace add junjiezhou1122/multica-team
codex plugin add multica-team@multica-team
```

For a local checkout, replace the marketplace source with `/absolute/path/to/multica-team`. Start a new session and use `/skills` to select the installed plugin skill, or type `$mops` followed by your request. When another package has the same skill name, select the Multica Team entry and inspect its path.

An alternative for clients without plugin commands is a project mount. From the project root, create `.agents/skills` and link each directory in the checkout's `skills/` there. Keep the checkout in place so relative supporting references still resolve. Inspect existing entries before adding links and do not overwrite another skill with the same name.

## Pi

```sh
pi install /absolute/path/to/multica-team
```

Pi records the local package path without copying it. Keep the checkout in place. To install from Git instead:

```sh
pi install git:github.com/junjiezhou1122/multica-team
```

Invoke `/skill:mops` followed by your request. Use `/reload` after updating a checkout in an active session. For a session without persistent installation:

```sh
pi --skill /absolute/path/to/multica-team/skills
```

The Pi manifest declares only skills. It registers no extensions, prompts, or themes, and does not adapt Claude hooks. Skill names are bare, so resolve a collision by loading the intended skill file or disabling the conflicting package resource.

## Hermes

The root `plugin.json` is an Agent Plugins v1 package. Hermes discovers all 23 skills without importing Python plugin code. Portable plugin skills use Hermes-generated qualified names. Use `skills_list` to find the exact name ending in `:mops`, then ask the agent to load it with `skill_view` and follow your request.

Hermes's plugin installation and catalog validation scan the repository. The inherited operations tree contains security test fixtures and shell examples that this scan flags as dangerous. The portable manifest and skill discovery pass, but the default native plugin installation is not a supported route yet. Do not disable the scan or override its rejection to install this package.

For reviewed local skill workflows, keep a full checkout and use Hermes's `skills.external_dirs` in the selected profile's `config.yaml`:

```yaml
skills:
  external_dirs:
    - /absolute/path/to/multica-team/skills
```

Merge the entry with existing skill settings and restart the session. This is an explicit user configuration change, not an installation side effect. A directory mount keeps all references attached to the checkout. Invoke `/mops` or `/skill mops`. Hermes reserves some bare names, including `status`; use `/skill status` or the exact discovered path when a built-in or another skill collides.

Hermes's `skill_view` file argument serves files inside an individual skill directory. To read a linked `../../docs`, `../../operations`, template, or specification file, use the client's file or terminal tool and resolve the path from the loaded `SKILL.md` location. Keep the full checkout reachable. If that tool is unavailable or its sandbox cannot read the checkout, stop and report the missing access.

## Verification and limits

Run `python3 scripts/check.py` and `python3 scripts/test-portability.py` for package and isolated installation checks. The portability suite always checks whole-tree references and inventory behavior. With clients installed, it also tests Claude manifest validation, Codex marketplace installation, Pi package installation and its native skill loader, and Hermes's native portable package loader. The suite uses temporary configuration directories and makes no model calls. Missing clients are reported as skipped.

These checks prove packaging and discovery. They do not prove live model compliance, Multica worker access, or remote memory access. Company creation, service startup, automatic capture, scheduled work, and paid model calls still need the applicable user authorization.
