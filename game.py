# Main game loop, calling the appropriate functions from menu.py at each stage
# Track player score
# Show final score and option to replay
# import quiz_handler as handler
import menu
import quiz_handler as handler
from enum import Enum

# --------------------------------
# GLOBALS
# --------------------------------

NUMBER_OF_ROUNDS = 2
NUMBER_OF_HINTS = 3


class GameMode(Enum):
    """
    This enumerator sets the mode in which the game will be played.
    """

    WHO = "who"
    WHAT = "what"
    WHERE = "where"
    WHEN = "when"


class WhoCategory(Enum):
    SPORTS = "sports"
    INFLUENTIAL = "influential"


class WhatCategory(Enum):
    ANIMALS = "animals"
    KITCHEN_ITEMS = "kitchen_items"
    TECHNOLOGY = "technology"


class WhereCategory(Enum):
    MONUMENTS = "monuments"
    CITIES = "cities"
    NATIONAL_PARKS = "national_parks"


class WhenCategory(Enum):
    FESTIVITIES = "festivities"
    WARS = "wars"
    INVENTIONS = "inventions"


CATEGORY_MAP = {
    GameMode.WHO: WhoCategory,
    GameMode.WHAT: WhatCategory,
    GameMode.WHERE: WhereCategory,
    GameMode.WHEN: WhenCategory,
}


# --------------------------------
# HELPER FUNCTIONS
# --------------------------------


def get_category_options(mode: GameMode):
    """
    Returns a list of available enumerator category options for the given mode.
    """

    category_options = list(CATEGORY_MAP[mode])
    return category_options


# --------------------------------
# FUNCTIONS
# --------------------------------


def get_points(attempt):
    """
    Takes in the attempt number (1, 2, or 3) and translates/returns corresponding points
    Args:
        attempt:

    Returns: The corresponding points (5, 3, 1)
    """

    points_map = {1: 5, 2: 3, 3: 1}
    get_user_points = points_map.get(attempt, 0)
    return get_user_points


def play_round(question_data):
    """
    This handles what happens for a single round.
    Args:
        question_data:

    Returns: score earned in the round
    """
    print(f"\n--- Here is your Question ---")

    for attempt in range(1, NUMBER_OF_HINTS + 1):
        # This will find the clue by matching the number: clue1, clue2, or clue3
        clue_to_show = question_data[f"clue{attempt}"]
        print(f"Hint {attempt}: {clue_to_show}")

        # We can use the menu to get the player's guess
        player_guess = menu.get_input("Your guess: ").strip().lower()

        if player_guess == question_data["answer"].lower():
            points_earned = get_points(attempt)
            print(f"Correct! You earned {points_earned} points.")
            return points_earned

    print(
        f"You have unfortunately exhausted all your tries! The answer was: {question_data['answer']}"
    )
    return None


def start_game():
    """
    This function runs the round loop,
    tracks the total score,
    and calls the final scoreboard.

    Returns: total_score

    Main flow: Pick mode -> Pick category -> Play rounds -> Show score."""

    # The player picks a mode they want to play (WHO, WHAT, etc.) via menu
    chosen_mode_str = menu.select_mode()
    mode = GameMode(chosen_mode_str)

    # We can get the subcategories from the helper
    options = get_category_options(mode)
    sub_category = menu.select_sub_category(options)

    # We get the Wikipedia resources or questions
    question_bank = handler.get_questions(mode, sub_category)

    total_score = 0

    # The player plays the required number of rounds
    for i in range(NUMBER_OF_ROUNDS):
        current_question = question_bank[i]
        total_score += play_round(current_question)

    # We then show the scoreboard and handle replay via menu
    print(f"\nFINAL SCORE: {total_score}")
    if menu.ask_replay():
        start_game()
    else:
        print("See you next time!")
