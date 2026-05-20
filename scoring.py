import json
from pathlib import Path
from typing import List, Dict

LEADERBOARD_FILE = Path("leaderboard.json")
MAX_ENTRIES = 10


def load_leaderboard() -> List[Dict]:
    """
    Loads leaderboard from file.
    Returns empty list if file doesn't exist or is invalid.
    """

    if not LEADERBOARD_FILE.exists():
        return []

    try:
        with open(LEADERBOARD_FILE, "r") as f:
            data = json.load(f)

        if not isinstance(data, list):
            return []

        return data

    except (json.JSONDecodeError, IOError):
        return []


def save_leaderboard(leaderboard: List[Dict]):
    """
    Saves leaderboard to file.
    """

    with open(LEADERBOARD_FILE, "w") as f:
        json.dump(leaderboard, f, indent=4)


def update_leaderboard(
    player: str, score: int, number_of_rounds: int, hints_per_round: int
):
    """
    Updates leaderboard with a new score entry.
    Keeps only top 10 scores (sorted descending).
    """

    leaderboard = load_leaderboard()

    new_entry = {
        "player": player,
        "score": score,
        "number_of_rounds": number_of_rounds,
        "hints_per_round": hints_per_round,
    }

    leaderboard.append(new_entry)

    # Sort by score (highest first)
    leaderboard.sort(key=lambda x: x.get("score", 0), reverse=True)

    # Keep only top 10
    leaderboard = leaderboard[:MAX_ENTRIES]

    save_leaderboard(leaderboard)
    return leaderboard
