from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Question Bank
question_bank = []
for each_object in question_data:
    object_text = each_object["question"]
    object_answer = each_object["correct_answer"]
    new_object = Question(object_text, object_answer)
    question_bank.append(new_object)

# Quiz Object
quiz = QuizBrain(question_bank)

# Running Quiz
while quiz.still_has_questions():
    quiz.next_question()

print("You've completed the quiz.")
print(f"Your final score is: {quiz.score}/{len(question_bank)}")
