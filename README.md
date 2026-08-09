# AI CLI Catalog

A machine-readable catalog of terminal-first **AI coding agents**, **agent harnesses**, **agent orchestrators**, **agent frameworks**, **local inference runtimes**, **gateways**, and supporting CLI infrastructure.

> Last reviewed: 2026-08-09  
> Catalog entries: **86**

## Catalog schema v2

`catalog.json` records installer and capability metadata suitable for launchers, dashboards, routers, audits, and automated discovery. Feature flags are tri-state: `true`, `false`, or `null` when support has not yet been verified.

Key fields:

- `category`
- `installer`
- `installer_type`
- `binary`
- `open_source`
- `local_models`
- `openai_compatible`
- `mcp`
- `acp`
- `subscription_auth`
- `api_key`
- `daemon_server`
- `last_verified`
- `official_source`

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

## Built-in catalog CLI

The repository includes a Python 3.12 CLI for querying the machine-readable catalog without scraping the README. Installer execution is deliberately opt-in.

```bash
# Search/filter
python scripts/catalog.py list --category agent-harness
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
