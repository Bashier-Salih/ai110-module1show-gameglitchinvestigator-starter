# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [ ] Describe the game's purpose.
A number guessing game where the player picks a difficulty, then tries to guess a randomly chosen secret number within a limited number of attempts. After each guess, the game gives a directional hint (go higher/lower) and updates the player's score based on the outcome and attempt number.

- [ ] Detail which bugs you found.
The hint messages in check_guess were inverted, "Go HIGHER!" was shown when the guess was too high, and "Go LOWER!" when it was too low.
The Hard difficulty range (1–50) was narrower than Normal (1–100), making it easier instead of harder.
After winning and clicking "New Game", the game froze, the status field was never reset to "playing", so st.stop() blocked all input processing.

- [ ] Explain what fixes you applied.
Swapped the hint messages in check_guess inside logic_utils.py so "Go LOWER!" maps to "Too High" and "Go HIGHER!" maps to "Too Low".
Updated get_range_for_difficulty in logic_utils.py to return (1, 200) for Hard, making it the widest range.
All four logic functions (get_range_for_difficulty, parse_guess, check_guess, update_score) were refactored out of app.py into logic_utils.py. Bug 3 (status reset) was identified but not yet applied.

## 📸 Demo Walkthrough

Describe your fixed game in numbered steps so a reader can follow along without watching a video:

1. User enters a guess of 50
2. Game returns "Go HIGHER!"
3. User enters a guess of 70
4. Game returns "Go LOWER!"
5. User enters a guess of 60
6. Game returns "Go LOWER!"
7. Score updates correctly after each guess
8. Game ends after the correct guess

**Screenshot** *(optional)*: <!-- Insert a screenshot of your fixed, winning game here -->

## 🧪 Test Results

```
================================================================= test session starts =================================================================
platform darwin -- Python 3.13.7, pytest-9.0.3, pluggy-1.6.0 -- /Users/bashiersalih/CodePath Projects/ai110-module1show-gameglitchinvestigator-starter/.venv/bin/python
cachedir: .pytest_cache
rootdir: /Users/bashiersalih/CodePath Projects/ai110-module1show-gameglitchinvestigator-starter
plugins: anyio-4.13.0
collected 10 items                                                                                                                                    

tests/test_game_logic.py::test_winning_guess PASSED                                                                                             [ 10%]
tests/test_game_logic.py::test_guess_too_high PASSED                                                                                            [ 20%]
tests/test_game_logic.py::test_guess_too_low PASSED                                                                                             [ 30%]
tests/test_game_logic.py::test_too_low_message_says_go_higher PASSED                                                                            [ 40%]
tests/test_game_logic.py::test_too_high_message_says_go_lower PASSED                                                                            [ 50%]
tests/test_game_logic.py::test_no_string_cast_on_even_attempts PASSED                                                                           [ 60%]
tests/test_game_logic.py::test_hard_range_is_harder_than_normal PASSED                                                                          [ 70%]
tests/test_game_logic.py::test_negative_number_rejected PASSED                                                                                  [ 80%]
tests/test_game_logic.py::test_extremely_large_number_rejected PASSED                                                                           [ 90%]
tests/test_game_logic.py::test_decimal_rounds_to_zero_rejected PASSED                                                                           [100%]

================================================================= 10 passed in 0.03s ==================================================================
```

## 🚀 Stretch Features

**Challenge 4**
UI Enhancements

Three visual improvements were added to make the game more informative and easier to read:

1. Color-coded hint messages
The hint display in app.py now uses Streamlit's colored alert components instead of a plain st.warning for every guess. A "Too Low" result renders in blue (st.info) and a "Too High" result renders in orange (st.warning), giving the player an immediate visual cue about which direction to go.

2. Hot/Cold proximity indicator
A new function get_hotcold_label(guess, secret, low, high) was added to logic_utils.py. It calculates how close the guess is to the secret as a percentage of the difficulty range and returns one of four labels shown alongside the hint:

🔥 Burning hot — within 5% of the range
♨️ Warm — within 15%
🌡️ Lukewarm — within 35%
🧊 Ice cold — beyond 35%
3. Session summary table
After each game ends (win or loss), a summary table is displayed using st.table() in app.py. It shows every attempt in order, including the guess value, the outcome (Too Low / Too High / Win), and the hot/cold rating for that guess.
