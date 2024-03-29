from question_model import Question
from data import question_data
from quiz_brain import QuizBrain
question_bank = []

for i in question_data:
    new_question = Question(
        i["text"], i['answer'])
    question_bank.append(new_question)


quiz = QuizBrain(question_bank)

while quiz.still_has_question():

    quiz.next_question()

print("!!!!You have completed the Quiz!!!!")
print(f"Your final score is {quiz.score}/{quiz.question_number}")
