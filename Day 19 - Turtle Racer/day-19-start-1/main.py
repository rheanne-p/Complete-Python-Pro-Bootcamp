from turtle import Turtle, Screen

# Turtle Object
tim = Turtle()

# Screen Object: controls window
screen = Screen()
screen.exitonclick()


# Move Forwards Function for Event Listener
def move_forwards():
    tim.forward(10)


# Start Listening for Events
screen.listen()

# Bind a keystroke (action) to an event (function)
# Use an event listener
# Parameters: function, key
screen.onkey(key="space", fun=move_forwards)

# Function as an argument: don't include parentheses at end
# Only pass in name
# Parentheses triggers function
# Want method to listen to space bar, THEN trigger function