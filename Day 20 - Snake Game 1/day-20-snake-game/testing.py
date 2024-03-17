from turtle import Turtle, Screen
import time

# Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Testing Snake Game")
# Turn off tracer (screen won't update until screen.update() gets called)

# Segments List
squares_list = []
starting_positions = [(0, 0), (-20, 0), (-40, 0)]

# Three Squares
x = 0
for position in starting_positions:
    new_square = Turtle(shape="square")
    new_square.color("white")
    new_square.penup()
    new_square.goto(position)
    squares_list.append(new_square)

# Running Snake
game_on = True
while game_on:
    # Redraw Screen
    # Move Squares Forward
    for square in squares_list:
        print(squares_list[square])
        print(square.pos())
        square.forward(20)
        if square.xcor() > 280:
            game_on = False

# Screen Exit
screen.exitonclick()