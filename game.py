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
