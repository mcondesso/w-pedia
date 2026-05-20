from enum import Enum

# --------------------------------
# GLOBALS
# --------------------------------

NUMBER_OF_ROUNDS = 2
NUMBER_OF_HINTS = 3
NUMBER_OF_API_TRIES = 3


class GameMode(Enum):
    """
    This enumerator sets the mode in which the game will be played.
    """

    WHO = "who"
    WHAT = "what"
    WHERE = "where"
    # WHEN = "when"


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
    # GameMode.WHEN: WhenCategory,
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
