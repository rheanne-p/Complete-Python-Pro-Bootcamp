# Modules
from turtle import Turtle, Screen
from random import randint

# Screen Object
screen = Screen()
screen.setup(width=500, height=400)

# User Pop-up
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

# Lists
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
turtles = []

# Variables
race_ongoing = True

# Creating Turtles
y = -180
for turtle_no in range(0, 6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_no])
    new_turtle.penup()
    y += 50
    new_turtle.goto(x=-230, y=y)
    turtles.append(new_turtle)

# Racing Turtles
while race_ongoing:
    # Assign Random Speed
    for turtle in turtles:
        turtle.forward(randint(0, 10))
        # End Race
        if turtle.xcor() > 230:
            race_ongoing = False
            winners_color = turtle.pencolor()
            # Winner Message
            if user_bet == winners_color:
                print(f"You're right, the {winners_color} turtle won.")
            # Loser Message
            else:
                print(f"You're wrong, the {winners_color} turtle won.")

# Exit Screen
screen.exitonclick()
