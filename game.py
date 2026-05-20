# Main game loop, calling the appropriate functions from menu.py at each stage
# Track player score
# Show final score and option to replay
import random

import menu
from quiz_handler import QuizHandler
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


def play_round(question_data):
    """
    This handles what happens for a single round.
    Args:
        question_data:

    Returns: score earned in the round
    """

    menu.display_new_round()
    print(f"Answer: {question_data['answer']}")
    print(f"Options: {question_data['options']}")
    # prompt player
    options_shuffled = shuffle_options(
        question_data["answer"], question_data["options"]
    )
    print(f"Options: {options_shuffled}")
    # track attempts
    for attempt in range(1, NUMBER_OF_HINTS + 1):

        # This will find the clue by matching the number: clue1, clue2, or clue3
        clue_to_show = question_data["hints"][attempt - 1]
        print(f"Hint {attempt}:")

        player_guess = menu.display_question(clue_to_show, options_shuffled)
        if player_guess is None:
            replay_game()
        # validate answer
        if player_guess.lower() == question_data["answer"].lower():
            points_earned = get_points(attempt)
            print(f"Correct! You earned {points_earned} points.")
            return points_earned

    print(
        f"You have unfortunately exhausted all your tries! The answer was: {question_data['answer']}"
    )

    return None


def replay_game():
    """Handle end of game event ask if user wants to play again."""

    choice = menu.replay_menu()
    if choice == "Yes":
        start_game()
    elif choice == "No":
        print("Thank you for playing W-Pedia!")
        print("See you again soon, explorer!\n")
    else:
        print("Invalid choice.")
        print("Please enter 1 or 2.")


def initialize_game():
    """
    Get game mode, category, and player name from menu.py.

    Returns: game_settings
    """
    # The player picks a mode they want to play (WHO, WHAT, etc.) via menu
    game_settings = menu.main_menu()
    player_name = game_settings["player_name"]
    print("Reading Game Settings...")
    # TODO! ADD validation for game_settings, check not empty and that its a valid enum.

    return game_settings


def start_game():
    """
    This function runs the round loop,
    tracks the total score,
    and calls the final scoreboard.

    Returns: total_score

    Main flow: Pick mode -> Pick category -> Play rounds -> Show score.
    """

    game_settings = initialize_game()

    # CALL TO API COMMENT OUT WHEN DEBUGGING ANYTHING BUT API
    # -------------

    # get quiz
    handler = QuizHandler.handle_quiz(
        mode=game_settings["game_mode"], game_category=game_settings["game_category"]
    )
    quiz = handler.generate_quiz()

    # ---------UNCOMMENT HERE WHEN TESTING UI
    # quiz = EXAMPLE_QUIZ

    total_score = 0
    score_rounds = []
    # The player plays the required number of rounds
    for i in range(NUMBER_OF_ROUNDS):
        current_question = quiz[i]
        tmp_score = play_round(current_question)
        score_rounds.append(tmp_score)
        total_score += tmp_score

    # We then show the scoreboard and handle replay via menu
    scores = {
        "player_name": game_settings["player_name"],
        "score_rounds": score_rounds,
        "total": total_score,
    }
    menu.display_end_of_game(scores=scores)

    # restart
    replay_game()
