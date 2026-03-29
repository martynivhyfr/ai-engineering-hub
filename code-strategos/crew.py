import os
from crewai import Agent, Task, Crew, Process, LLM
from dotenv import load_dotenv

load_dotenv()

model = os.getenv("MODEL", "gpt-4o")

llm = LLM(model=f"openai/{model}")


# ── Agents ──────────────────────────────────────────────────────────────────

strategist = Agent(
    role="Code Strategist",
    goal=(
        "Analyze the coding problem and produce a clear, high-level strategy: "
        "identify the core challenge, constraints, edge cases, and the best "
        "algorithmic / architectural approach to solve it."
    ),
    backstory=(
        "You are a seasoned software architect with 20 years of experience "
        "leading complex engineering initiatives. Like a military general "
        "surveying the battlefield before issuing orders, you always begin "
        "with a thorough analysis of the terrain before devising a plan of "
        "attack. You speak in precise, structured terms and leave no "
        "assumption unexamined."
    ),
    llm=llm,
    verbose=True,
)

architect = Agent(
    role="Software Architect",
    goal=(
        "Transform the strategist's high-level plan into a concrete technical "
        "blueprint: define modules/classes/functions, data structures, "
        "interfaces, and the sequence of operations."
    ),
    backstory=(
        "You are a principal engineer who bridges strategy and implementation. "
        "Given a battle plan, you draw detailed maps—naming every component, "
        "specifying every interface, and anticipating integration points. Your "
        "blueprints are so clear that any skilled developer can implement them "
        "without ambiguity."
    ),
    llm=llm,
    verbose=True,
)

coder = Agent(
    role="Senior Developer",
    goal=(
        "Implement clean, well-structured, production-ready Python code that "
        "faithfully follows the architect's blueprint."
    ),
    backstory=(
        "You are an elite developer who turns blueprints into battle-tested "
        "code. You write idiomatic Python, add docstrings to every public "
        "function, handle errors gracefully, and include concise inline "
        "comments where the logic is non-obvious. Your code is ready to run "
        "on first attempt."
    ),
    llm=llm,
    verbose=True,
)

reviewer = Agent(
    role="Code Reviewer",
    goal=(
        "Review the generated code for correctness, clarity, performance, and "
        "security. Provide an improved final version with a brief review "
        "summary highlighting what was changed and why."
    ),
    backstory=(
        "You are a staff engineer renowned for rigorous code reviews. You "
        "look for bugs, off-by-one errors, missing edge-case handling, "
        "inefficient algorithms, security pitfalls, and style inconsistencies. "
        "You deliver the final, battle-hardened version of the code together "
        "with a concise review report."
    ),
    llm=llm,
    verbose=True,
)


# ── Tasks ────────────────────────────────────────────────────────────────────

def build_tasks(problem: str) -> tuple[Task, Task, Task, Task]:
    strategy_task = Task(
        description=(
            f"Analyze the following coding problem and produce a strategic plan:\n\n"
            f"{problem}\n\n"
            "Your output must include:\n"
            "1. Problem summary (1-2 sentences)\n"
            "2. Key constraints and edge cases\n"
            "3. Recommended algorithmic / architectural approach with justification\n"
            "4. Potential pitfalls to watch out for"
        ),
        expected_output=(
            "A structured strategic analysis with the four sections listed above."
        ),
        agent=strategist,
    )

    blueprint_task = Task(
        description=(
            "Using the strategist's analysis, produce a detailed technical blueprint.\n\n"
            "Your output must include:\n"
            "1. Module / class / function layout (names, responsibilities, signatures)\n"
            "2. Data structures to be used\n"
            "3. Step-by-step execution flow\n"
            "4. Any external libraries required (standard library preferred)"
        ),
        expected_output=(
            "A detailed technical blueprint covering the four sections listed above."
        ),
        agent=architect,
        context=[strategy_task],
    )

    coding_task = Task(
        description=(
            "Implement the solution in Python, strictly following the architect's "
            "blueprint.\n\n"
            "Requirements:\n"
            "- Complete, runnable Python code\n"
            "- Docstrings on every public function/class\n"
            "- Inline comments for non-obvious logic\n"
            "- A `if __name__ == '__main__':` block with a brief usage example\n"
            "- No placeholder stubs — every function must be fully implemented"
        ),
        expected_output=(
            "Complete Python source code enclosed in a single Python code block."
        ),
        agent=coder,
        context=[strategy_task, blueprint_task],
    )

    review_task = Task(
        description=(
            "Review the developer's code and produce a final polished version.\n\n"
            "Your output must include:\n"
            "1. **Review Summary**: bullet-point list of issues found and fixes applied\n"
            "2. **Final Code**: the improved, complete Python source in a code block"
        ),
        expected_output=(
            "A review summary followed by the final, improved Python code block."
        ),
        agent=reviewer,
        context=[strategy_task, blueprint_task, coding_task],
    )

    return strategy_task, blueprint_task, coding_task, review_task


# ── Entry point ──────────────────────────────────────────────────────────────

def run_strategos(problem: str) -> dict:
    """Run the Code STRATEGOS crew for the given coding problem.

    Args:
        problem: Natural-language description of the coding problem to solve.

    Returns:
        A dict with keys 'strategy', 'blueprint', 'code', 'review' mapping to
        each agent's output string.
    """
    strategy_task, blueprint_task, coding_task, review_task = build_tasks(problem)

    crew = Crew(
        agents=[strategist, architect, coder, reviewer],
        tasks=[strategy_task, blueprint_task, coding_task, review_task],
        process=Process.sequential,
        verbose=True,
    )

    crew.kickoff()

    return {
        "strategy": strategy_task.output.raw if strategy_task.output else "",
        "blueprint": blueprint_task.output.raw if blueprint_task.output else "",
        "code": coding_task.output.raw if coding_task.output else "",
        "review": review_task.output.raw if review_task.output else "",
    }


if __name__ == "__main__":
    problem = input("Enter the coding problem: ")
    results = run_strategos(problem)
    for section, content in results.items():
        print(f"\n{'='*60}\n{section.upper()}\n{'='*60}\n{content}")
