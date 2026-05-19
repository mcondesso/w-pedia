from game import GameMode, WhoCategory

def get_player_name():
    """
    Gets the name of the player from the user.
    """

    #TODO! validate player name!
    player_name = input("\nWhat would you like to be adddressed as: ")
    return player_name

def multiple_choice_menu(question: str, choices: List[str]):
    """

    :param choices: Defines the multiple choice options
    :return:
    """
    choice = None
    while not choice:
        print(question)

        i=1
        for c in choices:
            print(f"{i}. {c}")
            i +=1

        input_str = input("\nEnter your choice: ")
        #TODO! check the input_chosen it should not be larger or smaller than the choices list length.

        try:
            input_chosen = int(input_str)
            choice = choices[input_chosen - 1]
        except ValueError as e:
            print(f"Could not convert your option to an integer, try again! \n {e}")


    return choice


def show_welcome():
    """
    This function displays a welcome message.
    :return:
    """
    print("=" * 50)
    print("Welcome to W-Pedia".center(50))
    print("=" * 50)


    player_name = get_player_name()

    print(f"\nWelcome, {player_name}!")

    print("\nWhere curiosity turns into knowledge,")
    print("time turns into wisdome,")
    print("and lerning becommes an unforgetable adventure.\n")



def show_menu():
    """

    :return:
    """

    choice = multiple_choice_menu( "\nMain Menu", ["Start the game", "Instructions", "Settings", "Quit"])



    if choice == "Start the game":
        game_mode, game_category, number_of_players = start_game()
        return game_mode, game_category, number_of_players

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

        #TODO! make a quit_game() function or use quit_game() from game.py

    else:

        print("\nInvalid choice.")
        print("Please enter 1, 2, 3, or 4.")



def start_game():

    #set game_mode

    # TODO! VERA will edit enumerators for Mode and Category
    mode_choice = multiple_choice_menu("\nWhich 'Mode' would you like to play today? ",["who", "what", "where", "when"])
    game_mode = GameMode.WHO #hard coded for now
    print("\nAmazing choice!")
    print(f"Welcome to {mode_choice} mode!")


    #set game category
    category_choice= multiple_choice_menu("\nWhich 'Category' would you like to play today? ",["sports", "influential"])
    game_category = WhoCategory.SPORTS #hard coded for now
    print("\nAmazing choice!")
    print(f"Welcome to {category_choice} Category!")

    # set number of players
    number_of_players = 1
    return game_mode, game_category, number_of_players

def randomize_options(answer, options):
    pass
# -------------------------------------------
# Functions for GAME
# -------------------------------------------

def main_menu():
    """Function called by game.py which returns the settings for the game."""

    show_welcome()
    game_mode, game_category, number_of_players = show_menu()

    game_mode = "who"
    game_category = "sports"
    number_of_players = 1

    game_settings = {"mode":game_mode, "category":game_category, "players":number_of_players}

    return game_settings

def display_question(question, answer, options):
    """
    Displays a given question with multiple choice options in the menu.
    :param question:
    :param answer:
    :param options:
    :return: string with the chosen answer or option
    """

    # choices = [answer, options[0], options[2], options[1]]
    choices = randomize_options(answer, options)
    answer = multiple_choice_menu(question, choices)

    return answer



main_menu()