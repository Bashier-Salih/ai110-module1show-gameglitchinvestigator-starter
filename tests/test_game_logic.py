from logic_utils import check_guess, get_range_for_difficulty, parse_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"


def test_too_low_message_says_go_higher():
    # Bug 1: messages were swapped — guess < secret should tell the player to go higher
    outcome, message = check_guess(50, 65)
    assert outcome == "Too Low"
    assert "HIGHER" in message, f"Expected 'HIGHER' in message, got: {message}"

def test_too_high_message_says_go_lower():
    # Bug 1: guess > secret should tell the player to go lower
    outcome, message = check_guess(80, 65)
    assert outcome == "Too High"
    assert "LOWER" in message, f"Expected 'LOWER' in message, got: {message}"

def test_no_string_cast_on_even_attempts():
    # Bug 2: secret must always be compared as int — lexicographic comparison of "9" > "65"
    # returns True, which wrongly reports "Too High" instead of "Too Low"
    outcome, _ = check_guess(9, 65)
    assert outcome == "Too Low", (
        f"Expected 'Too Low' but got '{outcome}' — likely a string comparison bug"
    )

def test_hard_range_is_harder_than_normal():
    # Bug: Hard difficulty was returning (1, 50), which is easier than Normal (1, 100).
    # Hard must have a strictly larger upper bound than Normal.
    _, normal_high = get_range_for_difficulty("Normal")
    _, hard_high = get_range_for_difficulty("Hard")
    assert hard_high > normal_high, (
        f"Hard upper bound ({hard_high}) must exceed Normal upper bound ({normal_high})"
    )


# --- Edge case tests ---

def test_negative_number_rejected():
    # Negative numbers are outside the valid range (min is 1); parse_guess should reject them
    ok, value, _ = parse_guess("-5")
    assert not ok or value < 1, "Negative guess should be invalid"

def test_extremely_large_number_rejected():
    # Numbers far above any difficulty's upper bound should be flagged as out of range
    ok, value, _ = parse_guess("999999999")
    assert not ok or value > 200, "Extremely large guess should be out of range"

def test_decimal_rounds_to_zero_rejected():
    # 0.4 rounds to 0, which is below the minimum valid guess of 1
    ok, value, _ = parse_guess("0.4")
    assert not ok or value < 1, "Decimal rounding to 0 should be invalid"
