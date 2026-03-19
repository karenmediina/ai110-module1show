def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    # CPFIXED: Implemented ranges for difficulties (moved from app.py)
    # CPFIXED: Swapped mapping so Normal is 1-50 and Hard is 1-100
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 50
    if difficulty == "Hard":
        return 1, 100
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


def check_guess(guess, secret):
    """
    Compare guess to secret and return (outcome, message).

    outcome examples: "Win", "Too High", "Too Low"
    """
    # Normalize types: try to interpret secret as int when possible
    try:
        if not isinstance(secret, int):
            secret_int = int(secret)
        else:
            secret_int = secret
    except Exception:
        secret_int = None

    # If we have integer secret, compare numerically
    if secret_int is not None:
        if guess == secret_int:
            return "Win", "🎉 Correct!"
        if guess > secret_int:
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"

    # Fallback to string comparison
    try:
        if str(guess) == str(secret):
            return "Win", "🎉 Correct!"
        if str(guess) > str(secret):
            return "Too High", "📉 Go LOWER!"
        return "Too Low", "📈 Go HIGHER!"
    except Exception:
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
