# AI CLI Catalog

A machine-readable catalog of terminal-first **AI coding agents**, **agent harnesses**, **agent orchestrators**, **agent frameworks**, **local inference runtimes**, **gateways**, and supporting CLI infrastructure.

> Last reviewed: 2026-08-17
> Catalog entries: **443**

## Catalog schema v2

`catalog.json` now records installer and capability metadata suitable for launchers, dashboards, routers, audits, and automated discovery. Feature flags are tri-state: `true`, `false`, or `null` when not yet verified.

Key fields: `category`, `installer`, `installer_type`, `binary`, `open_source`, `local_models`, `openai_compatible`, `mcp`, `acp`, `subscription_auth`, `api_key`, `daemon_server`, `last_verified`, and `official_source`.

## Categories

| Category | Entries |
|---|---:|
| `agent-infrastructure` | 70 |
| `coding-agent` | 57 |
| `mcp-tooling` | 54 |
| `agent-harness` | 47 |
| `agent-orchestrator` | 37 |
| `provider-agent` | 27 |
| `inference` | 23 |
| `agent-framework` | 22 |
| `provider-infrastructure` | 19 |
| `observability` | 17 |
| `gateway` | 15 |
| `eval-harness` | 13 |
| `agent-ui` | 10 |
| `security-eval` | 9 |
| `general-ai-cli` | 8 |
| `model-tooling` | 6 |
| `provider-cli` | 5 |
| `acp-bridge` | 2 |
| `agent-launcher` | 2 |

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

## Newly added in the August 2026 expansion pass

This pass adds **73** newly verified, de-duplicated tools, bringing the catalog to **159 entries**. It broadens coverage into ACP bridges, MCP tooling, evaluation harnesses, inference servers, provider infrastructure, gateways, and additional terminal coding agents.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| Claude Agent ACP | `acp-bridge` | `npm install -g @agentclientprotocol/claude-agent-acp` | `claude-agent-acp` | https://www.npmjs.com/package/@agentclientprotocol/claude-agent-acp |
| Codex ACP | `acp-bridge` | `npm install -g @agentclientprotocol/codex-acp` | `codex-acp` | https://www.npmjs.com/package/@agentclientprotocol/codex-acp |
| AutoGen Studio | `agent-framework` | `pip install -U autogenstudio` | `autogenstudio` | https://microsoft.github.io/autogen/stable/user-guide/autogenstudio-user-guide/installation.html |
| Flowise | `agent-framework` | `npm install -g flowise` | `flowise` | https://docs.flowiseai.com/getting-started |
| Genkit CLI | `agent-framework` | `npm install -g genkit-cli` | `genkit` | https://firebase.google.com/docs/genkit/get-started |
| Google Agent Development Kit (ADK) | `agent-framework` | `pip install google-adk` | `adk` | https://google.github.io/adk-docs/get-started/installation/ |
| Langflow | `agent-framework` | `uv pip install langflow` | `langflow` | https://docs.langflow.org/get-started-installation |
| LFX | `agent-framework` | `uv pip install lfx` | `lfx` | https://www.langflow.org/blog/langflow-1-11 |
| Mastra CLI | `agent-framework` | `npm install mastra@latest -g` | `mastra` | https://mastra.ai/blog/upgraded-mastra-cli |
| OpenClaw | `agent-framework` | `npm install -g openclaw@latest` | `openclaw` | https://docs.openclaw.ai/ |
| smolagents CLI | `agent-framework` | `pip install smolagents` | `smolagent` | https://github.com/huggingface/smolagents |
| Agent CLI | `agent-harness` | `uv tool install agent-cli -p 3.13` | `agent-cli` | https://pypi.org/project/agent-cli/ |
| GPTScript | `agent-harness` | `curl https://get.gptscript.ai/install.sh \| sh` | `gptscript` | https://docs.gptscript.ai/ |
| Magentic-One CLI | `agent-harness` | `pip install -U magentic-one-cli` | `m1` | https://microsoft.github.io/autogen/0.4.9/index.html |
| Browser Use CLI | `agent-infrastructure` | `curl -fsSL https://browser-use.com/cli/install.sh \| bash` | `browser-use` | https://docs.browser-use.com/open-source/browser-use-cli |
| Composio Universal CLI | `agent-infrastructure` | `curl -fsSL https://composio.dev/install \| bash` | `composio` | https://composio.dev/cli |
| Open WebUI Computer | `agent-infrastructure` | `pip install cptr` | `cptr` | https://docs.openwebui.com/ecosystem/computer/install/ |
| OpenSpec | `agent-infrastructure` | `npm install -g @fission-ai/openspec@latest` | `openspec` | https://github.com/Fission-AI/OpenSpec |
| Skills CLI | `agent-infrastructure` | `npx skills@latest` | `npx` | https://www.skills.sh/docs/cli |
| BMAD Method | `agent-orchestrator` | `npx bmad-method install` | `npx` | https://github.com/bmad-code-org/BMAD-METHOD |
| Open WebUI | `agent-ui` | `pip install open-webui` | `open-webui` | https://docs.openwebui.com/getting-started/quick-start/ |
| Mastra Code | `coding-agent` | `npm install -g mastracode` | `mastracode` | https://code.mastra.ai/ |
| DeepEval | `eval-harness` | `pip install -U deepeval` | `deepeval` | https://deepeval.com/docs/getting-started |
| GuideLLM | `eval-harness` | `pip install 'guidellm[recommended]'` | `guidellm` | https://github.com/vllm-project/guidellm |
| Inspect AI | `eval-harness` | `pip install inspect-ai` | `inspect` | https://inspect.aisi.org.uk/ |
| Lighteval | `eval-harness` | `pip install lighteval` | `lighteval` | https://huggingface.co/docs/lighteval/en/installation |
| LM Evaluation Harness | `eval-harness` | `pip install "lm_eval[api]"` | `lm-eval` | https://github.com/EleutherAI/lm-evaluation-harness |
| OpenAI Evals | `eval-harness` | `pip install evals` | `oaieval` | https://github.com/openai/evals |
| Promptfoo | `eval-harness` | `npm install -g promptfoo` | `promptfoo` | https://www.promptfoo.dev/docs/installation/ |
| Ragas | `eval-harness` | `pip install ragas` | `ragas` | https://docs.ragas.io/en/stable/references/cli/ |
| Bifrost Gateway | `gateway` | `npx @maximhq/bifrost` | `npx` | https://github.com/maximhq/bifrost |
| OGX (formerly Llama Stack) | `gateway` | `curl -LsSf https://github.com/ogx-ai/ogx/raw/main/scripts/install.sh \| bash` | `ogx` | https://github.com/ogx-ai/ogx |
| Portkey AI Gateway | `gateway` | `npx @portkey-ai/gateway` | `npx` | https://github.com/Portkey-AI/gateway |
| SGLang Model Gateway | `gateway` | `pip install sglang-router` | `smg` | https://docs.sglang.ai/advanced_features/model_gateway.html |
| ShellGPT | `general-ai-cli` | `pip install shell-gpt` | `sgpt` | https://github.com/TheR1D/shell_gpt |
| Aphrodite Engine | `inference` | `pip install -U aphrodite-engine` | `aphrodite` | https://github.com/PygmalionAI/aphrodite-engine |
| BentoML | `inference` | `pip install bentoml` | `bentoml` | https://docs.bentoml.com/en/latest/ |
| LMDeploy | `inference` | `pip install lmdeploy` | `lmdeploy` | https://lmdeploy.readthedocs.io/en/latest/get_started/installation.html |
| mistral.rs | `inference` | `curl --proto '=https' --tlsv1.2 -sSf https://raw.githubusercontent.com/EricLBuehler/mistral.rs/master/install.sh \| sh` | `mistralrs` | https://github.com/EricLBuehler/mistral.rs |
| MLX-LM | `inference` | `pip install mlx-lm` | `mlx_lm.generate` | https://github.com/ml-explore/mlx-lm |
| MLX-VLM | `inference` | `pip install -U mlx-vlm` | `mlx_vlm.generate` | https://github.com/Blaizzy/mlx-vlm |
| OpenLLM | `inference` | `pip install openllm` | `openllm` | https://github.com/bentoml/OpenLLM |
| RamaLama | `inference` | `curl -fsSL https://ramalama.ai/install.sh \| bash` | `ramalama` | https://ramalama.ai/ |
| Ray Serve LLM | `inference` | `pip install "ray[serve,llm]"` | `serve` | https://docs.ray.io/en/latest/serve/llm/quick-start.html |
| SGLang | `inference` | `pip install sglang` | `sglang` | https://docs.sglang.ai/get_started/install.html |
| TensorRT-LLM | `inference` | `pip3 install tensorrt_llm -U --extra-index-url https://pypi.nvidia.com` | `trtllm-serve` | https://nvidia.github.io/TensorRT-LLM/installation/linux.html |
| vllm-mlx | `inference` | `pip install vllm-mlx` | `vllm-mlx` | https://github.com/waybarrios/vllm-mlx |
| Xinference | `inference` | `pip install "xinference[all]"` | `xinference-local` | https://inference.readthedocs.io/en/latest/getting_started/installation.html |
| FastMCP | `mcp-tooling` | `pip install fastmcp` | `fastmcp` | https://gofastmcp.com/getting-started/installation |
| MCP Inspector | `mcp-tooling` | `npx @modelcontextprotocol/inspector` | `npx` | https://github.com/modelcontextprotocol/inspector |
| mcp-proxy | `mcp-tooling` | `npm install -g mcp-proxy` | `mcp-proxy` | https://www.npmjs.com/package/mcp-proxy |
| mcp-remote | `mcp-tooling` | `npm install -g mcp-remote` | `mcp-remote` | https://github.com/geelen/mcp-remote |
| MCPTools | `mcp-tooling` | `brew install mcptools` | `mcptools` | https://formulae.brew.sh/formula/mcptools |
| Smithery CLI | `mcp-tooling` | `npm install -g @smithery/cli@latest` | `smithery` | https://www.npmjs.com/package/@smithery/cli |
| Supergateway | `mcp-tooling` | `npm install -g supergateway` | `supergateway` | https://github.com/supercorp-ai/supergateway |
| LLaMA Factory | `model-tooling` | `pip install llamafactory` | `llamafactory-cli` | https://pypi.org/project/llamafactory/ |
| Arize Phoenix | `observability` | `pip install arize-phoenix` | `phoenix` | https://arize.com/docs/phoenix |
| CodeBuddy Code | `provider-agent` | `curl -fsSL https://www.codebuddy.cn/cli/install.sh \| bash` | `codebuddy` | https://www.codebuddy.cn/docs/cli/installation |
| CoStrict CLI | `provider-agent` | `curl -fsSL https://costrict.ai/install.sh \| bash` | `cs` | https://docs.costrict.ai/en/cli/guide/installation |
| iFlow CLI | `provider-agent` | `npm install -g @iflow-ai/iflow-cli@latest` | `iflow` | https://github.com/iflow-ai/iflow-cli |
| Jules Tools | `provider-agent` | `npm install -g @google/jules` | `jules` | https://developers.google.com/jules |
| Qoder CLI | `provider-agent` | `curl -fsSL https://qoder.com/install \| bash` | `qodercli` | https://qoder.com/cli |
| agent.ai CLI | `provider-cli` | `curl -fsSL https://agent.ai/cli/install.sh \| sh` | `agentai` | https://pypi.org/project/agentai-cli/ |
| Portkey CLI | `provider-cli` | `npm install -g portkey` | `portkey` | https://portkey.ai/docs/guides/coding-agents/agent-cli |
| Anyscale CLI | `provider-infrastructure` | `pip install -U anyscale` | `anyscale` | https://docs.anyscale.com/reference/cli/ |
| Cerebrium CLI | `provider-infrastructure` | `pip install cerebrium --upgrade` | `cerebrium` | https://docs.cerebrium.ai/getting-started/installation |
| Lepton AI CLI | `provider-infrastructure` | `pip install -U leptonai` | `lep` | https://www.lepton.ai/docs/guides/cli |
| Modal CLI | `provider-infrastructure` | `pip install modal` | `modal` | https://modal.com/docs/guide |
| RunPodctl | `provider-infrastructure` | `wget -qO- cli.runpod.net \| sudo bash` | `runpodctl` | https://docs.runpod.io/runpodctl/install-runpodctl |
| SkyPilot | `provider-infrastructure` | `uv tool install --with pip skypilot` | `sky` | https://docs.skypilot.co/en/latest/getting-started/installation.html |
| Truss | `provider-infrastructure` | `uv tool install truss` | `truss` | https://docs.baseten.co/development/model/truss |
| garak | `security-eval` | `python -m pip install -U garak` | `garak` | https://github.com/NVIDIA/garak |
| Antigravity CLI | `provider-agent` | `curl -fsSL https://antigravity.google/cli/install.sh \| bash` | `agy` | https://github.com/google-antigravity/antigravity-cli |

## Exhaustive expansion pass

This pass added **131 unique entries**, expanding the catalog from **159 to 290** tools. Candidates were de-duplicated and pruned when the installer was deprecated, ambiguous, or had a current safety concern. Capability flags remain `null` when they were not verified.

### Additions by category

| Category | New entries |
|---|---:|
| `coding-agent` | 30 |
| `agent-orchestrator` | 17 |
| `agent-infrastructure` | 16 |
| `agent-harness` | 13 |
| `mcp-tooling` | 12 |
| `observability` | 12 |
| `provider-infrastructure` | 9 |
| `provider-agent` | 5 |
| `agent-ui` | 4 |
| `gateway` | 4 |
| `agent-framework` | 3 |
| `model-tooling` | 3 |
| `eval-harness` | 1 |
| `inference` | 1 |
| `provider-cli` | 1 |

### Representative additions

| Tool | Category | One-line install | Binary |
|---|---|---|---|
| Deep Agents Code | `coding-agent` | `curl -LsSf https://langch.in/dcode \| bash` | `dcode` |
| Roo Code CLI | `coding-agent` | `curl -fsSL https://raw.githubusercontent.com/RooCodeInc/Roo-Code/main/apps/cli/install.sh \| sh` | `roo` |
| pi_agent_rust | `agent-harness` | `curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/pi_agent_rust/main/install.sh?$(date +%s)" \| bash` | `pi` |
| Ruflo | `agent-orchestrator` | `curl -fsSL https://cdn.jsdelivr.net/gh/ruvnet/ruflo@main/scripts/install.sh \| bash` | `ruflo` |
| Nanocoder | `coding-agent` | `npm install -g @nanocollective/nanocoder` | `nanocoder` |
| BLACKBOX CLI | `provider-agent` | `curl -fsSL https://blackbox.ai/install.sh \| bash` | `blackbox` |
| OpenClaude | `coding-agent` | `npm install -g @gitlawb/openclaude` | `openclaude` |
| Letta Code | `coding-agent` | `npm install -g @letta-ai/letta-code` | `letta` |
| Grok Build | `provider-agent` | `curl -fsSL https://x.ai/cli/install.sh \| bash` | `grok` |
| Kode CLI | `coding-agent` | `npm install -g @shareai-lab/kode` | `kode` |
| Dexto | `agent-harness` | `npm install -g dexto` | `dexto` |
| Every Code | `coding-agent` | `npm install -g @just-every/code` | `coder` |
| jcode | `coding-agent` | `curl -fsSL https://jcode.sh/install \| bash` | `jcode` |
| MiMo Code | `provider-agent` | `npm install -g @mimo-ai/cli` | `mimo` |
| agentty | `coding-agent` | `curl -fsSL https://agentty.org/install.sh \| sh` | `agentty` |
| Nori CLI | `coding-agent` | `npm install -g nori-ai-cli` | `nori` |
| DvalinCode | `coding-agent` | `curl -fsSL https://raw.githubusercontent.com/arthurpanhku/dvalincode/main/scripts/install.sh \| bash` | `dvalincode` |
| Darce CLI | `coding-agent` | `npm install -g darce-cli` | `darce` |
| Agent of Empires | `agent-orchestrator` | `curl -fsSL https://raw.githubusercontent.com/agent-of-empires/agent-of-empires/main/scripts/install.sh \| bash` | `aoe` |
| CLI Agent Orchestrator | `agent-orchestrator` | `uv tool install git+https://github.com/awslabs/cli-agent-orchestrator.git@main --upgrade` | `cao` |
| cmux | `agent-ui` | `brew tap manaflow-ai/cmux && brew install --cask cmux` | `cmux` |
| Superset CLI | `agent-orchestrator` | `curl -fsSL https://superset.sh/cli/install.sh \| sh` | `superset` |
| amux | `agent-orchestrator` | `brew install mixpeek/amux/amux` | `amux` |
| dmux | `agent-orchestrator` | `npm install -g dmux` | `dmux` |
| AgentManager | `agent-infrastructure` | `brew install kevinelliott/tap/agentmanager` | `agentmgr` |
| ByteRover CLI | `agent-infrastructure` | `curl -fsSL https://byterover.dev/install.sh \| sh` | `brv` |
| CocoIndex Code | `agent-infrastructure` | `pipx install 'cocoindex-code[full]'` | `ccc` |
| Serena | `agent-infrastructure` | `uv tool install -p 3.13 serena-agent` | `serena` |
| agent-browser | `agent-infrastructure` | `npm install -g agent-browser` | `agent-browser` |
| agent-install | `agent-infrastructure` | `npx agent-install@latest --help` | `agent-install` |
| mcp2cli | `mcp-tooling` | `curl -fsSL https://mcp2cli.dev/install.sh \| sh` | `mcp2cli` |
| mcpo | `mcp-tooling` | `pip install mcpo` | `mcpo` |
| ToolHive | `mcp-tooling` | `brew tap stacklok/tap && brew install thv` | `thv` |
| MCPJam CLI | `mcp-tooling` | `npm install -g @mcpjam/cli` | `mcpjam` |
| Braintrust CLI | `observability` | `curl -fsSL https://bt.dev/cli/install.sh \| bash` | `bt` |
| Langfuse CLI | `observability` | `npm install -g langfuse-cli` | `langfuse` |
| Arize AX CLI | `observability` | `pip install arize-ax-cli` | `ax` |
| Daytona CLI | `provider-infrastructure` | `brew install daytonaio/cli/daytona` | `daytona` |
| E2B CLI | `provider-infrastructure` | `npm install -g @e2b/cli` | `e2b` |
| Nebius CLI | `provider-infrastructure` | `curl -sSL https://storage.eu-north1.nebius.cloud/cli/install.sh \| bash` | `nebius` |
| Fireworks firectl | `provider-infrastructure` | `brew tap fw-ai/firectl && brew install firectl` | `firectl` |
| dstack CLI | `provider-infrastructure` | `uv tool install dstack -U` | `dstack` |
| Replicate Cog | `provider-infrastructure` | `sh <(curl -fsSL https://cog.run/install.sh)` | `cog` |
| Snowflake Cortex Code CLI | `provider-agent` | `curl -LsS https://ai.snowflake.com/static/cc-scripts/install.sh \| sh` | `cortex` |
| ElevenLabs CLI | `provider-cli` | `npm install -g @elevenlabs/cli` | `elevenlabs` |
| AgentGateway | `gateway` | `curl -sL https://agentgateway.dev/install \| bash` | `agentgateway` |
| nanobot | `agent-harness` | `curl -fsSL https://raw.githubusercontent.com/HKUDS/nanobot/main/scripts/install.sh \| sh` | `nanobot` |
| ZeroClaw | `agent-harness` | `curl -fsSL https://raw.githubusercontent.com/zeroclaw-labs/zeroclaw/master/install.sh \| bash` | `zeroclaw` |
| IronClaw | `agent-harness` | `curl --proto '=https' --tlsv1.2 -LsSf https://github.com/nearai/ironclaw/releases/latest/download/ironclaw-installer.sh \| sh` | `ironclaw` |
| NullClaw | `agent-harness` | `brew install nullclaw` | `nullclaw` |
| Moltis | `agent-harness` | `curl -fsSL https://www.moltis.org/install.sh \| sh` | `moltis` |
| Octocode | `agent-infrastructure` | `curl -fsSL https://raw.githubusercontent.com/Muvon/octocode/master/install.sh \| sh` | `octocode` |

The complete 290-entry list, including source URLs and capability metadata, lives in **`catalog.json`** and is the canonical source of truth.

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

## Continued exhaustive expansion — August 2026

This continuation added **48** additional de-duplicated one-line-installable tools, bringing the catalog to **338 entries**. Commands were checked against current upstream project documentation or repositories; uncertain capability flags remain `null`.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| Waza | `eval-harness` | `curl -fsSL https://raw.githubusercontent.com/microsoft/waza/main/install.sh \| bash` | `waza` | https://github.com/microsoft/waza |
| ClawHub CLI | `agent-infrastructure` | `npm install -g clawhub` | `clawhub` | https://github.com/openclaw/clawhub |
| Clarity Agent | `agent-framework` | `curl -fsSL https://raw.githubusercontent.com/microsoft/clarity-agent/main/scripts/install.sh \| bash` | `clarity` | https://github.com/microsoft/clarity-agent |
| Eidos Memory | `agent-infrastructure` | `npm install -g eidos-memory` | `eidos` | https://www.npmjs.com/package/eidos-memory |
| San | `coding-agent` | `curl -fsSL https://raw.githubusercontent.com/genai-io/san/main/install.sh \| bash` | `san` | https://github.com/genai-io/san |
| picocode | `coding-agent` | `curl -sSfL https://raw.githubusercontent.com/jondot/picocode/main/install.sh \| sh` | `picocode` | https://github.com/jondot/picocode |
| Zap Coding Agent | `coding-agent` | `curl -fsSL https://raw.githubusercontent.com/zap-coding-agent/zap-coding-agent/main/install.sh \| sh` | `zap` | https://github.com/zap-coding-agent/zap-coding-agent |
| showagent | `agent-infrastructure` | `go install github.com/aytzey/showagent/cmd/showagent@latest` | `showagent` | https://github.com/aytzey/showagent |
| GitClaw | `agent-framework` | `npm install -g gitclaw` | `gitclaw` | https://github.com/open-gitagent/gitagent |
| AgentBox | `agent-orchestrator` | `npm install -g @madarco/agentbox` | `agentbox` | https://github.com/madarco/agentbox |
| Crusoe CLI | `provider-infrastructure` | `brew install crusoecloud/cli/crusoe` | `crusoe` | https://docs.crusoecloud.com/cli/ |
| HELM | `eval-harness` | `pip install crfm-helm` | `helm-run` | https://github.com/stanford-crfm/helm |
| NeMo Guardrails | `security-eval` | `pip install nemoguardrails` | `nemoguardrails` | https://github.com/NVIDIA/NeMo-Guardrails |
| Weights & Biases CLI | `observability` | `pip install wandb` | `wandb` | https://docs.wandb.ai/ref/cli/ |
| Guardrails AI | `security-eval` | `pip install guardrails-ai` | `guardrails` | https://github.com/guardrails-ai/guardrails |
| OpenCompass | `eval-harness` | `pip install -U opencompass` | `opencompass` | https://github.com/open-compass/opencompass |
| Agno CLI | `general-ai-cli` | `pip install agno-cli` | `agno` | https://pypi.org/project/agno-cli/ |
| MCP-Get | `mcp-tooling` | `npm install -g @michaellatman/mcp-get` | `mcp-get` | https://mcp-get.com/ |
| KTransformers / SGLang-KT CLI | `inference` | `pip install kt-kernel sglang-kt` | `kt` | https://ktransformers.readthedocs.io/ |
| Ferro AI Gateway | `gateway` | `go install github.com/ferro-labs/ai-gateway/cmd/ferrogw@latest` | `ferrogw` | https://github.com/ferro-labs/ai-gateway |
| OpenLore | `agent-infrastructure` | `npm install -g openlore` | `openlore` | https://github.com/clay-good/OpenLore |
| CodeMie Code | `provider-agent` | `npm install -g @codemieai/code` | `codemie` | https://github.com/codemie-ai/codemie-code |
| AnyCoding | `agent-ui` | `npm install -g @luzedong/anycoding` | `anycoding` | https://github.com/luzedong/anycoding |
| Coding Agent Account Manager | `agent-infrastructure` | `curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/coding_agent_account_manager/main/install.sh?$(date +%s)" \| bash` | `caam` | https://github.com/Dicklesworthstone/coding_agent_account_manager |
| llm-wiki | `agent-infrastructure` | `curl -fsSL https://raw.githubusercontent.com/geronimo-iia/llm-wiki/main/install.sh \| bash` | `llm-wiki` | https://github.com/geronimo-iia/llm-wiki |
| WebdriverIO MCP | `mcp-tooling` | `npm install -g @wdio/mcp` | `wdio-mcp` | https://github.com/webdriverio/mcp |
| RayClaw | `agent-harness` | `curl -fsSL https://rayclaw.ai/install.sh \| bash` | `rayclaw` | https://github.com/rayclaw/rayclaw |
| ZeptoClaw | `agent-harness` | `curl -fsSL https://raw.githubusercontent.com/qhkm/zeptoclaw/main/install.sh \| sh` | `zeptoclaw` | https://github.com/qhkm/zeptoclaw |
| QwenPaw | `agent-framework` | `curl -fsSL https://qwenpaw.agentscope.io/install.sh \| bash` | `qwenpaw` | https://github.com/agentscope-ai/QwenPaw |
| HiClaw | `agent-orchestrator` | `bash <(curl -fsSL https://raw.githubusercontent.com/agentscope-ai/HiClaw/main/install/hiclaw-install.sh)` | `hiclaw` | https://github.com/agentscope-ai/HiClaw |
| OneCLI | `agent-infrastructure` | `curl -fsSL https://onecli.sh/install \| sh` | `onecli` | https://github.com/onecli/onecli |
| Caido MCP Server | `mcp-tooling` | `curl -fsSL https://raw.githubusercontent.com/c0tton-fluff/caido-mcp-server/main/install.sh \| bash` | `caido-mcp-server` | https://github.com/c0tton-fluff/caido-mcp-server |
| c7search | `mcp-tooling` | `go install github.com/kevin-burns/c7search@latest` | `c7search` | https://github.com/kevin-burns/c7search |
| MCP Reference: Everything | `mcp-tooling` | `npx -y @modelcontextprotocol/server-everything` | `npx` | https://github.com/modelcontextprotocol/servers/tree/main/src/everything |
| MCP Reference: Fetch | `mcp-tooling` | `uvx mcp-server-fetch` | `uvx` | https://github.com/modelcontextprotocol/servers/tree/main/src/fetch |
| MCP Reference: Filesystem | `mcp-tooling` | `npx -y @modelcontextprotocol/server-filesystem` | `npx` | https://github.com/modelcontextprotocol/servers/tree/main/src/filesystem |
| MCP Reference: Git | `mcp-tooling` | `uvx mcp-server-git` | `uvx` | https://github.com/modelcontextprotocol/servers/tree/main/src/git |
| MCP Reference: Memory | `mcp-tooling` | `npx -y @modelcontextprotocol/server-memory` | `npx` | https://github.com/modelcontextprotocol/servers/tree/main/src/memory |
| MCP Reference: Sequential Thinking | `mcp-tooling` | `npx -y @modelcontextprotocol/server-sequential-thinking` | `npx` | https://github.com/modelcontextprotocol/servers/tree/main/src/sequentialthinking |
| MCP Reference: Time | `mcp-tooling` | `uvx mcp-server-time` | `uvx` | https://github.com/modelcontextprotocol/servers/tree/main/src/time |
| Playwright MCP | `mcp-tooling` | `npm install -g @playwright/mcp` | `playwright-mcp` | https://github.com/microsoft/playwright-mcp |
| Google MCP Server | `mcp-tooling` | `brew install ngs/tap/google-mcp-server` | `google-mcp-server` | https://github.com/ngs/google-mcp-server |
| GitHub MCP Server | `mcp-tooling` | `docker pull ghcr.io/github/github-mcp-server` | `github-mcp-server` | https://github.com/github/github-mcp-server |
| Atlassian Jira MCP Server | `mcp-tooling` | `npm install -g @aashari/mcp-server-atlassian-jira` | `mcp-atlassian-jira` | https://github.com/aashari/mcp-server-atlassian-jira |
| Atlassian Confluence MCP Server | `mcp-tooling` | `npm install -g @aashari/mcp-server-atlassian-confluence` | `mcp-atlassian-confluence` | https://github.com/aashari/mcp-server-atlassian-confluence |
| Harbor | `agent-infrastructure` | `curl -fsSL https://raw.githubusercontent.com/av/harbor/refs/heads/main/install.sh \| bash` | `harbor` | https://github.com/av/harbor |
| OpenBench | `eval-harness` | `pip install "git+https://github.com/minghinmatthewlam/openbench.git"` | `obench` | https://github.com/minghinmatthewlam/openbench |
| Smelt | `coding-agent` | `cargo install smelt` | `smelt` | https://github.com/leonardcser/smelt |

The machine-readable `catalog.json` remains the canonical source of truth for all entries and capability metadata.

## Second continued expansion — August 2026

This pass added **28** more de-duplicated entries, bringing the catalog to **366 tools**. Each added record has a current upstream one-line installer or package-manager command; uncertain capability flags remain `null`.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| Microsoft Conductor | `agent-orchestrator` | `curl -sSfL https://aka.ms/conductor/install.sh \| sh` | `conductor` | https://github.com/microsoft/conductor |
| Google LiteRT-LM CLI | `inference` | `uv tool install litert-lm` | `litert-lm` | https://developers.google.com/edge/litert-lm/cli/installation |
| Google LiteRT CLI | `model-tooling` | `pip install -q litert-cli-nightly` | `litert` | https://developers.google.com/edge/litert/cli |
| Go Micro Agent Harness | `agent-framework` | `curl -fsSL https://go-micro.dev/install.sh \| sh` | `micro` | https://github.com/micro/go-micro |
| GetMCP CLI | `mcp-tooling` | `npm install -g @getmcp/cli` | `getmcp` | https://www.npmjs.com/package/@getmcp/cli |
| gopls MCP | `mcp-tooling` | `go install golang.org/x/tools/gopls@latest` | `gopls` | https://go.dev/gopls/features/mcp |
| Google SecOps MCP | `mcp-tooling` | `uv tool install google-secops-mcp` | `secops_mcp` | https://github.com/google/mcp-security |
| Google Threat Intelligence MCP | `mcp-tooling` | `uv tool install gti-mcp` | `gti_mcp` | https://pypi.org/project/gti-mcp/ |
| Google Security Command Center MCP | `mcp-tooling` | `uv tool install scc-mcp` | `scc_mcp` | https://pypi.org/project/scc-mcp/ |
| Google SecOps SOAR MCP | `mcp-tooling` | `uv tool install secops-soar-mcp` | `secops_soar_mcp` | https://pypi.org/project/secops-soar-mcp/ |
| NotebookLM MCP CLI | `mcp-tooling` | `uv tool install notebooklm-mcp-cli` | `nlm` | https://pypi.org/project/notebooklm-mcp-cli/ |
| ClifCode | `coding-agent` | `cargo install --git https://github.com/DLhugly/Clif-Code.git --path clif-code-tui` | `clifcode` | https://github.com/DLhugly/Clif-Code |
| claimcheck | `agent-infrastructure` | `cargo install claimcheck` | `claimcheck` | https://github.com/ojuschugh1/claimcheck |
| PleaseAI Chrome DevTools CLI | `agent-infrastructure` | `curl -fsSL https://raw.githubusercontent.com/pleaseai/chrome-devtools-cli/main/install.sh \| bash` | `chrome-devtools` | https://github.com/pleaseai/chrome-devtools-cli |
| Aeroxy Chrome DevTools CLI | `agent-infrastructure` | `cargo install chrome-devtools-cli` | `chrome-devtools` | https://github.com/aeroxy/chrome-devtools-cli |
| Agent Memory MCP | `agent-infrastructure` | `go install github.com/ipiton/agent-memory-mcp/cmd/agent-memory-mcp@latest` | `agent-memory-mcp` | https://github.com/ipiton/agent-memory-mcp |
| Agent Context Lens | `agent-infrastructure` | `python -m pip install "git+https://github.com/ciceroyang/agent-context-lens.git"` | `agent-context-lens` | https://github.com/ciceroyang/agent-context-lens |
| A2A CLI | `agent-infrastructure` | `pip install a2a-cli` | `a2a` | https://pypi.org/project/a2a-cli/ |
| Apify mcpc | `mcp-tooling` | `npm install -g @apify/mcpc` | `mcpc` | https://www.npmjs.com/package/@apify/mcpc |
| mcps Universal MCP Manager | `mcp-tooling` | `npm install -g @itzfaisal/mcp-cli` | `mcps` | https://www.npmjs.com/package/@itzfaisal/mcp-cli |
| Microsoft Agent Package Manager | `agent-infrastructure` | `curl -sSL https://aka.ms/apm-unix \| sh` | `apm` | https://github.com/microsoft/apm |
| skillpm | `agent-infrastructure` | `npm install -g skillpm` | `skillpm` | https://skillpm.dev/ |
| gflow-cli | `provider-cli` | `uv tool install gflow-cli` | `gflow` | https://pypi.org/project/gflow-cli/ |
| MCP Language Server | `mcp-tooling` | `go install github.com/isaacphi/mcp-language-server@latest` | `mcp-language-server` | https://github.com/isaacphi/mcp-language-server |
| LSP MCP | `mcp-tooling` | `npm install -g @theupsider/lsp-mcp` | `lsp-mcp` | https://www.npmjs.com/package/@theupsider/lsp-mcp |
| MCPorter | `mcp-tooling` | `npm install -g mcporter` | `mcporter` | https://github.com/openclaw/mcporter |
| projectmem | `agent-infrastructure` | `pip install projectmem` | `projectmem` | https://pypi.org/project/projectmem/ |
| DeepXiv SDK CLI | `agent-infrastructure` | `pip install "deepxiv-sdk[all]"` | `deepxiv` | https://pypi.org/project/deepxiv-sdk/ |

The machine-readable `catalog.json` remains the canonical source of truth.

## Third continued expansion — August 2026

This pass added **17** more unique one-line-installable tools, bringing the catalog to **383 entries**.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| CASS (Coding Agent Session Search) | `observability` | `curl -fsSL "https://raw.githubusercontent.com/Dicklesworthstone/coding_agent_session_search/main/install.sh?$(date +%s)" \| bash -s -- --easy-mode --verify` | `cass` | https://github.com/Dicklesworthstone/coding_agent_session_search |
| NClaw | `agent-harness` | `brew install --cask nickalie/apps/nclaw` | `nclaw` | https://github.com/nickalie/nclaw |
| Leon CLI | `general-ai-cli` | `npm install --global @leon-ai/cli` | `leon` | https://github.com/leon-ai/leon-cli |
| Agentic Coding Flywheel Setup | `agent-infrastructure` | `curl -fsSL https://agent-flywheel.com/install \| bash` | `acfs` | https://github.com/Dicklesworthstone/agentic_coding_flywheel_setup |
| Crystal | `agent-ui` | `brew install --cask stravu-crystal` | `Crystal` | https://github.com/stravu/crystal |
| Agent Sessions | `observability` | `brew tap jazzyalex/agent-sessions && brew install --cask agent-sessions` | `Agent Sessions` | https://github.com/jazzyalex/agent-sessions |
| AI Agent Session Center | `agent-ui` | `npx ai-agent-session-center` | `npx` | https://github.com/coding-by-feng/ai-agent-session-center |
| MCPJungle | `gateway` | `brew install mcpjungle/mcpjungle/mcpjungle` | `mcpjungle` | https://github.com/mcpjungle/MCPJungle |
| AgentMemory | `agent-infrastructure` | `npm install -g @agentmemory/agentmemory` | `agentmemory` | https://github.com/rohitg00/agentmemory |
| OpenModel | `inference` | `npm install --global @wundercorp/openmodel` | `om` | https://www.npmjs.com/package/@wundercorp/openmodel |
| mcp-scan | `security-eval` | `npm install -g mcp-scan` | `mcp-scan` | https://github.com/rodolfboctor/mcp-scan |
| MCP Scanner | `security-eval` | `brew install oabraham1/tap/mcp-scanner` | `mcp-scanner` | https://github.com/oabraham1/mcp-scanner |
| Agentlint | `security-eval` | `pip install leporis-agentlint` | `agentlint` | https://github.com/Leporis14/agentlint |
| MCP Safety Warden | `security-eval` | `pip install mcpsafetywarden` | `mcpsafetywarden` | https://github.com/gautamvarmadatla/mcpsafetywarden |
| Agent Audit | `security-eval` | `pip install agent-audit` | `agent-audit` | https://github.com/HeadyZhang/agent-audit |
| Snyk Agent Scan | `security-eval` | `uvx snyk-agent-scan@latest` | `snyk-agent-scan` | https://github.com/snyk/agent-scan |
| IronCurtain | `agent-harness` | `npm install -g @provos/ironcurtain` | `ironcurtain` | https://github.com/provos/ironcurtain |

The machine-readable `catalog.json` remains the canonical source of truth.

## Fourth continued expansion — August 2026

This pass added **17** more de-duplicated one-line-installable tools, taking the catalog past the 400-entry mark to **400 tools**. Current upstream installer/package-manager commands were preferred; uncertain capability flags remain `null`.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| 9router | `gateway` | `npm install -g 9router` | `9router` | https://github.com/decolua/9router |
| Gnoma | `coding-agent` | `go install somegit.dev/Owlibou/gnoma/cmd/gnoma@latest` | `gnoma` | https://github.com/VikingOwl91/gnoma |
| Agent Ready | `agent-infrastructure` | `npm install -g @eagerminds/agent-ready` | `agent-ready` | https://github.com/prajapatimehul/agent-ready |
| Jean Server | `agent-ui` | `curl -fsSL https://raw.githubusercontent.com/coollabsio/jean/main/scripts/install-jean-server.sh \| sudo bash -s -- -y` | `jean-server` | https://github.com/coollabsio/jean |
| Hummcode | `coding-agent` | `pip install hummcode` | `hummcode` | https://github.com/0xchamin/hummcode |
| adport | `mcp-tooling` | `npm install -g adport` | `adport` | https://github.com/ynnickw/adport |
| k8stalk | `agent-harness` | `brew install naman833/k8stalk/k8stalk` | `k8stalk` | https://github.com/naman833/k8stalk |
| Agent Orchestrator Runtime | `agent-orchestrator` | `npm install -g @bpinhosilva/agent-orchestrator` | `agent-orchestrator` | https://github.com/bpinhosilva/agent-orchestrator |
| Agency Orchestrator | `agent-orchestrator` | `npm install -g agency-orchestrator` | `ao` | https://github.com/jnMetaCode/agency-orchestrator |
| FitLab Agent Infra | `agent-infrastructure` | `npm install -g @fitlab-ai/agent-infra` | `ai` | https://github.com/fitlab-ai/agent-infra |
| AgentBrain MCP Server | `mcp-tooling` | `npx -y @agentbrain/mcp-server` | `npx` | https://github.com/benmalcom/agentbrain |
| Aurra | `agent-infrastructure` | `pip install aurra` | `aurra` | https://pypi.org/project/aurra/ |
| agent-memory | `agent-infrastructure` | `npm install -g myagentmemory` | `agent-memory` | https://github.com/jayzeng/agentmemory |
| vLLM-Omni | `inference` | `uv pip install vllm-omni` | `vllm` | https://github.com/vllm-project/vllm-omni |
| Gograph | `agent-infrastructure` | `go install github.com/ozgurcd/gograph@latest` | `gograph` | https://github.com/ozgurcd/gograph |
| Coder Mux | `agent-orchestrator` | `npm install -g mux@next` | `mux` | https://github.com/coder/mux |
| Keen Code | `coding-agent` | `curl -fsSL https://raw.githubusercontent.com/mochow13/keen-code/main/scripts/install.sh \| bash` | `keen` | https://github.com/mochow13/keen-code |

The machine-readable `catalog.json` remains the canonical source of truth.

## Fifth continued expansion — August 2026

This pass added **9** more de-duplicated one-line-installable tools, bringing the catalog to **409 entries**. This pass emphasizes memory/context infrastructure, gateways, browser tooling, and official/reference MCP servers.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| Prism Coder | `agent-infrastructure` | `npm install -g prism-mcp-server` | `prism` | https://github.com/dcostenco/prism-coder |
| Neo4j Agent Memory | `agent-infrastructure` | `pip install 'neo4j-agent-memory[cli,mcp]'` | `neo4j-memory` | https://github.com/neo4j-labs/agent-memory |
| Vault Agent Memory | `agent-infrastructure` | `curl -sSL https://raw.githubusercontent.com/zycaskevin/Vault-Agent-Memory/main/scripts/install.sh \| bash` | `vault` | https://github.com/zycaskevin/Vault-Agent-Memory |
| IWE | `agent-infrastructure` | `brew tap iwe-org/iwe && brew install iwe` | `iwe` | https://github.com/iwe-org/iwe |
| Chrome DevTools MCP | `mcp-tooling` | `npm install -g chrome-devtools-mcp@latest` | `chrome-devtools` | https://github.com/ChromeDevTools/chrome-devtools-mcp |
| Context7 MCP | `mcp-tooling` | `npx -y @upstash/context7-mcp@latest` | `npx` | https://github.com/upstash/context7 |
| Postman MCP Server | `mcp-tooling` | `npx -y @postman/postman-mcp-server@latest` | `npx` | https://github.com/postmanlabs/postman-mcp-server |
| Notion MCP Server | `mcp-tooling` | `npx -y @notionhq/notion-mcp-server` | `npx` | https://github.com/makenotion/notion-mcp-server |
| Sentry MCP Server | `mcp-tooling` | `npx @sentry/mcp-server@latest` | `npx` | https://github.com/getsentry/sentry-mcp |

The machine-readable `catalog.json` remains the canonical source of truth.

## Newly verified CLIs — August 10, 2026

This pass adds **3 newly verified terminal-first AI tools** discovered from current upstream documentation and package registries.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| AgentForge CLI | `agent-framework` | `npm install -g @agentforge/cli` | `agentforge` | https://github.com/TVScoundrel/agentforge |
| Lurus Code CLI | `coding-agent` | `npm install -g @scramble-cloud/lurus-code-cli` | `lurus` | https://code.lurus.ai/en/docs/cli-commands/ |
| AgentProto CLI | `agent-orchestrator` | `npm install -g @agentproto/cli` | `agentproto` | https://agentproto.sh/cli |

The machine-readable `catalog.json` remains the canonical source of truth.

## Verified CLI refresh — August 11, 2026

This pass adds **5 newly verified terminal-first AI tools** and migrates one deprecated installer/package identity. The catalog now contains **417 entries**.

| Tool | Category | One-line install | Binary | Upstream | Change |
|---|---|---|---|---|---|
| Marvin | `coding-agent` | `npm install -g @yeshwanthyk/coding-agent` | `marvin` | https://github.com/Yeshwanthyk/marvin | New terminal-native multi-provider coding agent. |
| prjct-cli | `agent-infrastructure` | `curl -sSL https://raw.githubusercontent.com/prjct-app/cli/main/scripts/install-standalone.sh \| bash` | `prjct` | https://github.com/prjct-app/cli | New agent harness/infrastructure CLI with standalone installer and local daemon. |
| spec-guard CLI | `agent-infrastructure` | `npm install -g @spec-guard/cli` | `specguard` | https://github.com/spec-guard/spec-guard | New governance/spec-driven development CLI for AI coding agents. |
| AgentsMesh Config CLI | `agent-infrastructure` | `curl -fsSL https://github.com/sampleXbro/agentsmesh/releases/latest/download/install.sh \| sh` | `agentsmesh` | https://github.com/sampleXbro/agentsmesh | New cross-agent configuration and shared-memory CLI with standalone installer. |
| FAF CLI | `agent-infrastructure` | `npm install -g faf-cli` | `faf` | https://github.com/Wolfe-Jam/faf-cli | New git-native AI context/configuration CLI. |
| FitLab Agent Infra | `agent-infrastructure` | `npm install -g @fitlab-ai/agent-infra` | `ai` | https://github.com/fitlab-ai/agent-infra | Replaces deprecated `@fitlab-ai/agent-orchestrator` package and old installer. |

The machine-readable `catalog.json` remains the canonical source of truth.

## Verified CLI refresh — August 12, 2026

This pass adds **8 newly verified terminal-first AI tools**, bringing the catalog to **425 entries**.

| Tool | Category | One-line install | Binary | Upstream | Change |
|---|---|---|---|---|---|
| LLM Gateway CLI | `gateway` | `npm install -g @llmgateway/cli` | `llmgateway` | https://docs.llmgateway.io/guides/cli | New official gateway/account/coding-agent launcher CLI. |
| Draht | `coding-agent` | `npm install -g @draht/coding-agent` | `draht` | https://github.com/draht-dev/draht | New terminal coding harness with npm distribution and subscription/API-key auth. |
| Unity AI Gateway Coding CLI (ucode) | `agent-launcher` | `uv tool install git+https://github.com/databricks/ucode` | `ucode` | https://github.com/databricks/ucode | New Databricks launcher for Codex, Claude Code, Gemini CLI, OpenCode, Copilot CLI, Pi, and Cursor. |
| CAAMP | `agent-infrastructure` | `npm install -g @cleocode/caamp` | `caamp` | https://github.com/kryptobaseddev/cleo/tree/main/packages/caamp | New cross-agent package manager for skills, MCP servers, and instruction files. |
| Kimchi | `coding-agent` | `curl -fsSL https://github.com/getkimchi/kimchi/releases/latest/download/install.sh \| bash` | `kimchi` | https://docs.kimchi.dev/docs/kimchi-cli | New multi-model terminal coding harness with one-line release installer. |
| Sudo Code | `coding-agent` | `curl -fsSL https://raw.githubusercontent.com/sudoprivacy/sudocode/main/install.sh \| sh` | `scode` | https://github.com/sudoprivacy/sudocode | New Rust-native terminal coding agent with ACP server and MCP support. |
| zaly | `coding-agent` | `npm install -g @zaly/cli` | `zaly` | https://github.com/folke/zaly | New hackable terminal coding agent published as @zaly/cli. |
| wigolo | `agent-infrastructure` | `npm install -g wigolo` | `wigolo` | https://github.com/KnockOutEZ/wigolo | New local-first web intelligence CLI/MCP server for coding agents. |

The machine-readable `catalog.json` remains the canonical source of truth.

## Newly verified CLIs — August 13, 2026

This pass adds **3 newly verified terminal-first AI tools** and removes the frozen legacy `@aoagents/ao` CLI entry after upstream marked npm distribution as legacy and no longer recommended for new installs.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| Tau | `coding-agent` | `uv tool install tau-ai` | `tau` | https://github.com/huggingface/tau |
| Untether | `agent-infrastructure` | `uv tool install untether` | `untether` | https://github.com/littlebearapps/untether |
| ast-outline | `agent-infrastructure` | `uv tool install ast-outline` | `ast-outline` | https://github.com/ast-outline/ast-outline |

**Removed stale entry:** `Agent Orchestrator (ao)` / `@aoagents/ao` because upstream freezes the npm CLI at 0.10.0 and explicitly recommends the desktop distribution for new setups.

The machine-readable `catalog.json` remains the canonical source of truth.

## Newly verified CLIs — August 14, 2026

This pass adds **4 newly verified terminal-first AI tools** discovered from current official documentation and package registries.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| Indusagi Coding Agent | `coding-agent` | `npm install -g indusagi-coding-agent` | `indus` | https://www.indusagi.com/cli |
| Xyne CLI | `coding-agent` | `npm install -g @xyne/xyne-cli` | `xyne` | https://github.com/xyne/xyne-cli |
| Agent Commander | `agent-orchestrator` | `npm install -g agent-commander` | `start-agent` | https://github.com/link-assistant/agent-commander |
| Cairn | `observability` | `uv tool install cairn-workspace` | `cairn` | https://github.com/Harsh-Daga/Cairn |

The machine-readable `catalog.json` remains the canonical source of truth.

## Newly verified CLIs — August 15, 2026

This pass adds **5** newly verified, de-duplicated terminal-first AI tools, bringing the catalog to **436 entries**.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| UmaDev | `agent-orchestrator` | `npm install -g umadev` | `umadev` | https://github.com/umacloud/umadev |
| Headless CLI | `agent-orchestrator` | `npm install -g @roberttlange/headless` | `headless` | https://github.com/RobertTLange/headless-cli |
| Agent Code | `coding-agent` | `curl -fsSL https://raw.githubusercontent.com/avala-ai/agent-code/main/install.sh \| bash` | `agent` | https://github.com/avala-ai/agent-code |
| Agent Harness (MadeByWild) | `agent-infrastructure` | `npx -y @madebywild/agent-harness-framework` | `harness` | https://github.com/madebywild/agent-harness |
| Agent Harness (ar27111994) | `agent-infrastructure` | `npm install -g @ar27111994/agent-harness` | `agent-harness` | https://github.com/ar27111994/agent-harness |

The machine-readable `catalog.json` remains the canonical source of truth.

## Newly verified CLIs — August 16, 2026

This pass adds **4** newly verified, de-duplicated terminal-first AI tools, bringing the stacked catalog to **440 entries**.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| X-Code CLI | `coding-agent` | `npm install -g @x-code-cli/cli` | `xc` | https://github.com/woai3c/x-code-cli |
| TheGitAI CLI | `coding-agent` | `npm install -g @thegitai/cli` | `ai` | https://www.npmjs.com/package/@thegitai/cli |
| CodeAM CLI | `agent-infrastructure` | `npm install -g codeam-cli` | `codeam` | https://github.com/edgar-durand/codeagent-mobile-clients |
| mcp-coordinator | `agent-infrastructure` | `npm install -g mcp-coordinator` | `mcp-coordinator` | https://github.com/swoofer/mcp-coordinator |

The machine-readable `catalog.json` remains the canonical source of truth.

## Newly verified CLIs — August 17, 2026

This pass adds **3 newly verified terminal-first AI tools** discovered from current upstream repositories and release metadata.

| Tool | Category | One-line install | Binary | Source |
|---|---|---|---|---|
| btch-cli | `coding-agent` | `curl -fsSL https://raw.githubusercontent.com/hostinger-bot/btch-cli/main/install.sh \| bash` | `btch` | https://github.com/hostinger-bot/btch-cli |
| Wrenyard | `agent-orchestrator` | `curl -fsSL https://raw.githubusercontent.com/wrenyard/wrenyard/main/scripts/install.sh \| bash -s -- --update --bin-dir "$HOME/.local/bin"` | `wrenyard` | https://github.com/wrenyard/wrenyard |
| Agent Firewall | `agent-infrastructure` | `go install github.com/SamVale29/agent-firewall/cmd/afw@latest` | `afw` | https://github.com/SamVale29/agent-firewall |

The machine-readable `catalog.json` remains the canonical source of truth.
