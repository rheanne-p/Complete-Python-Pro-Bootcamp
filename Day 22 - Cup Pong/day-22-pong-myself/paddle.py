from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, x_cor):
        super().__init__()
        self.speed("fastest")
        self.setheading(90)
        self.setx(x_cor)
        self.shape("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=4)

    def up(self):
        if self.ycor() < 240:
            self.forward(20)

    def down(self):
        if self.ycor() > -240:
            self.backward(20)

