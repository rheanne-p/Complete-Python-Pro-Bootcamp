from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard, Line

# Screen
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong Game - Built Myself")
screen.tracer(0)

# Paddle Objects
r_paddle = Paddle(370)
l_paddle = Paddle(-370)

# Ball Object
ball = Ball()

# Scoreboard Objects
scoreboard = ScoreBoard()
line = Line()
line.draw_line()

# Update Screen
screen.update()
screen.tracer(1)

# Paddle Controls
screen.listen()
screen.onkeypress(fun=r_paddle.up, key="Up")
screen.onkeypress(fun=r_paddle.down, key="Down")
screen.onkeypress(fun=l_paddle.up, key="w")
screen.onkeypress(fun=l_paddle.down, key="s")

# Running Game
game_on = True
while game_on:
    ball.move()

    # Detect collision with wall
    ball_y_cor = ball.ycor()
    if ball_y_cor > 280 or ball_y_cor < -280:
        ball.bounce()

    # Detect collision with paddle
    l_paddle_distance = l_paddle.distance(ball)
    r_paddle_distance = r_paddle.distance(ball)
    if l_paddle_distance < 50 or r_paddle_distance < 50:
        ball.paddle_bounce()
        ball.increase_speed()
        if l_paddle_distance < 50:
            screen.tracer(0)
            scoreboard.add_l_score()
            screen.tracer(1)
        if r_paddle_distance < 50:
            screen.tracer(0)
            scoreboard.add_r_score()
            screen.tracer(1)

    # Detect collision beyond paddle
    ball_x_cor = ball.xcor()
    if ball_x_cor > 380 or ball_x_cor < -380:
        screen.tracer(0)
        ball.home()
        screen.tracer(1)
        if ball_x_cor > 380:
            scoreboard.add_l_score()
        if ball_x_cor < -380:
            scoreboard.add_r_score()

# Screen Exit
screen.exitonclick()

