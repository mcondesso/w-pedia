import json
import os

from openai import OpenAI
from dotenv import load_dotenv


from globals import NUMBER_OF_API_TRIES


class AIError(Exception):
    """Base exception class for errors thrown by the ai module."""


class InvalidOutputError(AIError):
    """Thrown when the output from the openAI API is invalid."""


load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)


def validate_output(wiki_data: list[dict], quiz_data: list[dict]):
    if not quiz_data:
        raise InvalidOutputError()
    if len(wiki_data) != len(quiz_data):
        raise InvalidOutputError()
    answers = [output["answer"] for output in quiz_data]
    for input in wiki_data:
        if input["answer"] not in answers:
            raise InvalidOutputError()


def generate_quiz(wiki_data: list[dict]) -> list[dict] | None:
    instructions = (
        "You are generating quiz items from structured input. "
        "Return exactly valid JSON and nothing else. "
        "The response must be a JSON array with one object per input item. "
        "Each object must contain exactly these keys: "
        "`answer`, `hints`, `options`. "
        "`hints` must be an array of 3 anonymized clue strings. "
        "`options` must be an array of 3 plausible but incorrect answer strings. "
        "Do not include markdown, explanations, or extra fields."
    )

    prompt = (
        "Create a quiz for a guessing game.\n"
        "For each input entity, generate:\n"
        "1) `answer`: the entity name\n"
        "2) `hints`: 3 anonymized hints that help identify the entity without naming it\n"
        "3) `options`: 3 plausible incorrect choices that fit the hints but are not the answer\n\n"
        "Input data:\n"
        f"{json.dumps(wiki_data, ensure_ascii=False)}"
    )

    print("Generating quiz, please wait...")

    quiz = None
    for i in range(NUMBER_OF_API_TRIES):
        try:
            response = client.responses.create(
                model="gpt-5-nano",
                instructions=instructions,
                input=prompt,
            )
            quiz = json.loads(response.output_text)
            validate_output(wiki_data, quiz)
            break
        except Exception as error:
            print(f"Invalid response from OpenAI: {error}")
            if i < NUMBER_OF_API_TRIES - 1:
                print("Trying again...")
            else:
                raise InvalidOutputError()

    print("Quiz successfully generated!")
    return quiz
