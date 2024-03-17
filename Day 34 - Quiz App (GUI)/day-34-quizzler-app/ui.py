from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")


class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz_brain = quiz_brain

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_label = Label(text="Score: 0", bg=THEME_COLOR, fg="white")
        self.score_label.grid(column=1, row=0)

        self.canvas = Canvas(width=300, height=250, bg="white", highlightthickness=0)
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            text="My question goes here",
            font=FONT,
            fill=THEME_COLOR

        )
        self.canvas.grid(column=0, row=1, columnspan=2, pady=20)

        check_img = PhotoImage(file="./images/true.png")
        self.check_button = Button(image=check_img, command=self.user_true, highlightthickness=0)
        self.check_button.grid(column=0, row=2)

        x_img = PhotoImage(file="./images/false.png")
        self.x_button = Button(image=x_img, command=self.user_false, highlightthickness=0)
        self.x_button.grid(column=1, row=2)
        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_label.config(text=f"Score: {self.quiz_brain.score}")
            q_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You've reached the end of the quiz!")
            self.check_button.config(state="disabled")
            self.x_button.config(state="disabled")

    def user_true(self):
        is_right = self.quiz_brain.check_answer(user_answer="True")
        self.give_feedback(is_right)

    def user_false(self):
        is_right = self.quiz_brain.check_answer(user_answer="False")
        self.give_feedback(is_right)

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)
