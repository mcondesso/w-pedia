# Hardcoded lists with wikipedia URLs of people for each category
# Game Modes : Who, What, Where, When?
# generates questions, answers 

def question_handler(mode="who"):
    quiz = []

    round = {}
    if mode == "who":
        question = ["Famous Wizard?", "Sometimes he's grey, sometimes he's white.", "Lord of the rings?"]
        answer = "Gandalf"
        options = ["Frodo", "Sam", "Smeagol"]

        round["question"] = question
        round["answer"] = answer
        round["options"] = options
    quiz.append(round)
    return quiz


# 
