from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game Retry")

screen.tracer(0)

squares_list = []

x = 0
for square in range(3):
    new_square = Turtle(shape="square")
    new_square.color("white")
    new_square.penup()
    new_square.setx(x)
    x += 20
    squares_list.append(new_square)

screen.update()

game_on = True
while game_on:
    for square in squares_list:
        square.forward(20)

screen.exitonclick()