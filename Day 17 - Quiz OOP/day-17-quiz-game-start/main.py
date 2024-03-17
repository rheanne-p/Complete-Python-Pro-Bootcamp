from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

# Make a question_bank list of all the Question objects
question_bank = []

# TODO 2.1: Write a for loop to iterate over the question_data
for dictionary_entry in question_data:
    q_text = dictionary_entry["text"]
    q_answer = dictionary_entry["answer"]
    # TODO 2.2: Create a Question object from each entry in question_data
    question_object_entry = Question(q_text, q_answer)
    # TODO 2.3: Append each Question object to the question_bank
    question_bank.append(question_object_entry)

quiz = QuizBrain(question_bank)
quiz.next_question()

# Left off at Part 4, keep looping questions for user to answer...
