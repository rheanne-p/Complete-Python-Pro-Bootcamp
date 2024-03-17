from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")  # shape method is directly from the Turtle class
        self.penup()
        self.shapesize(0.5, 0.5)  # 10 x 10 circle, parameters are stretch_len
        self.color("red2")
        self.speed("fastest")  # don't have to see food moving to location
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(x=random_x, y=random_y)
