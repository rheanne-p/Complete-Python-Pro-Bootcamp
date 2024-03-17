from turtle import Turtle, Screen
from data import COLORS
import random

# Turtle Object
timmy = Turtle()
timmy.speed("fastest")
timmy.pensize(5)

# Angle & Cycle Variables
angle = 0
angle_increments = 10
cycles = int(360 / angle_increments)

# Drawing Circles
for number in range(cycles):
    timmy.setheading(angle)
    timmy.circle(100)
    timmy.pencolor(random.choice(COLORS))
    angle += angle_increments

# Screen Object
screen = Screen()
screen.exitonclick()
