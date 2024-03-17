from turtle import Turtle, Screen


# Method to Change Shape
timmy_the_turtle = Turtle()
timmy_the_turtle.shape("turtle")

# Rely on TK interface for GUI (graphical user interface)
timmy_the_turtle.color("aquamarine")

# Action Methods
timmy_the_turtle.forward(100)

# Faces East on Default
# Turn Right by 90 degrees
timmy_the_turtle.right(90)


# Create Screen Object
screen = Screen()
screen.exitonclick()