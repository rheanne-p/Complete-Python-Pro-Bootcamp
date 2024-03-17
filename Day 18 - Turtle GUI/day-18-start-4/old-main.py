from turtle import Turtle, Screen
from tkinterlist import COLORS
import random

# Attributes
timmy = Turtle()
timmy.pensize(10)


# Random Color
def random_color():
    random_tkinter_color = random.choice(COLORS)
    timmy.pencolor(random_tkinter_color)


# Square
random_color()
for _ in range(4):
    timmy.forward(100)
    timmy.right(90)

# Pentagon
random_color()
for _ in range(5):
    timmy.forward(100)
    timmy.right(72)

# Hexagon
random_color()
for _ in range(6):
    timmy.forward(100)
    timmy.right(60)

# Heptagon
random_color()
for _ in range(7):
    timmy.forward(100)
    timmy.right(360/7)

# Octagon
random_color()
for _ in range(8):
    timmy.forward(100)
    timmy.right(45)

# Nonagon
random_color()
for _ in range(9):
    timmy.forward(100)
    timmy.right(40)

# Decagon
random_color()
for _ in range(10):
    timmy.forward(100)
    timmy.right(36)

# Show Screen
screen = Screen()
screen.exitonclick()