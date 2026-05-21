# Hardcoded lists with wikipedia URLs of people for each category
# Game Modes : Who, What, Where, When?
# generates questions, answers
from abc import ABC, abstractmethod
from enum import Enum


from src.wikipedia_scraper import get_random_wiki_data, WikipediaError
from src.ai import generate_quiz, AIError
from src.globals import (
    GameMode,
    WhoCategory,
    WhatCategory,
    WhereCategory,
    WhenCategory,
    CATEGORY_MAP,
)

class QuizHandlerError(Exception):
    """Base exception class for errors thrown by the Quiz Handler module."""


class BaseQuizHandler(ABC):
    game_mode: GameMode = None

    def __init__(self, game_category: Enum):
        self.game_category = game_category

    def generate_quiz(self):
        self.validate()

        try:
            wiki_data = get_random_wiki_data(
                mode=self.game_mode, category=self.game_category.value
            )
        except WikipediaError as error:
            raise QuizHandlerError from error

        try:
            quiz = generate_quiz(wiki_data)
        except AIError as error:
            raise QuizHandlerError from error

        # implement class specific processing , maybe for scoring?
        self.process()
        return quiz

    def validate(self):
        if self.game_mode is None:
            raise NotImplementedError(
                "Game mode is not set. Handler must define game_mode."
            )

    @abstractmethod
    def process(self):
        pass


class WhoHandler(BaseQuizHandler):
    game_mode = GameMode.WHO

    def process(self):
        pass


class WhatHandler(BaseQuizHandler):
    game_mode = GameMode.WHAT

    def process(self):
        pass


class WhereHandler(BaseQuizHandler):
    game_mode = GameMode.WHERE

    def process(self):
        pass


# class WhenHandler(BaseQuizHandler):
#     game_mode = GameMode.WHEN
#
#     def process(self):
#         pass


HANDLER_MAP = {
    GameMode.WHO: WhoHandler,
    GameMode.WHAT: WhatHandler,
    GameMode.WHERE: WhereHandler,
    # GameMode.WHEN: WhenHandler,
}


class QuizHandler:
    @staticmethod
    def handle_quiz(mode: GameMode, game_category: Enum):

        # validate mode and category
        if mode not in HANDLER_MAP:
            raise ValueError(f"Invalid mode: {mode}")

        expected_category_enum = CATEGORY_MAP[mode]

        if not isinstance(game_category, expected_category_enum):
            raise ValueError(
                f"Invalid category '{game_category}' for mode '{mode.value}'"
            )

        handler_cls = HANDLER_MAP[mode]
        handler = handler_cls(game_category=game_category)
        return handler


# --------------------------------
# TMP RUN
# --------------------------------


def tmp_run():

    # handle questions replace with class methods later
    handler = QuizHandler.handle_quiz(
        mode=GameMode.WHO, game_category=WhoCategory.SPORTS
    )
    quiz = handler.generate_quiz()
    print(quiz[0]["hints"][0])
    # handle hints and answers
    print(f"answer is {quiz[0]['answer']}")

    # call scoring return a result dictionary
    print("Your score is XXX")
    quiz_results = {10, 5, 2}

    # get final menu
    return quiz_results


# tmp_run()
