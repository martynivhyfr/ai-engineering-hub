# CLAUDE.md — AI Engineering Hub

This file provides guidance for AI assistants (Claude Code and others) working in this repository.

---

## Repository Overview

**AI Engineering Hub** is an educational collection of ~70 independent AI engineering projects. Each project demonstrates a specific pattern, technology, or integration—from multi-agent systems and RAG pipelines to MCP servers and model comparisons. Projects are primarily Python-based and target practitioners learning to build production AI applications.

- **License:** MIT
- **Primary language:** Python 3.10–3.13
- **Default branch:** `master` / `main`

---

## Repository Structure

```
ai-engineering-hub/
├── README.md                    # Root hub README with project index
├── LICENSE
├── assets/                      # Shared images and GIFs used in README
│   ├── ai-eng-hub.gif
│   └── TRENDING-BADGE.png
├── <project-name>/              # Each directory is a self-contained project
│   ├── README.md                # Project-specific docs
│   ├── app.py                   # Streamlit app entry point (most projects)
│   ├── server.py                # MCP server entry point (MCP projects)
│   ├── main.py                  # CLI/script entry point (some projects)
│   ├── requirements.txt         # Pip dependencies (older-style projects)
│   ├── pyproject.toml           # Modern Python project config (newer projects)
│   ├── uv.lock                  # Locked deps for uv-based projects
│   ├── .env.example             # Template for required environment variables
│   ├── .gitignore               # Ignores .env, __pycache__, .DS_Store
│   └── config/                  # CrewAI YAML configs (agent/CrewAI projects)
│       ├── agents.yaml
│       └── tasks.yaml
└── ...
```

Each project directory is **completely independent** — it has its own dependencies, entry point, and README. There is no monorepo build system tying them together.

---

## Project Categories

### 1. CrewAI Multi-Agent Projects
Agent orchestration using the [CrewAI](https://github.com/joaomdmoura/crewAI) framework.

Key projects: `agentic_rag/`, `hotel-booking-crew/`, `flight-booking-crew/`, `content_planner_flow/`, `documentation-writer-flow/`, `financial-analyst-deepseek/`, `Multi-Agent-deep-researcher-mcp-windows-linux/`

Structure pattern:
```
src/<project_name>/
├── main.py          # run(), train(), replay(), test() entry points
├── crew.py          # Crew class definition
├── tools/           # Custom tool classes
│   └── custom_tool.py
└── config/
    ├── agents.yaml  # Agent role/goal/backstory definitions
    └── tasks.yaml   # Task descriptions and expected outputs
```

CrewAI projects use `hatchling` as build backend and `uv` as the package manager. Run with `uv run python src/<name>/main.py` or `crewai run`.

### 2. RAG / LlamaIndex Projects
Retrieval-augmented generation using [LlamaIndex](https://github.com/run-llama/llama_index).

Key projects: `llama-4-rag/`, `llama-4_vs_deepseek-r1/`, `qwen3_vs_deepseek-r1/`, `simple-rag-workflow/`, `fastest-rag-stack/`, `trustworthy-rag/`, `video-rag-gemini/`, `rag-voice-agent/`

Entry point is typically `app.py` (Streamlit) or `workflow.py`. Evaluation data lives in `eval-data/test.csv`.

### 3. MCP Server Projects
Servers implementing the [Model Context Protocol](https://modelcontextprotocol.io/) for tool integration.

Key projects: `audio-analysis-toolkit/`, `llamaindex-mcp/`, `mcp-agentic-rag/`, `mcp-video-rag/`, `mcp-voice-agent/`, `kitops-mcp/`, `cursor_linkup_mcp/`, `sdv-mcp/`, `eyelevel-mcp-rag/`

Structure pattern:
```
<project>/
├── server.py     # MCP server definition with @server.tool() decorators
├── tools.py      # Tool implementations (some projects)
├── app.py        # Optional Streamlit client demo
└── requirements.txt
```

MCP servers use the `mcp` package (`mcp[cli]` or `fastapi-mcp`). Run with `python server.py` or `mcp run server.py`.

### 4. Model Comparison / Evaluation Projects
Side-by-side benchmarks of LLM capabilities.

Key projects: `sonnet4-vs-o4/`, `llama-4_vs_deepseek-r1/`, `qwen3_vs_deepseek-r1/`, `o3-vs-claude-code/`, `eval-and-observability/`

Use `opik` or `deepeval` for evaluation metrics. Test data in `eval-data/test.csv` or `data/test.csv`.

### 5. Voice / Audio Projects
`rag-voice-agent/`, `mcp-voice-agent/`, `audio-analysis-toolkit/`

Use AssemblyAI (transcription), Cartesia (TTS), LiveKit (real-time communication).

### 6. Notebooks / Learning
Jupyter notebooks for exploration, fine-tuning demos, and tutorials. Not meant to be run as applications.

Examples: `Build-reasoning-model/`, `DeepSeek-finetuning/`, `siamese-network/`, `knowledge distillation/`, `agentic_rag_deepseek/`

---

## Technology Stack

| Category | Key Libraries |
|---|---|
| Agent frameworks | `crewai`, `crewai-tools`, `autogen` |
| RAG / indexing | `llama-index`, `llama-index-*` plugins |
| MCP | `mcp`, `mcp[cli]`, `fastapi-mcp` |
| UI | `streamlit` |
| LLM providers | `openai`, `google-generativeai`, `groq`, `cerebras-cloud-sdk` |
| Local LLMs | `ollama` (via llama-index-llms-ollama) |
| Vector DBs | `qdrant-client`, `fastembed` |
| Browser automation | `browserbase`, `playwright` |
| Audio/Speech | `assemblyai`, `cartesia`, `livekit` |
| Data | `pandas`, `pdfplumber`, `yfinance` |
| Evaluation | `opik`, `deepeval` |
| Memory | `zep-cloud` |
| Build / packaging | `uv`, `hatchling`, `pip` |
| Data validation | `pydantic` v2 |

---

## Development Conventions

### Environment Variables
- Never commit `.env` files. Each project provides a `.env.example` listing required keys.
- Copy `.env.example` to `.env` and fill in values before running.
- Common keys: `OPENAI_API_KEY`, `MODEL` (model name string), `SERPER_API_KEY`, `FIRECRAWL_API_KEY`, `BROWSERBASE_API_KEY`, `GOOGLE_API_KEY`.

### Dependency Management
Two patterns coexist:

**Modern (uv + pyproject.toml)** — preferred for new projects:
```bash
cd <project>
uv sync          # install deps from uv.lock
uv run python app.py
```

**Traditional (pip + requirements.txt)**:
```bash
cd <project>
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
python app.py
```

### Python Version
Most projects target Python 3.10–3.13. Use the version specified in `.python-version` or `pyproject.toml` if present.

### Adding a New Project
1. Create a new directory at the repo root: `mkdir <project-name>`
2. Add `README.md` describing the project and how to run it
3. Add `.env.example` listing all required environment variables
4. Add `.gitignore` (at minimum ignore `.env`, `__pycache__/`, `.DS_Store`)
5. Add either `requirements.txt` or `pyproject.toml` with locked dependencies
6. Use `app.py` as the Streamlit entry point or `server.py` for MCP servers
7. Update the root `README.md` to include the project in the index

### Code Style
- No enforced linter/formatter is configured repo-wide. Follow the style of the existing file being edited.
- CrewAI projects follow the standard CrewAI project scaffold generated by `crewai create`.
- Use `python-dotenv` and `load_dotenv()` for loading `.env` files.
- Keep agent/task definitions in YAML (`config/agents.yaml`, `config/tasks.yaml`), not hardcoded in Python.

---

## Running Projects

### Streamlit Apps (most projects)
```bash
cd <project>
# install deps, then:
streamlit run app.py
```

### CrewAI Agents
```bash
cd <project>
uv run python src/<name>/main.py   # or: crewai run
```

### MCP Servers
```bash
cd <project>
python server.py          # standalone
# or via MCP CLI:
mcp run server.py
```

### Jupyter Notebooks
```bash
jupyter notebook <notebook>.ipynb
```

---

## Testing

There is no repo-wide test suite. Project-level testing:

- **CrewAI projects** expose a `test()` function in `main.py` that runs the crew for N iterations and evaluates with `crewai.evaluate`.
- **Evaluation projects** use `eval-data/test.csv` with `opik` or `deepeval` to benchmark model outputs.
- **`video-rag-gemini/test_setup.py`** verifies environment setup prerequisites.

When modifying a project, manually run the app or agent to verify behavior. There are no automated CI checks currently configured.

---

## Git Workflow

- **Feature branch:** `claude/add-claude-documentation-jZBGB` (current)
- **Main branches:** `master` / `main` (equivalent, both in use)
- Commit messages are short and descriptive (e.g., `"add llama-4-rag project"`, `"update README"`).
- PRs are merged from contributor forks into the main branch.

---

## Key Files to Know

| File | Purpose |
|---|---|
| `README.md` | Root index of all projects — update when adding new projects |
| `assets/ai-eng-hub.gif` | Demo GIF embedded in root README |
| `<project>/.env.example` | Required env vars — always provide this in new projects |
| `<project>/config/agents.yaml` | CrewAI agent definitions |
| `<project>/config/tasks.yaml` | CrewAI task definitions |
| `<project>/pyproject.toml` | Python project metadata and deps (modern projects) |

---

## What NOT to Do

- Do not add a global `requirements.txt` or `pyproject.toml` at the repo root — each project manages its own dependencies.
- Do not commit `.env` files or any file containing API keys.
- Do not create shared utility modules used across projects — keep each project self-contained.
- Do not add CI/CD configuration unless explicitly requested.
- Do not modify unrelated projects when fixing a bug in one project.
