from turtle import Turtle, Screen
import time

# Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")

# Pause Screen
screen.tracer(0)

# Segments List
squares_list = []

# Three Squares
x = 0
for square in range(3):
    new_square = Turtle(shape="square")
    new_square.color("white")
    new_square.penup()
    new_square.setx(x)
    x += 20
    squares_list.append(new_square)


def change_direction():
    if square.xcor() > 270:
        square.setheading(90)
    if square.ycor() > 270:
        square.setheading(180)
    if square.xcor() < -270:
        square.setheading(270)
    if square.ycor() < -270:
        square.setheading(360)


# Running Snake
game_on = True
while game_on:
    # Redraw Screen
    screen.update()
    time.sleep(0.1)
    # Move Squares Forward
    for square in squares_list:
        square.forward(20)
        # Change Direction


# Screen Exit
screen.exitonclick()