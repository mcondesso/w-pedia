# Main game loop, calling the appropriate functions from menu.py at each stage
# Track player score
# Show final score and option to replay
import quiz_handler as handler

def run():


    #handle questions replace with class methods later
    quiz = handler.question_handler(mode="who")
    print(quiz)
    quiz = quiz[0]
    print(quiz["question"][0])

    #handle hints and answers
    print(f"answer is {quiz['answer']}")

    # call scoring return a result dictionary
    print("Your score is XXX")
    quiz_results = {}

    #get final menu
    return quiz_results