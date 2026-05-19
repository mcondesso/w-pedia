import json
import os

from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(
    # This is the default and can be omitted
    api_key=os.environ.get("OPENAI_API_KEY"),
)

title = "Michael Jordan"
summary = """Michael Jeffrey Jordan (born February 17, 1963), also known by his initials MJ,[8]
is an American businessman and retired professional basketball player who is a minority owner
of the Charlotte Hornets of the National Basketball Association (NBA)"""


def generate_quiz(wiki_data):

    instructions = (
        "Please format the response into a list of dictionaries with: a list of 3 hints, "
        "a list of 3 fake options and the solution (which is just the input title)." \
        "The response list should contain one dictionary per input (title, summary) pair." \
        "Each dictionary contains only the keys 'solution', 'hints', 'fake_options'."
    )

    prompt = (
        "I am creating a quizz game where the player should guess an entity based on "
        "anonymized hints. For each pair of title and summary, please generate:"
        "- a list with 3 anonymized hints for the player to guess. Each hint should add information,"
        "but not make it obvious."
        "- a list with 3 fake options, that could potentially fit the information in the hint, but "
        "not match exactly, to challenge the player, but not make it impossible."
        f"Input data: {wiki_data}"
    )

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
    if len(wiki_data) != len(quiz):
        print("Invalid response from OpenAI")
        return None
    solutions = [output["solution"] for output in quiz]
    for input in wiki_data:
        if input["name"] not in solutions:
            print("Invalid response from OpenAI")
            return None
    
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
