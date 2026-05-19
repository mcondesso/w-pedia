import json
import os

from openai import OpenAI
from dotenv import load_dotenv


class AIError(Exception):
    """Base exception class for errors thrown by the ai module."""


class InvalidInputError(AIError):
    """Thrown when the input to generate the quiz is invalid."""


class InvalidOutputError(AIError):
    """Thrown when the output from the openAI API is invalid."""


load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

title = "Michael Jordan"
summary = """Michael Jeffrey Jordan (born February 17, 1963), also known by his initials MJ,[8]
is an American businessman and retired professional basketball player who is a minority owner
of the Charlotte Hornets of the National Basketball Association (NBA)"""


def validate_input(wiki_data: list[dict]):
    for entry in wiki_data:
        if not entry.get("name", "") or not entry.get("summary", ""):
            raise InvalidInputError()


def validate_output(wiki_data: list[dict], quiz_data: list[dict]):
    if len(wiki_data) != len(quiz_data):
        raise InvalidOutputError()
    solutions = [output["solution"] for output in quiz_data]
    for input in wiki_data:
        if input["name"] not in solutions:
            raise InvalidOutputError()


def generate_quiz(wiki_data: list[dict]) -> list[dict] | None:
    validate_input(wiki_data)

    instructions = (
        "You are generating quiz items from structured input. "
        "Return exactly valid JSON and nothing else. "
        "The response must be a JSON array with one object per input item. "
        "Each object must contain exactly these keys: "
        "`solution`, `hints`, `fake_options`. "
        "`hints` must be an array of 3 anonymized clue strings. "
        "`fake_options` must be an array of 3 plausible but incorrect answer strings. "
        "Do not include markdown, explanations, or extra fields."
    )

    prompt = (
        "Create a quiz for a guessing game.\n"
        "For each input entity, generate:\n"
        "1) `solution`: the entity name\n"
        "2) `hints`: 3 anonymized hints that help identify the entity without naming it\n"
        "3) `fake_options`: 3 plausible incorrect choices that fit the hints but are not the solution\n\n"
        "Input data:\n"
        f"{json.dumps(wiki_data, ensure_ascii=False)}"
    )

    print("Generating quiz, please wait...")

    try:
        response = client.responses.create(
            model="gpt-5-nano",
            instructions=instructions,
            input=prompt,
        )
    except Exception as error:
        print(f"Invalid response from OpenAI: {error}")
        return None

    try:
        quiz = json.loads(response.output_text)
    except Exception as error:
        print(f"Error parsing reply from OpenAI: {error}")
        return None

    # Validate response from OpenAI
    validate_output(wiki_data, quiz)

    return quiz


wiki_data = [
    {
        "name": "Gandalf",
        "summary": "Gandalf is a Wizard from Lord of the Rings. "
        "He is one of the main protagonists of the book/film series.",
    },
    {
        "name": "Mickey Mouse",
        "summary": "He loves Minie Mouse and is a silly mouse.",
    },
]

quiz = generate_quiz(wiki_data)
print(quiz)
