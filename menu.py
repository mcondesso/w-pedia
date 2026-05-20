import random
from typing import Dict, List, Tuple

from globals import GameMode, WhoCategory, CATEGORY_MAP

INDENT = "     -----> "
SEPERATOR = "<:>:" * 40
WARNING_SEPERATOR = "-<>-" * 20
NEXT_ROUND_SEPERATOR = "¸,ø¤°`°¤ø,¸" * 20

BAD_EMOTE = "     (x__x)     -" * 3
NORMAL_EMOTE = "     (o.o)     -" * 3
GOOD_EMOTE = "     (^-^)     -" * 3

LEADERBOARD_BANNER = """
                _______________
                |@@@@|     |####|
                |@@@@|     |####|
                |@@@@|     |####|
                \\@@@@|     |####/
                 \\@@@|     |###/
                  `@@|_____|##'
                       (O)
                    .-'''''-.
                  .'  * * *  `.
                 :  *       *  :
                : ~L E A D E R~ :
                : ~ B O A R D ~ :
                 :  *       *  :
                  `.  * * *  .'
                    `-.....-'
"""


def get_player_name():
    """
    Gets the name of the player from the user.
    """

    while True:
        player_name = input("\nWhat would you like to be addressed as: ").strip()

        # Check if empty
        if not player_name:
            print("Player name cannot be empty. Please try again!")
            continue

        # Check for numbers
        if any(char.isdigit() for char in player_name):
            print("Player name cannot contain numbers. Please try again!")
            continue

        else:
            break

    return player_name


def multiple_choice_menu(question: str, choices: list[str]):
    """

    :param choices: Defines the multiple choice options
    :return:
    """
    choice = None
    while not choice:
        print(question)

        i = 1
        for c in choices:
            print(f"{i}. {c}")
            i += 1

        input_str = input("\nEnter your choice: ")
        # TODO! check the input_chosen it should not be larger or smaller than the choices list length.

        try:
            input_chosen = int(input_str)

            # Validate range
            if 1 <= input_chosen <= len(choices):
                choice = choices[input_chosen - 1]
            else:
                print(f"Please enter a number between 1 and {len(choices)}.")

        except ValueError as e:
            print(f"Could not convert your option to an integer, try again! \n {e}")

    return choice


def get_game_mode_from_user():
    """
    Asks the user to choose a game mode.
    :return: A GameMode enum value.
    """

    game_modes = list(GameMode)

    mode_choice = multiple_choice_menu(
        "\nWhich 'Mode' would you like to play today?",
        [mode.value.title() for mode in game_modes],
    )

    # Convert selected string back to enum
    game_mode = next(mode for mode in game_modes if mode.value.title() == mode_choice)

    print("\nAmazing choice!")
    print(f"Welcome to {game_mode.value.title()} mode!")
    return game_mode


def get_category_from_user(game_mode: GameMode):
    """
    Ask the user to choose a category.
    :returns: A Category enum value matching the game mode.
    """

    categories = list(CATEGORY_MAP[game_mode])

    category_choice = multiple_choice_menu(
        "\nWhich 'Category' would you like to play today?",
        [category.value.replace("_", " ").title() for category in categories],
    )

    # Convert selected string back to enum
    game_category = next(
        category
        for category in categories
        if category.value.replace("_", " ").title() == category_choice
    )

    print("\nAmazing choice!")
    print(f"Welcome to {category_choice} Category!")
    return game_category


def show_welcome():
    """
    This function displays a welcome message.
    :return:
    """
    print(SEPERATOR)
    print("Welcome to W-Pedia".center(50))
    print(SEPERATOR)

    print("\nWhere curiosity turns into knowledge,")
    print("time turns into wisdom,")
    print("and learning becomes an unforgettable adventure.\n")


def show_menu():
    """

    :return:
    """

    choice = multiple_choice_menu(
        "\nMain Menu", ["Start the game", "Instructions", "Settings", "Quit"]
    )

    if choice == "Start the game":
        game_mode, game_category, number_of_players, player_name = start_game()
        return {
            "game_mode": game_mode,
            "game_category": game_category,
            "number_of_players": number_of_players,
            "player_name": player_name,
        }

    elif choice == "Instructions":

        print("\nInstructions:")
        print("This manu is under construction.")
        print("Learn while having fun and exploring new ideas!")
        show_menu()

    elif choice == "Settings":

        print("\nSettings menu coming soon!")
        print("Here you will later customize your game experience.")
        show_menu()

    elif choice == "Quit":

        print("\nThank you for playing W-Pedia!")
        print("See you again soon, explorer!\n")
        show_menu()

        # TODO! make a quit_game() function or use quit_game() from game.py

    else:

        print("\nInvalid choice.")
        print("Please enter 1, 2, 3, or 4.")


def start_game():

    # set player name
    player_name = get_player_name()

    print(f"\nWelcome, {player_name}!")

    # set game_mode
    game_mode = get_game_mode_from_user()

    # set game category
    game_category = get_category_from_user(game_mode=game_mode)

    # set number of players
    number_of_players = 1
    return game_mode, game_category, number_of_players, player_name


def randomize_options(answer, options):
    pass


# -------------------------------------------
# Functions for GAME
# -------------------------------------------


def main_menu():
    """Function called by game.py which returns the settings for the game."""

    show_welcome()
    game_settings = show_menu()

    print(f"{INDENT}exiting main menu")
    return game_settings


def display_question(question, options):
    """
    Displays a given question with multiple choice options in the menu.
    :param question:
    :param options:
    :return: string with the chosen answer or option
    """

    try:
        selected_answer = multiple_choice_menu(question, options)
        print(f"You chose: {selected_answer}")
    except TypeError as e:
        display_error_message(e)
        return None

    return selected_answer


def display_new_round():
    """
    Displays the new round message.
    :return:
    """
    print("Congratulations! You have completed a round!")
    print(NEXT_ROUND_SEPERATOR)


def display_error_message(error_message: str):
    """
    Displays an error message and returns the user to the main menu.
    :param error_message:
    :return:
    """

    print(SEPERATOR)
    print("Oops! Something went wrong. ")

    print(WARNING_SEPERATOR)
    print(f"Error: {error_message}")
    print(WARNING_SEPERATOR)

    print("We're working on it. Please try again!")
    print(SEPERATOR)


def display_leaderboard(scores: List[Tuple[str, int]]):
    """Displays the leaderboard. Highscores of all time"""

    print(SEPERATOR)
    print(LEADERBOARD_BANNER)
    for score in scores:
        try:
            print(f"{score[0]}: {score[1]} points")
        except ValueError:
            print("ValueError displaying leaderboard player name or score")
        except IndexError:
            print("IndexError displaying leaderboard player name or score")
    print(SEPERATOR)


def display_end_of_game(scores):
    """
    Displays the end of the game message.

    scores: {player_name: str, score_rounds: [int,int,int], total: [int]}
    """

    print(SEPERATOR)
    print("Congratulations! You have completed the game!")
    print("\n")
    print(f"Player: {scores['player_name']}")
    for score in scores["score_rounds"]:
        print(f"Round {scores['score_rounds'].index(score) + 1}: {score} points")
    print(f"Total: {scores['total']} points")


def replay_menu():
    """
    Prompts the user to play again.
    :return:
    """

    print(SEPERATOR)
    choice = multiple_choice_menu("Play again?", ["Yes", "No"])
    return choice
