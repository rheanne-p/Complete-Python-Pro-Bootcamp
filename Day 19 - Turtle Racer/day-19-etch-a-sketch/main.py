from turtle import Turtle, Screen

# Turtle Object
tim = Turtle()

# Screen Object
screen = Screen()
screen.listen()


# Turtle Key Functions
def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def rotate_counter_clockwise():
    tim.left(10)


def rotate_clockwise():
    tim.right(10)


def clear_screen():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


# Function and Keystroke Binds
screen.onkeypress(fun=move_forwards, key="w")
screen.onkeypress(fun=move_backwards, key="s")
screen.onkeypress(fun=rotate_counter_clockwise, key="a")
screen.onkeypress(fun=rotate_clockwise, key="d")
screen.onkeypress(fun=clear_screen, key="c")

# Screen Exit on Click
screen.exitonclick()
