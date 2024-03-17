from turtle import Turtle, Screen
from tkinterlist import COLORS
import random

# Attributes & Variables
timmy = Turtle()
timmy.pensize(20)
sides = 4


# Random Color
def random_color():
    random_tkinter_color = random.choice(COLORS)
    timmy.pencolor(random_tkinter_color)


# Drawing Loop
for _ in range(10):
    random_color()
    for _ in range(sides):
        timmy.forward(100)
        timmy.right(360 / sides)
    sides += 1

# Show Screen
screen = Screen()
screen.exitonclick()