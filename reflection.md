# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

1. The first bug I noticed was that when I enter a guess for example 50, and the correct number was 65, the pragram would respond with "Go LOWER". This is wrong since 65 > 50 so the program should've responded with "Go HIGHER".

2. The second bug I noticed was that when I changed the game mode from normal to hard, the range went from 1-100 to 1-50, when in fact it should've been the opposite. The hard game mode should have a bigger range when compared to the normal game mode.

3.The third bug I noticed was that when I guess the correct number and I press on "Start new game", the secret number actually updates to a new number, but when I try to input a new guess for the new secret number, nothing happens. It should've processed my input similar to how it worked out at first.

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-------------------|-----------------|------------------------|
|50 |Go HIGHER! |Go LOWER! |NONE |
|101 |GO LOWER! |Go HIGHER! | NONE|
| -34|Go HIGHER |GO LOWER! |NONE |

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
I used Claude Code.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
When I asked claude Code to explain the hint message bug, it identified that in check_guess, the messages "Go HIGHER!" and "Go LOWER!" were attached to the wrong outcomes. I verified this by tracing the logic manually: if my guess (50) is less than the secret (65), the outcome is "Too Low", but the old code would display "Go LOWER!", sending me in the wrong direction. After the fix in logic_utils.py, I tested it in the running app and confirmed the hints now match the correct direction.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
When Claude Code refactored the new game handler, it suggested resetting st.session_state.attempts to 1 and also resetting score and history to their defaults. While resetting status and attempts was correct and necessary, resetting score and history was not asked for and changes game behavior, a player might want their score to carry across rounds. I caught this by reviewing the diff before accepting the edit and rejected that part of the suggestion, keeping only the status reset that was needed to fix the actual bug.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I decided a bug was really fixed by running pytest and confirming the relevant test passed, and then also verifying the behaviour manually in the running app.


- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
I ran `pytest tests/test_game_logic.py` after fixing the Hard difficulty range. The test `test_hard_range_is_harder_than_normal` asserted that Hard's upper bound must exceed Normal's (100). Before the fix, that test would have failed because Hard was returning 1–50. After the fix it passed, which confirmed the range was corrected. Running the suite also caught that the older tests (`test_winning_guess`, `test_guess_too_high`, `test_guess_too_low`) were asserting against a plain string when `check_guess` actually returns a tuple — a secondary bug the tests revealed.


- Did AI help you design or understand any tests? How?
Yes. I asked Claude Code to write a pytest case specifically targeting the Hard difficulty bug. It generated `test_hard_range_is_harder_than_normal`, which fetches both ranges from `get_range_for_difficulty` and compares their upper bounds. This approach was better than hardcoding a number like `assert hard_high == 1000`, because it tests the relationship between difficulties rather than an arbitrary value. Claude also spotted that the existing tests were broken by the tuple return and explained exactly why the `AssertionError` was occurring.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
