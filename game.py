# Main game loop, calling the appropriate functions from menu.py at each stage
# Track player score
# Show final score and option to replay
# import quiz_handler as handler
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

questions = [
    {
        "answer": "Apollo 11",
        "clue1": "A historic event from 1969.",
        "clue2": "A spaceflight mission that landed the first two humans on the Moon.",
        "clue3": "The mission where Neil Armstrong said, 'One small step for man...'",
    },
]
def get_points(attempt):
    """
    Takes in the attempt number (1, 2, or 3)
    Args:
        attempt:

    Returns: The corresponding points (5, 3, 1)
    """

    #creating a dictionary of attempt numbers matched to points
    attempts = {attempt_1 : 5, attempt_2 : 3, attempt_3 : 1}


def play_round(question, data):
    """
    Handles the logic for a single round (the 3-try loop).
    Args:
        question:
        data:

    Returns: score earned in round

    """
    pass

def start_game():
    """
    The main entry point. Runs the round loop, tracks total_score, and calls the final scoreboard.
    Returns: total_score

    """
    pass

def show_scoreboard():
    """
    Formats and prints the final total_score

    Returns:total_score formatted

    """
    pass


def run():

    # handle questions replace it with class methods later
    quiz = handler.question_handler(mode="who")
    print(quiz)
    quiz = quiz[0]
    print(quiz["question"][0])

    # handle hints and answers
    print(f"answer is {quiz['answer']}")

    # call scoring return a result dictionary
    print("Your score is XXX")
    quiz_results = {}

    # get final menu
    return quiz_results


print("Hello World!")
