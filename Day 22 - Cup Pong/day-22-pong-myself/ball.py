from turtle import Turtle
import random


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.input_speed = 1.5
        self.x_move = 5
        self.y_move = 5
        self.speed(self.input_speed)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1

    def increase_speed(self):
        self.x_move *= 1.2
        self.y_move *= 1.2