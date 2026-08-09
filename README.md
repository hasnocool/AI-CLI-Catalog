# AI CLI Catalog

A machine-readable catalog of terminal-first **AI coding agents**, **agent harnesses**, **agent orchestrators**, **agent frameworks**, **local inference runtimes**, **gateways**, and supporting CLI infrastructure.

> Last reviewed: 2026-08-09
> Catalog entries: **86**

## Catalog schema v2

`catalog.json` now records installer and capability metadata suitable for launchers, dashboards, routers, audits, and automated discovery. Feature flags are tri-state: `true`, `false`, or `null` when not yet verified.

Key fields: `category`, `installer`, `installer_type`, `binary`, `open_source`, `local_models`, `openai_compatible`, `mcp`, `acp`, `subscription_auth`, `api_key`, `daemon_server`, `last_verified`, and `official_source`.

## Categories

| Category | Entries |
|---|---:|
| `agent-framework` | 5 |
| `agent-harness` | 26 |
| `agent-infrastructure` | 7 |
| `agent-launcher` | 1 |
| `agent-orchestrator` | 9 |
| `agent-ui` | 1 |
| `coding-agent` | 5 |
| `gateway` | 3 |
| `general-ai-cli` | 5 |
| `inference` | 5 |
| `model-tooling` | 1 |
| `provider-agent` | 15 |
| `provider-cli` | 1 |
| `provider-infrastructure` | 2 |

## Newly added in the deep-search pass

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| Auggie CLI | `provider-agent` | `npm install -g @augmentcode/auggie` | `auggie` | https://www.augmentcode.com/product/CLI |
| Cody CLI | `provider-agent` | `npm install -g @sourcegraph/cody` | `cody` | https://sourcegraph.com/docs/cody/clients/install-cli |
| Junie CLI | `provider-agent` | `curl -fsSL https://junie.jetbrains.com/install.sh \| bash` | `junie` | https://junie.jetbrains.com/docs/junie-cli.html |
| Qodo Gen CLI | `provider-agent` | `npm install -g @qodo/gen` | `qodo` | https://docs.qodo.ai/qodo-documentation/qodo-gen/cli/setup-and-quickstart |
| Agent Harness (Go) | `agent-harness` | `curl -fsSL https://raw.githubusercontent.com/BA-CalderonMorales/agent-harness/main/scripts/install.sh \| bash` | `agent-harness` | https://github.com/BA-CalderonMorales/agent-harness |
| Codebuff | `agent-harness` | `npm install -g codebuff` | `codebuff` | https://www.codebuff.com/docs/help/quick-start |
| Dot Coding Agent | `agent-harness` | `uv tool install dot-coding-agent` | `dot` | https://pypi.org/project/dot-coding-agent/ |
| ForgeCode | `agent-harness` | `curl -fsSL https://forgecode.dev/cli \| sh` | `forge` | https://forgecode.dev/docs/piping-guide/ |
| Hermes Agent | `agent-harness` | `curl -fsSL https://hermes-agent.nousresearch.com/install.sh \| bash` | `hermes` | https://hermes-agent.nousresearch.com/docs/ |
| Koder | `agent-harness` | `uv tool install koder` | `koder` | https://github.com/feiskyer/koder |
| Oh My Pi | `agent-harness` | `npm install -g @oh-my-pi/pi-coding-agent` | `omp` | https://github.com/can1357/oh-my-pi |
| OpenHarness | `agent-harness` | `curl -fsSL https://raw.githubusercontent.com/HKUDS/OpenHarness/main/scripts/install.sh \| bash` | `oh` | https://github.com/HKUDS/OpenHarness |
| RA.Aid | `agent-harness` | `pip install ra-aid` | `ra-aid` | https://docs.ra-aid.ai/quickstart/installation/ |
| VTX Coding Agent | `agent-harness` | `curl -fsSL https://raw.githubusercontent.com/OEvortex/vtx-coding-agent/main/scripts/install.sh \| bash` | `vtx` | https://pypi.org/project/vtx-coding-agent/ |
| Agent Deck | `agent-orchestrator` | `curl -fsSL https://raw.githubusercontent.com/asheshgoplani/agent-deck/main/install.sh \| bash` | `agent-deck` | https://github.com/asheshgoplani/agent-deck |
| Claude Squad | `agent-orchestrator` | `curl -fsSL https://raw.githubusercontent.com/smtg-ai/claude-squad/main/install.sh \| bash` | `cs` | https://github.com/smtg-ai/claude-squad |
| Open Ralph Wiggum | `agent-orchestrator` | `npm install -g @th0rgal/ralph-wiggum` | `ralph` | https://github.com/Th0rgal/open-ralph-wiggum |
| Ralph CLI | `agent-orchestrator` | `curl -fsSL https://raw.githubusercontent.com/kylemclaren/ralph/main/install.sh \| sh` | `ralph` | https://github.com/kylemclaren/ralph |
| Ralph Starter | `agent-orchestrator` | `npm install -g ralph-starter` | `ralph-starter` | https://ralphstarter.ai/docs/installation |
| Ralph-E | `agent-orchestrator` | `npm install -g @ralph-e-cli/ralph-e` | `ralph-e` | https://www.npmjs.com/package/@ralph-e-cli/ralph-e |
| Docker Agent | `agent-framework` | `brew install docker-agent` | `docker-agent` | https://docker.github.io/docker-agent/getting-started/installation/ |
| AI CLI | `general-ai-cli` | `npm install -g ai-cli` | `ai` | https://www.npmjs.com/package/ai-cli |
| Spec Kit / Specify CLI | `agent-infrastructure` | `uv tool install specify-cli` | `specify` | https://github.github.com/spec-kit/installation.html |
| Claude Code Router | `gateway` | `npm install -g @musistudio/claude-code-router` | `ccr` | https://musistudio.github.io/claude-code-router/docs/cli/installation/ |
| llama-swap | `gateway` | `brew install llama-swap` | `llama-swap` | https://github.com/mostlygeek/llama-swap |
| llmfit | `model-tooling` | `curl -fsSL https://llmfit.axjns.dev/install.sh \| sh` | `llmfit` | https://www.llmfit.org/ |

## Built-in catalog CLI

The repository includes a Python 3.12 CLI for querying the machine-readable catalog without scraping the README. Installer execution is deliberately opt-in.

```bash
# Search/filter
python scripts/catalog.py list --category coding-agent
python scripts/catalog.py list --local-models true --mcp true
python scripts/catalog.py list --text google --json

# Inspect one entry
python scripts/catalog.py show opencode

# Print an installer without executing it
python scripts/catalog.py install opencode

# Explicitly execute the cataloged upstream installer
python scripts/catalog.py install opencode --execute
```

`catalog.schema.json` documents the machine schema, while `scripts/validate_catalog.py` enforces unique slugs, required fields, tri-state feature values, dates, and source URLs. GitHub Actions runs validation and CLI smoke tests on pushes and pull requests.

## Query examples

```bash
# All tools that support local models
jq -r '.entries[] | select(.local_models == true) | [.name,.binary,.installer] | @tsv' catalog.json

# MCP-capable agent harnesses
jq -r '.entries[] | select(.category == "agent-harness" and .mcp == true) | .name' catalog.json

# Shell-script installers verified today
jq -r '.entries[] | select(.installer_type == "shell-script" and .last_verified == "2026-08-09") | .installer' catalog.json

# Tools that expose or consume OpenAI-compatible APIs
jq -r '.entries[] | select(.openai_compatible == true) | [.name,.category] | @tsv' catalog.json
```

## Security

A catalog entry is **not** an endorsement of running a remote installer without inspection. `curl | sh` / `curl | bash` executes downloaded code immediately. Verify the upstream domain, inspect scripts when practical, prefer signed/checksummed releases where available, and avoid running installers as root unless required.

## Machine-readable source of truth

The README is a human-friendly view. **`catalog.json` is the canonical source of truth.** New automation should consume the JSON rather than scrape Markdown tables.

## Contributing

Additions should include an upstream source, a reproducible installer command, the installed binary name, and a fresh `last_verified` date. Capability flags should remain `null` rather than guessed when support has not been verified.
