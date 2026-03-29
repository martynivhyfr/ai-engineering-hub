import streamlit as st
from crew import run_strategos

st.set_page_config(
    page_title="Code STRATEGOS",
    page_icon="⚔️",
    layout="wide",
)

# ── Header ────────────────────────────────────────────────────────────────────
st.title("⚔️ Code STRATEGOS")
st.markdown(
    """
    **Code STRATEGOS** is a multi-agent AI system that approaches every coding
    problem like a military campaign.
    Four specialized agents — *Strategist*, *Architect*, *Developer*, and
    *Reviewer* — collaborate sequentially to deliver a battle-hardened
    solution.
    """
)
st.divider()

# ── Sidebar ───────────────────────────────────────────────────────────────────
with st.sidebar:
    st.header("⚙️ Command Center")
    st.markdown(
        """
        **Agent Pipeline**

        1. 🎯 **Strategist** — analyzes the problem and defines the approach
        2. 🗺️ **Architect** — designs the technical blueprint
        3. 💻 **Developer** — implements the code
        4. 🔍 **Reviewer** — reviews and refines the final solution
        """
    )
    st.divider()
    st.markdown(
        "Built with [CrewAI](https://github.com/joaomdmoura/crewAI) · "
        "[OpenAI](https://openai.com)"
    )

# ── Problem input ─────────────────────────────────────────────────────────────
st.subheader("📋 State Your Mission")

example_problems = [
    "Write a Python function that finds the longest palindromic substring in a given string.",
    "Implement a thread-safe LRU cache in Python with O(1) get and put operations.",
    "Build a Python CLI tool that watches a directory for new files and compresses them automatically.",
    "Write a rate limiter in Python using the token bucket algorithm.",
]

with st.expander("💡 Example problems", expanded=False):
    for i, example in enumerate(example_problems, 1):
        if st.button(f"Example {i}", key=f"ex_{i}"):
            st.session_state["problem_input"] = example

problem = st.text_area(
    "Describe the coding problem you want solved:",
    value=st.session_state.get("problem_input", ""),
    height=140,
    placeholder="e.g. Implement a min-heap in Python with insert, extract_min, and heapify operations.",
    key="problem_input",
)

run_btn = st.button("⚔️ Deploy STRATEGOS", type="primary", disabled=not problem.strip())

# ── Run crew ──────────────────────────────────────────────────────────────────
if run_btn and problem.strip():
    with st.spinner("Marshalling the agents... this may take a minute."):
        try:
            results = run_strategos(problem.strip())
        except Exception as exc:
            st.error(f"Mission failed: {exc}")
            st.stop()

    st.success("Mission accomplished!")
    st.divider()

    tab1, tab2, tab3, tab4 = st.tabs(
        ["🎯 Strategy", "🗺️ Blueprint", "💻 Code", "🔍 Review"]
    )

    with tab1:
        st.subheader("Strategic Analysis")
        st.markdown(results["strategy"])

    with tab2:
        st.subheader("Technical Blueprint")
        st.markdown(results["blueprint"])

    with tab3:
        st.subheader("Implementation")
        # Try to extract code block; fall back to raw text
        raw = results["code"]
        if "```" in raw:
            st.markdown(raw)
        else:
            st.code(raw, language="python")

    with tab4:
        st.subheader("Code Review & Final Solution")
        raw = results["review"]
        st.markdown(raw)
