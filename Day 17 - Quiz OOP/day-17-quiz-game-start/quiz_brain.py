# TODO 3.1: Create a class called QuizBrain
class QuizBrain:
    # TODO 3.2: Write an __init__() method
    def __init__(self, q_list):
        # TODO 3.3: Initialize the question_number to 0
        self.question_number = 0
        # TODO 3.4: Initialize the question_list ot an input
        self.question_list = q_list

    # TODO 3.5: Create a method called next_question()
    def next_question(self):
        # TODO 3.6: Retrieve the item at the current question_number
        #  from the question_list
        self.current_question = self.question_list[self.question_number]
        self.question_number += 1
        current_question_text = self.current_question.text
        # TODO 3.7: Use the input() function to show the user
        #  the Question text and ask for the user's answer
        input(f"Q.{self.question_number + 1}: {current_question_text} (True/False)?: ")