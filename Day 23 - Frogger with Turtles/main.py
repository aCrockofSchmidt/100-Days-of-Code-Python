import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
scoreboard = Scoreboard()
cars = CarManager()

screen.listen()
screen.onkeypress(player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()

    # create cars
    if random.choice([True, False, False, False, False, False]):
        cars.add_car()
    cars.car_move()


    # detect collision
    for car in cars.all_cars:
        if player.distance(car) < 20:
            scoreboard.game_over()
            game_is_on = False


    # detect top of screen
    if player.ycor() > 285:
        player.end_of_screen()
        scoreboard.scorekeeping()
        cars.increase_speed()

screen.exitonclick()




