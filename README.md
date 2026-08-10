# AI CLI Catalog

A machine-readable catalog of terminal-first **AI coding agents**, **agent harnesses**, **agent orchestrators**, **agent frameworks**, **local inference runtimes**, **gateways**, and supporting CLI infrastructure.

> Last reviewed: 2026-08-09
> Catalog entries: **159**

## Catalog schema v2

`catalog.json` now records installer and capability metadata suitable for launchers, dashboards, routers, audits, and automated discovery. Feature flags are tri-state: `true`, `false`, or `null` when not yet verified.

Key fields: `category`, `installer`, `installer_type`, `binary`, `open_source`, `local_models`, `openai_compatible`, `mcp`, `acp`, `subscription_auth`, `api_key`, `daemon_server`, `last_verified`, and `official_source`.

## Categories

| Category | Entries |
|---|---:|
| `agent-harness` | 29 |
| `provider-agent` | 21 |
| `inference` | 18 |
| `agent-framework` | 14 |
| `agent-infrastructure` | 12 |
| `agent-orchestrator` | 10 |
| `provider-infrastructure` | 9 |
| `eval-harness` | 8 |
| `gateway` | 7 |
| `mcp-tooling` | 7 |
| `coding-agent` | 6 |
| `general-ai-cli` | 6 |
| `provider-cli` | 3 |
| `acp-bridge` | 2 |
| `agent-ui` | 2 |
| `model-tooling` | 2 |
| `agent-launcher` | 1 |
| `observability` | 1 |
| `security-eval` | 1 |

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
