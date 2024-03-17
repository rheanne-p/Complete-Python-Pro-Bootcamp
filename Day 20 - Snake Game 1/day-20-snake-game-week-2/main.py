from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import ScoreBoard
import time

# Screen Object
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("sea green")
screen.title("Snake Game - Week 2")
screen.tracer(0)  # Pause Screen

# Objects
snake = Snake()
food = Food()
scoreboard = ScoreBoard()

# Keystrokes
screen.listen()
screen.onkey(fun=snake.up, key="Up")
screen.onkey(fun=snake.down, key="Down")
screen.onkey(fun=snake.left, key="Left")
screen.onkey(fun=snake.right, key="Right")

# Run Game
game_is_on = True
while game_is_on:
    screen.update()  # Screen updates every 0.1 second
    time.sleep(0.1)  # Works with update method
    snake.move()

    # Detect collision with food
    if snake.head.distance(food) < 15:  # snake head within 15 pixels of food
        food.refresh()
        snake.extend()
        scoreboard.increase_score()

    # Detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -300 or snake.head.ycor() > 300 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()

    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 3:
            pass
        elif snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()

# Screen Exit
screen.exitonclick()
