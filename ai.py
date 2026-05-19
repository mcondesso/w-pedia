import os

# from openai import OpenAI
#
# client = OpenAI(
#     # This is the default and can be omitted
#     api_key=os.environ.get("OPENAI_API_KEY"),
# )

title = "Michael Jordan"
summary = """Michael Jeffrey Jordan (born February 17, 1963), also known by his initials MJ,[8]
 is an American businessman and retired professional basketball player who is a minority owner
 of the Charlotte Hornets of the National Basketball Association (NBA)"""

prompt = "I am creating a quizz game where the player should guess the celebrity based on " \
    "anonymized hints. Please generate:" \
    "- a list with 3 anonymized hints for the player to guess. Each hint should add information," \
    "but not make it obvious." \
    "- a list with 3 fake options, that could potentially fit the information in the hint, but " \
    "don't quite match exactly." \
    f"So, title: {title} and {summary}"

# response = client.responses.create(
#     model="gpt-5-nano",
#     instructions="Please format the response into: a dictionary with: a "\
#         "list of 3 hints and a list of 3 fake options.",
#     input=prompt,
# )