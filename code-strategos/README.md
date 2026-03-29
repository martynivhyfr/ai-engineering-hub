# ⚔️ Code STRATEGOS

**Code STRATEGOS** is a multi-agent AI system that approaches every coding problem like a military campaign. Four specialized agents collaborate sequentially to deliver a battle-hardened solution.

> *STRATEGOS (στρατηγός) — Greek for "general" or "army leader".*

---

## Agent Pipeline

| # | Agent | Role |
|---|-------|------|
| 1 | 🎯 **Strategist** | Analyzes the problem, identifies constraints/edge cases, and recommends the best algorithmic approach |
| 2 | 🗺️ **Architect** | Translates the strategy into a concrete technical blueprint (modules, data structures, interfaces) |
| 3 | 💻 **Developer** | Implements clean, production-ready Python code following the blueprint |
| 4 | 🔍 **Reviewer** | Reviews for correctness, performance, and security; delivers the final polished solution |

---

## Setup

### Prerequisites

- Python 3.12+
- OpenAI API key

### Install Dependencies

```bash
cd code-strategos

# Using uv (recommended)
uv sync

# Or using pip
pip install crewai crewai-tools python-dotenv streamlit
```

### Configure Environment

```bash
cp .env.example .env
# Edit .env and add your OPENAI_API_KEY
```

---

## Run

### Streamlit App (recommended)

```bash
streamlit run app.py
```

Open [http://localhost:8501](http://localhost:8501) in your browser, describe your coding problem, and click **Deploy STRATEGOS**.

### CLI

```bash
python crew.py
# You will be prompted to enter the coding problem.
```

---

## Example Problems

- *"Write a Python function that finds the longest palindromic substring."*
- *"Implement a thread-safe LRU cache with O(1) get and put operations."*
- *"Build a rate limiter using the token bucket algorithm."*
- *"Create a CLI tool that watches a directory and compresses new files automatically."*

---

## Tech Stack

| Component | Library |
|-----------|---------|
| Agent orchestration | [CrewAI](https://github.com/joaomdmoura/crewAI) |
| LLM | OpenAI GPT-4o (configurable via `MODEL` env var) |
| UI | [Streamlit](https://streamlit.io) |

---

## 📬 Stay Updated with Our Newsletter!
**Get a FREE Data Science eBook** 📖 with 150+ essential lessons in Data Science when you subscribe to our newsletter! Stay in the loop with the latest tutorials, insights, and exclusive resources. [Subscribe now!](https://join.dailydoseofds.com)

[![Daily Dose of Data Science Newsletter](https://github.com/patchy631/ai-engineering/blob/main/resources/join_ddods.png)](https://join.dailydoseofds.com)

---

## Contribution

Contributions are welcome! Please fork the repository and submit a pull request with your improvements.
