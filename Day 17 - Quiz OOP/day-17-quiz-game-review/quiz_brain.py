# Quiz Brain Class
class QuizBrain:
    # Quiz Brain Object
    def __init__(self, question_list):
        self.question_number = 0
        self.question_list = question_list
        self.score = 0

    # Still Has Questions Method
    def still_has_questions(self):
        return self.question_number < len(self.question_list)

    # Next Question Method
    def next_question(self):
        current_object = self.question_list[self.question_number]
        current_object_text = current_object.text
        current_object_answer = current_object.answer
        self.question_number += 1
        user_answer = input(f"Q.{self.question_number}: {current_object_text} (True/False)?: ")
        self.check_answer(user_answer, current_object_answer)

    # Check Answer Method
    def check_answer(self, user_answer, current_object_answer):
        if user_answer.lower() == current_object_answer.lower():
            print("You got it right!")
            self.score += 1
        else:
            print("You got it wrong.")
            print(f"The correct answer was: {current_object_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}")
        print("\n")
