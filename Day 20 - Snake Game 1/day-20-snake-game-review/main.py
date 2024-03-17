from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard, GameOver
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game - Review")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(snake.up, "Up")
screen.onkeypress(snake.down, "Down")
screen.onkeypress(snake.left, "Left")
screen.onkeypress(snake.right, "Right")


game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        food.relocate()
        snake.add_tail()
        scoreboard.update_score()

    if abs(snake.head.xcor()) > 280 or abs(snake.head.ycor()) > 280:
        game_over = GameOver()
        game_on = False

    for segment in snake.segments_list:
        if segment == snake.head:
            pass
        else:
            if segment.distance(snake.head) < 10:
                game_over = GameOver()
                game_on = False


screen.mainloop()
