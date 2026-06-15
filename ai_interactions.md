# AI Interactions Log

> **Stretch features only.** Only fill in the sections that apply to stretch features you attempted. If you did not attempt a stretch feature, leave its section blank or delete it. This file is not required for the core project.

---

## Agent Workflow (SF8)

> Document your experience using an AI agent (e.g., Cursor Agent, Claude, Copilot) to make multi-step changes autonomously.

**What task did you give the agent?**

I asked Claude Code to plan and implement a High Score tracker that saves the best score per difficulty level across games.

**What did the agent do?**

1. Read app.py to understand the current session state and UI structure before making any changes
2. Added load_high_scores() and save_high_score() to logic_utils.py, using a high_scores.json file to persist scores between sessions
3. Updated the import line in app.py to include the two new functions
4. Added a High Scores section to the sidebar showing best scores for all three difficulties, with a crown next to the active difficulty
5. Updated the win handler to call save_high_score() and display "New high score!" if the player broke their record

**What did you have to verify or fix manually?**

The agent showed the plan before writing any code and asked for confirmation, which I approved. After implementation I ran the app manually to verify the sidebar updated correctly and the JSON file was created on first win. The agent also noted that linter hints appeared during editing (unused imports) but explained they would resolve once the functions were wired into the UI — which they did.

---

## Test Generation (SF7)

> Document how you used AI to help generate or improve tests.

| Edge Case | Prompt Used | AI-Suggested Test | Did It Pass? | Your Reasoning |
|-----------|-------------|-------------------|--------------|----------------|
| | | | | |
| | | | | |
| | | | | |

---

## Linting & Style (SF9)

> Document your use of AI for linting or code style improvements.

**Prompt used:**
**Challenge 1**
```
Prompt 1 (identifying edge cases):

"I finished fixing the bugs. What are some edge case inputs that could still break the game? Like weird numbers the player might type?"

Prompt 2 (generating the tests):

"Can you write pytest cases for those three edge cases and add them to my existing test file?"

Prompt 3 (following up on results):

"All 10 tests passed. But do the edge case tests actually enforce a fix or just document the current behavior?"

```
**Challenge 3**
```
Prompt 1 (Adding docstrings to every function):

I want you to add to add professional-grade docstrings to every function in logic_utils.py. but before you do that can you explain what it is

Prompt 2 (Reviewing the code):

I want you to review your code for PEP 8 style compliance and apply its suggestions to resolve any formatting or naming issues it identifies.

```

**Linting output before:**

**Challenge 3**
```
logic_utils.py:24:80: E501 line too long (85 > 79 characters)
logic_utils.py:59:80: E501 line too long (147 > 79 characters)
logic_utils.py:77:80: E501 line too long (87 > 79 characters)
logic_utils.py:108:80: E501 line too long (150 > 79 characters)

```

**Changes applied:**

**Challenge 3**
All four violations were E501 — lines exceeding the 79-character limit. The AI ran pycodestyle to identify them, then wrapped the offending lines across multiple lines. The affected lines were all inside docstrings and inline comments, not logic code. After applying the changes, re-running pycodestyle logic_utils.py returned no violations.

---

## Model Comparison (SF11)

> Compare two AI models on the same task.

**Task given to both models:**

<!-- Describe what you asked each model to do -->

| | Model A | Model B |
|-|---------|---------|
| **Model name** | | |
| **Response summary** | | |
| **More Pythonic?** | | |
| **Clearer explanation?** | | |

**Which did you prefer and why?**

<!-- Your conclusion -->
