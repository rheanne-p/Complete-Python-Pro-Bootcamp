import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

# TODO 1. Create Turtle Player
player = Player()
screen.listen()
screen.onkey(fun=player.up, key="Up")

# TODO 5. Create a scoreboard
scoreboard = Scoreboard()

game_is_on = True
cars_list = []
loop_count = 0
move_increment = 5

while game_is_on:
    loop_count += 1
    time.sleep(0.1)
    screen.update()

    # TODO 2. Create cars
    if loop_count % 6 == 0:
        new_car = CarManager()
        cars_list.append(new_car)

    # TODO 3. Detect collision with car
    for car in cars_list:
        car.move(move_increment)
        if player.distance(car) < 20:
            game_is_on = False
            scoreboard.game_over()

    # TODO 4. Detect if turtle reached top
    if player.ycor() > 280:
        player.return_start()
        # for car in cars_list:
        #     car.increase_speed()
        move_increment += 10
        scoreboard.level_up()

screen.exitonclick()
