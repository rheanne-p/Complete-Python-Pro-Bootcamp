from turtle import Turtle

class Line(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.setheading(90)
        self.penup()
        self.sety(-280)
        self.pensize(5)
        for _ in range(30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)