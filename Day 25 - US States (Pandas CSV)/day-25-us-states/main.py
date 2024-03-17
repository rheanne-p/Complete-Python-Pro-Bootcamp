import turtle
from turtle import Turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

writer = Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_states.csv")
states_list = data["state"].to_list()
answers_list = []

# TODO 1. Convert the guess to Title case
answer_state = screen.textinput(title="Guess the State", prompt="What's another state's name?").title()

# TODO 4. Use a loop to allow the user to keep guessing
while len(answers_list) < 50:

    # TODO 2. Check if the guess is among the 50 states
    if answer_state == "Exit":
        break

    elif answer_state in answers_list or answer_state not in states_list:
        answer_state = screen.textinput(title=f"{len(answers_list)}/50 States Correct", prompt="What's another state's name?").title()

    else:
        # TODO 3. Write correct guesses onto the map
        answer_row = data[data.state == answer_state]
        writer.goto(int(answer_row.x), int(answer_row.y))
        writer.write(arg=answer_state, align="center", font=("Arial", 10, "normal"))

        # TODO 5. Record the correct guesses in a list
        answers_list.append(answer_state)

        # TODO 6. Keep track of the score
        score = len(answers_list)
        answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?").title()


# TODO 7. Save the missing states to a .csv
missing_list = []

for state in states_list:
    if state not in answers_list:
        missing_list.append(state)

missing_df = pandas.DataFrame(missing_list)
missing_df.to_csv("missed_states.csv")
