# Take in user input, show game mode menu, category menu
import quiz_handler
import game

def main_menu():

    print("Welcome to the menu")
    print(" You have chosen the WHO is it game mode.")
    print("Generating questions...")
    results = game.run()
    print(f"The results are: {results}")




def get_user_input():
    pass

def choose_game_mode():
    pass

def choose_quiz_category():
    """historical, famous, etc"""
    pass