import json
import os

HIGH_SCORES_FILE = "high_scores.json"


def load_high_scores() -> dict:
    if not os.path.exists(HIGH_SCORES_FILE):
        return {"Easy": 0, "Normal": 0, "Hard": 0}
    with open(HIGH_SCORES_FILE, "r") as f:
        return json.load(f)


def save_high_score(difficulty: str, score: int) -> bool:
    """Save score if it beats the current high score. Returns True if a new record was set."""
    scores = load_high_scores()
    if score > scores.get(difficulty, 0):
        scores[difficulty] = score
        with open(HIGH_SCORES_FILE, "w") as f:
            json.dump(scores, f)
        return True
    return False


def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200  # FIX: I identified Hard returning (1, 50) — easier than Normal (1, 100); collaborated with AI to correct upper bound to 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse user input into an int guess.

    Returns: (ok: bool, guess_int: int | None, error_message: str | None)
    """
    if raw is None or raw == "":
        return False, None, "Enter a guess."

    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."

    return True, value, None


def check_guess(guess: int, secret: int):
    """
    Compare guess to secret and return (outcome, message).

    outcome: "Win", "Too High", or "Too Low"
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    # FIX (Bug 1): I identified swapped hint messages — "Go HIGHER" and "Go LOWER" were reversed; collaborated with AI to align messages with outcomes
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points

    if outcome == "Too High":
        if attempt_number % 2 == 0:
            return current_score + 5
        return current_score - 5

    if outcome == "Too Low":
        return current_score - 5

    return current_score
