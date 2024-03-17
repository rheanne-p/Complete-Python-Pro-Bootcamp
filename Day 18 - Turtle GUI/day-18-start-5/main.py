# Modules
import turtle
from turtle import Turtle, Screen
from data import COLORS
import random

# Turtle Object
timmy = Turtle()
timmy.pensize(15)
timmy.speed("fastest")


# Variables
directions = [0, 90, 180, 270]

# Change colormode of turtle to 255
# tap directly into turtle module
turtle.colormode(255)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    random_color_tuple = (r, g, b)
    return random_color_tuple


# Walking
for _ in range(200):
    timmy.forward(50)
    timmy.setheading(random.choice(directions))
    timmy.pencolor(random_color())
    # timmy.pencolor(random.choice(COLORS))


# Screen Object
my_screen = Screen()
my_screen.exitonclick()

