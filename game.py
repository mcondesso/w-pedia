# Main game loop, calling the appropriate functions from menu.py at each stage
# Track player score
# Show final score and option to replay
import menu
from quiz_handler import QuizHandler
from globals import *

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


# TODO! move to menu.py
def display_new_round():
    """
    Displays the new round message.
    :return:
    """

    print(f"\n--- Here is your Question ---")


def play_round(question_data):
    """
    This handles what happens for a single round.
    Args:
        question_data:

    Returns: score earned in the round
    """

    display_new_round()
    # track attempts
    for attempt in range(1, NUMBER_OF_HINTS + 1):

        # This will find the clue by matching the number: clue1, clue2, or clue3
        clue_to_show = question_data["hints"][attempt - 1]
        print(f"Hint {attempt}:")

        # hand over user input to menu
        player_guess = menu.display_question(
            clue_to_show, question_data["answer"], question_data["options"]
        )

        # validate answer
        if player_guess.lower() == question_data["answer"].lower():
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

    Main flow: Pick mode -> Pick category -> Play rounds -> Show score.
    """

    # The player picks a mode they want to play (WHO, WHAT, etc.) via menu
    game_settings = menu.main_menu()
    print("Reading Game Settings...")
    # TODO! ADD validation for game_settings, check not empty and that its a valid enum.
    # get quiz
    handler = QuizHandler.handle_quiz(
        mode=game_settings["mode"], game_category=game_settings["category"]
    )
    quiz = handler.generate_quiz()

    total_score = 0

    # The player plays the required number of rounds
    for i in range(NUMBER_OF_ROUNDS):
        current_question = quiz[i]
        total_score += play_round(current_question)

    # We then show the scoreboard and handle replay via menu
    print(f"\nFINAL SCORE: {total_score}")

    # restart
    start_game()

    # if menu.ask_replay():
    #     start_game()
    # else:
    #     print("See you next time!")
