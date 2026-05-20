import random
from typing import Dict, List, Tuple
from colorama import Fore, Style, init, Back
from globals import GameMode, WhoCategory, CATEGORY_MAP

# Initialize colorama
init(autoreset=True)


INDENT = " " * 10
SEPERATOR = "<:>:" * 40
WARNING_SEPERATOR = "-<>-" * 20
NEXT_ROUND_SEPERATOR = "¸,ø¤°`°¤ø,¸" * 20
START_GAME_SEPERATOR = """
               (( _______
     _______     /\\O    O\\
    /O     /\\   /  \\      \\
   /   O  /O \\ / O  \\O____O\\ ))
((/_____O/    \\    /O     /
  \\O    O\\    / \\  /   O  /
   \\O    O\\ O/   \\/_____O/
    \\O____O\\/ )) mrf      ))
  ((

"""


BAD_EMOTE = "(x__x)     -     " * 3
NORMAL_EMOTE = "(o.o)     -     " * 3
GOOD_EMOTE = "(^-^)     -     " * 3

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
        player_name = input(
            f"\n{INDENT}What would you like to be addressed as: "
        ).strip()

        # Check if empty
        if not player_name:
            print(Fore.YELLOW + "Player name cannot be empty. Please try again!")
            continue

        # Check for numbers
        if any(char.isdigit() for char in player_name):
            print(Fore.YELLOW + "Player name cannot contain numbers. Please try again!")
            continue

        # check length between 3 and 12
        if len(player_name) <= 3 or len(player_name) >= 12:
            print(Fore.YELLOW + "Invalid name. use 3-12 letters only.")
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
        print(Fore.LIGHTMAGENTA_EX + f"\n{INDENT}{question}")

        i = 1
        for c in choices:
            print(f"{INDENT}{i}. {c}")
            i += 1

        input_str = input(Fore.LIGHTMAGENTA_EX + f"\n{INDENT}Enter your choice: ")

        try:
            input_chosen = int(input_str)

            # Validate range
            if 1 <= input_chosen <= len(choices):
                choice = choices[input_chosen - 1]
            else:
                raise ValueError()

        except ValueError:
            print(
                Fore.YELLOW + f"Please enter a number between 1 and {len(choices)}."
            )

    return choice


def get_game_mode_from_user():
    """
    Asks the user to choose a game mode.
    :return: A GameMode enum value.
    """

    game_modes = list(GameMode)

    mode_choice = multiple_choice_menu(
        "Which 'Mode' would you like to play today?",
        [mode.value.title() for mode in game_modes],
    )

    # Convert selected string back to enum
    game_mode = next(mode for mode in game_modes if mode.value.title() == mode_choice)

    print(Fore.BLUE + "Amazing choice!")
    print(Fore.BLUE + f"Welcome to {game_mode.value.title()} mode!")
    return game_mode


def get_category_from_user(game_mode: GameMode):
    """
    Ask the user to choose a category.
    :returns: A Category enum value matching the game mode.
    """

    categories = list(CATEGORY_MAP[game_mode])

    category_choice = multiple_choice_menu(
        "Which 'Category' would you like to play today?",
        [category.value.replace("_", " ").title() for category in categories],
    )

    # Convert selected string back to enum
    game_category = next(
        category
        for category in categories
        if category.value.replace("_", " ").title() == category_choice
    )

    print(Fore.BLUE + "\nAmazing choice!")
    print(Fore.BLUE + f"Welcome to {category_choice} Category!")
    return game_category


def show_welcome():
    """
    This function displays a welcome message.
    :return:
    """
    print(Back.BLUE + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + SEPERATOR)
    print(Style.BRIGHT + Fore.LIGHTMAGENTA_EX + "Welcome to W-Pedia".center(50))
    print(Back.BLUE + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + SEPERATOR)

    print(Fore.MAGENTA + "\nWhere curiosity turns into knowledge,")
    print(Fore.MAGENTA + "time turns into wisdom,")
    print(Fore.MAGENTA + "and learning becomes an unforgettable adventure.\n")


def show_menu():
    """

    :return:
    """

    choice = multiple_choice_menu(
        "Main Menu", ["Start the game", "Instructions", "Settings", "Quit"]
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

    print(Fore.BLUE + f"\nWelcome, {player_name}!")

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
# Functions for game.py
# -------------------------------------------


def main_menu():
    """Function called by game.py which returns the settings for the game."""

    show_welcome()
    game_settings = show_menu()

    print(Fore.LIGHTMAGENTA_EX + START_GAME_SEPERATOR)
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
        print(Fore.BLUE + f"You chose: {selected_answer}")
    except TypeError as e:
        display_error_message(e)
        return None

    return selected_answer


def display_new_round():
    """
    Displays the new round message.
    :return:
    """
    print(NEXT_ROUND_SEPERATOR)


def display_result_answer(is_correct: bool, points: int, answer: str):
    """
    displays the result of the round.
    """
    if is_correct:
        print(Fore.GREEN + "\n" + GOOD_EMOTE)
        print(Fore.GREEN + "Congratulations! You have completed a round!".center(50))
        print(Fore.GREEN + f"You earned {points} points.")
        print(Fore.GREEN + GOOD_EMOTE + "\n")
    elif is_correct is None:
        print(Fore.YELLOW + "\n" + NORMAL_EMOTE)
        print(Fore.YELLOW + "Try again, that was not correct....".center(50))
        print(Fore.YELLOW + NORMAL_EMOTE + "\n")
    else:
        print(Fore.LIGHTRED_EX + "\n" + BAD_EMOTE)
        print(
            Fore.LIGHTRED_EX
            + f"You have unfortunately exhausted all your tries! The answer was: {answer}".center(
                50
            )
        )
        print(Fore.LIGHTRED_EX + BAD_EMOTE + "\n")


def display_error_message(error_message: str):
    """
    Displays an error message and returns the user to the main menu.
    :param error_message:
    :return:
    """

    print(SEPERATOR)
    print(Fore.RED + "Oops! Something went wrong. ")

    print(Fore.YELLOW + WARNING_SEPERATOR)
    print(Fore.RED + f"Error: {error_message}")
    print(WARNING_SEPERATOR)

    print("We're working on it. Please try again!")
    print(SEPERATOR)


def prompt_display_leaderboard(leaderboard: List[Dict]):
    """Ask the user if they want to display the leaderboard."""

    print(Back.BLUE + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + SEPERATOR)
    choice = multiple_choice_menu("Show Leaderboard?", ["Yes", "No"])
    if choice == "Yes":
        display_leaderboard(leaderboard)
    elif choice == "No":
        return
    else:
        print("Invalid choice. Please enter Yes or No.")
        prompt_display_leaderboard(leaderboard)
    return


def display_leaderboard(leaderboard: List[Dict]):
    """Displays the leaderboard. Highscores of all time"""

    print(Back.BLUE + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + SEPERATOR)
    print(
        Style.BRIGHT
        + Fore.LIGHTMAGENTA_EX
        + "Congratulations! You have completed the game!".center(50)
    )
    print(Back.LIGHTYELLOW_EX + Style.BRIGHT + Fore.BLUE + SEPERATOR)

    print(Fore.LIGHTYELLOW_EX + LEADERBOARD_BANNER)

    print(Fore.MAGENTA + "-" * 50)
    print(
        Fore.MAGENTA + f"{'PLACE':<15}{'POINTS':>10}{'MAX ROUNDS':>10}{'MAX HINTS':>10}"
    )
    print(Fore.MAGENTA + "-" * 50)

    if not leaderboard:
        print(Fore.MAGENTA + "No scores yet...")
    else:
        for i, entry in enumerate(leaderboard, start=1):

            player = entry.get("player", "-")
            score = entry.get("score", 0)
            rounds = entry.get("number_of_rounds", 0)
            hints = entry.get("hints_per_round", 0)

            print(Fore.MAGENTA + f"{i:<8}{player:<15}{score:>8}{rounds:>10}{hints:>10}")

    print(Fore.MAGENTA + "-" * 50)


def display_end_of_game(scores):
    """
    Displays the end of the game message.

    scores: {player_name: str, score_rounds: [int,int,int], total: [int]}
    """

    print(Back.BLUE + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + SEPERATOR)
    print(
        Style.BRIGHT
        + Fore.LIGHTMAGENTA_EX
        + "Congratulations! You have completed the game!".center(50)
    )
    print(Back.BLUE + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + SEPERATOR)

    print(Fore.CYAN + f"\nPlayer : {scores['player_name']}\n")

    print(Fore.CYAN + "-" * 30)
    print(Fore.CYAN + f"{'ROUND':<15}{'POINTS':>10}")
    print(Fore.CYAN + "-" * 30)

    for i, score in enumerate(scores["score_rounds"], start=1):
        print(Fore.CYAN + f"{f'Round {i}':<15}{score:>10}")

    print(Fore.CYAN + "-" * 30)
    print(Fore.CYAN + f"{'TOTAL':<15}{scores['total']:>10}")
    print(Fore.CYAN + "-" * 30)


def replay_menu():
    """
    Prompts the user to play again.
    :return:
    """

    print(Back.BLUE + Style.BRIGHT + Fore.LIGHTMAGENTA_EX + SEPERATOR)
    choice = multiple_choice_menu("Play again?", ["Yes", "No"])
    return choice
