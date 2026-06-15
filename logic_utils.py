import json
import os

HIGH_SCORES_FILE = "high_scores.json"


def load_high_scores() -> dict:
    """
    Load high scores from the JSON file on disk.

    Returns:
        A dict mapping difficulty name to the best score achieved,
        e.g. {"Easy": 80, "Normal": 0, "Hard": 50}. If the file does
        not exist yet, returns all zeros.
    """
    if not os.path.exists(HIGH_SCORES_FILE):
        return {"Easy": 0, "Normal": 0, "Hard": 0}
    with open(HIGH_SCORES_FILE, "r") as f:
        return json.load(f)


def save_high_score(difficulty: str, score: int) -> bool:
    """
    Persist a new high score for the given difficulty if it beats the
    current record.

    Args:
        difficulty: One of "Easy", "Normal", or "Hard".
        score: The final score achieved in the completed game.

    Returns:
        True if the score was a new record and was saved, False otherwise.
    """
    scores = load_high_scores()
    if score > scores.get(difficulty, 0):
        scores[difficulty] = score
        with open(HIGH_SCORES_FILE, "w") as f:
            json.dump(scores, f)
        return True
    return False


def get_range_for_difficulty(difficulty: str):
    """
    Return the inclusive numeric range for a given difficulty level.

    Args:
        difficulty: One of "Easy", "Normal", or "Hard".

    Returns:
        A tuple (low, high) representing the minimum and maximum
        values the secret number can take. Defaults to (1, 100) for
        unrecognized difficulty strings.
    """
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        # FIX: I identified Hard returning (1, 50) — easier than Normal
        # (1, 100); collaborated with AI to correct upper bound to 200
        return 1, 200
    return 1, 100


def parse_guess(raw: str):
    """
    Parse raw text input from the player into an integer guess.

    Handles empty input, plain integers, and decimals (truncated to int).
    Does not validate whether the value falls within the game's range.

    Args:
        raw: The raw string typed by the player.

    Returns:
        A tuple (ok, guess_int, error_message) where:
            ok (bool): True if parsing succeeded.
            guess_int (int | None): The parsed integer, or None on failure.
            error_message (str | None): A user-facing error string, or
                None on success.
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
    Compare the player's guess to the secret number and return a result.

    Args:
        guess: The integer the player submitted.
        secret: The target number to match.

    Returns:
        A tuple (outcome, message) where:
            outcome (str): One of "Win", "Too High", or "Too Low".
            message (str): A hint string shown to the player.
    """
    if guess == secret:
        return "Win", "🎉 Correct!"
    # FIX (Bug 1): I identified swapped hint messages — "Go HIGHER" and
    # "Go LOWER" were reversed; collaborated with AI to align messages
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    return "Too Low", "📈 Go HIGHER!"


def update_score(current_score: int, outcome: str, attempt_number: int):
    """
    Calculate and return the updated score based on the guess outcome.

    Scoring rules:
        - Win: awards 100 points minus 10 per attempt, minimum 10 points.
        - Too High on an even attempt: +5 points.
        - Too High on an odd attempt: -5 points.
        - Too Low: -5 points.

    Args:
        current_score: The player's score before this guess.
        outcome: One of "Win", "Too High", or "Too Low".
        attempt_number: The 1-based attempt count for the current game.

    Returns:
        The updated integer score.
    """
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
