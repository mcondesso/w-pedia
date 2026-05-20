from enum import Enum

# --------------------------------
# GLOBALS
# --------------------------------

NUMBER_OF_ROUNDS = 3
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
    HISTORICAL = "historical"
    MILITARY = "military"


class WhereCategory(Enum):
    COUNTRIES = "countries"
    CITIES = "cities"


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
