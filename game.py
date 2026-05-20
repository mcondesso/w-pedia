# Main game loop, calling the appropriate functions from menu.py at each stage
# Track player score
# Show final score and option to replay
import random
import sys

import globals
import menu
import scoring
from menu import display_error_message, display_change_rounds
from quiz_handler import QuizHandler, QuizHandlerError
from globals import *

EXAMPLE_QUIZ = [
    {
        "hints": [
            "Who is a Wizard in Lord of the Rings?",
            "Sometimes he's white, sometimes he's grey",
            "He's a good Wizard",
        ],
        "answer": "Gandalf",
        "options": ["Frodo", "Saruman", "Smeagol"],
    },
    {
        "hints": [
            "Who is a Mouse?",
            "Disney",
            "Loves minnie",
        ],
        "answer": "Mickey Mouse",
        "options": ["Minie", "Donald", "Pluto"],
    },
]


# --------------------------------
# HELPER FUNCTIONS
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


def shuffle_options(answer, options):
    """
    Shuffles the options and answers.
    :param question:
    :param answer:
    :param options:
    :return: randomly shuffled anwer and options in a combined list.
    """

    choices = [answer] + options
    random.shuffle(choices)

    return choices


def play_round(question_data, settings, num_round):
    """
    This handles what happens for a single round.
    Args:
        question_data:

    Returns: score earned in the round
    """

    points_earned = 0
    menu.display_new_round(num_round)

    # prompt player
    options_shuffled = shuffle_options(
        question_data["answer"], question_data["options"]
    )

    # track attempts

    is_correct = None
    for attempt in range(1, settings["number_of_hints"] + 1):

        if attempt > 1:
            menu.display_result_answer(
                is_correct=is_correct, points=0, answer=question_data["answer"]
            )

        # This will find the hint by matching the number: hint1, hint2, or hint3
        hint_to_show = question_data["hints"][attempt - 1]

        player_guess = menu.display_question(
            f"Hint {attempt}: " + hint_to_show, options_shuffled
        )
        if player_guess is None:
            replay_game(settings)
        # validate answer
        if player_guess.lower() == question_data["answer"].lower():
            is_correct = True
            points_earned = get_points(attempt)
            menu.display_result_answer(
                is_correct=is_correct,
                points=points_earned,
                answer=question_data["answer"],
            )
            break

    if not is_correct:
        menu.display_result_answer(
            is_correct=False, points=0, answer=question_data["answer"]
        )
        points_earned = 0

    menu.wait_for_enter()
    return points_earned


def validate_game_settings(game_settings):
    """
    Validates the game settings before starting the game.
    :return:
    """
    if not game_settings:
        raise ValueError("Game settings cannot be empty.")

    if not isinstance(game_settings, dict):
        raise TypeError("Game settings must be a dictionary.")

    required_keys = [
        "player_name",
        "game_mode",
        "game_category",
        "number_of_players",
        "number_of_rounds",
        "number_of_hints",
    ]
    for key in required_keys:
        if key not in game_settings:
            raise KeyError(f"Missing required game setting: '{key}'")

    player_name = game_settings["player_name"]
    if not isinstance(player_name, str) or not player_name.strip():
        raise ValueError("Player name must be a non-empty string.")

    game_mode = game_settings["game_mode"]
    if not isinstance(game_mode, GameMode):
        raise TypeError("game_mode must be a valid GameMode enum.")

    game_category = game_settings["game_category"]

    valid_category_enum = CATEGORY_MAP[game_mode]

    if not isinstance(game_category, valid_category_enum):
        raise TypeError(
            f"game_category must be a valid category for mode '{game_mode.value}'."
        )

    number_of_players = game_settings["number_of_players"]

    if not isinstance(number_of_players, int):
        raise TypeError("number_of_players must be an integer.")

    if number_of_players <= 0:
        raise ValueError("number_of_players must be greater than 0.")


def replay_game():
    """Handle end of game event ask if user wants to play again."""

    choice = menu.replay_menu()
    return choice == "Yes"


def start_game(settings):
    """
    This function runs the round loop, tracks the total score, and calls the final scoreboard.
    Main flow: Pick mode -> Pick category -> Play rounds -> Show score.
    """

    # validate game settings
    print(f"Checking Settings...")
    try:
        validate_game_settings(settings)
    except (KeyError, TypeError, ValueError) as e:
        menu.display_error_message(e)
        return

    # CALL TO API COMMENT OUT WHEN DEBUGGING ANYTHING BUT API
    # -------------
    # get quiz
    handler = QuizHandler.handle_quiz(
        mode=settings["game_mode"], game_category=settings["game_category"]
    )
    try:
        quiz = handler.generate_quiz()
    except QuizHandlerError:
        print("Unable to generate quiz, please try again later.")
        sys.exit(1)

    # ---------UNCOMMENT HERE WHEN TESTING UI
    # quiz = EXAMPLE_QUIZ

    total_score = 0
    score_rounds = []
    # The player plays the required number of rounds
    max_rounds = min(settings["number_of_rounds"], len(quiz))
    for i in range(max_rounds):

        current_question = quiz[i]
        tmp_score = play_round(current_question, settings, i+1)
        score_rounds.append(tmp_score)
        total_score += tmp_score

    # We then show the scoreboard and handle replay via menu
    scores = {
        "player_name": settings["player_name"],
        "score_rounds": score_rounds,
        "total": total_score,
    }
    menu.display_end_of_game(scores=scores)

    # update the leaderboard
    leaderboard = scoring.update_leaderboard(
        player=settings["player_name"],
        score=total_score,
        number_of_rounds=settings["number_of_rounds"],
        hints_per_round=settings["number_of_hints"],
    )

    menu.prompt_display_leaderboard(leaderboard)

    # restart
    if replay_game():
        return

    menu.display_quit()
    sys.exit(0)


def handle_settings(settings):

    while True:

        choice = menu.display_settings_menu()

        if choice == "Change number of rounds":

            rounds = int(menu.display_change_rounds())

            settings["number_of_rounds"] = rounds
            globals.NUMBER_OF_ROUNDS = rounds

        elif choice == "Change number of tries/hints":

            hints = int(menu.display_change_hints())

            settings["number_of_hints"] = hints
            globals.NUMBER_OF_HINTS = hints

        elif choice == "Back":

            return settings


def main():
    """Main function of the game."""

    settings = DEFAULT_SETTINGS.copy()

    menu.show_welcome()

    while True:

        choice = menu.show_main_menu()

        if choice == "Start the game":
            game_mode, game_category, number_of_players, player_name = menu.start_game()
            settings["game_mode"] = game_mode
            settings["game_category"] = game_category
            settings["number_of_players"] = number_of_players
            settings["player_name"] = player_name
            start_game(settings=settings)

        elif choice == "Instructions":
            menu.display_instructions_menu()

        elif choice == "Settings":
            settings = handle_settings(settings)

        elif choice == "Quit":
            menu.display_quit()
            break
