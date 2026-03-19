from logic_utils import (
    get_range_for_difficulty,
    parse_guess,
    check_guess,
    update_score,
)


def test_get_range_for_difficulty_values():
    """Difficulty ranges should match the specification."""
    assert get_range_for_difficulty("Easy") == (1, 20)
    assert get_range_for_difficulty("Normal") == (1, 50)
    assert get_range_for_difficulty("Hard") == (1, 100)


def test_parse_guess_int_and_float_strings():
    """`parse_guess` should accept integer and float-like strings and convert to int."""
    ok, val, err = parse_guess("7")
    assert ok and err is None and val == 7

    ok, val, err = parse_guess("7.0")
    assert ok and err is None and val == 7


def test_check_guess_handles_numeric_and_string_secret():
    """check_guess must compare numerically even if secret is a string."""
    outcome, message = check_guess(9, 42)
    assert outcome == "Too Low"

    # secret passed as string should behave the same
    outcome_s, message_s = check_guess(9, "42")
    assert outcome_s == "Too Low"


def test_check_guess_correct_messages():
    """Returned message text should indicate direction consistently."""
    _, msg_low = check_guess(9, 42)
    assert "HIGHER" in msg_low or "Go HIGHER" in msg_low

    _, msg_high = check_guess(100, 42)
    assert "LOWER" in msg_high or "Go LOWER" in msg_high


def test_update_score_win_minimum_points():
    """Winning awards at least the minimum point floor (10)."""
    # Simulate a late win (large attempt_number) so raw formula would go below 10
    score = update_score(0, "Win", attempt_number=20)
    assert score >= 10


# Original simple tests preserved (updated to match current check_guess signature)
def test_winning_guess():
    """If the secret is 50 and guess is 50, it should be a win."""
    outcome, _ = check_guess(50, 50)
    assert outcome == "Win"


def test_guess_too_high():
    """If secret is 50 and guess is 60, hint should be 'Too High'."""
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High"


def test_guess_too_low():
    """If secret is 50 and guess is 40, hint should be 'Too Low'."""
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low"
