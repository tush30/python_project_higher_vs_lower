from data import question_data
from question_model import Question
from quiz_brain import Quiz_Brain
question_bank = []
for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

quiz = Quiz_Brain(question_bank)

while quiz.still_has_question():
    quiz.next_qustion()
print("you've completed the quiz")
print(f"your final score was: {quiz.score}/{quiz.question_no}")