from data import question_data
from question_model import Question
from quiz_brain import QuizBrain

question_bank = []
#i = 0

for question in question_data:
    question_text = question["text"]
    question_answer = question["answer"]
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)

#    print(question_bank[i].text)
#    print(question_bank[i].answer)

#    i += 1

quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"You're final score was: {quiz.score}/{quiz.question_number}")




