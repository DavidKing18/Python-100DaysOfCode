import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)

player = Player()
car = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(player.go_up, "Up")
screen.onkeypress(player.move_left, "w")
screen.onkeypress(player.move_right, "e")
screen.onkeypress(player.go_down, "Down")

cars = [car]
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    for car in cars:
        car.move_car()
    if random.randint(1, 6) == 1:
        cars.append(CarManager())

    # Detect collision with car
    for car in cars:
        if car.distance(player) < 20:
            scoreboard.game_over()
            game_is_on = False

    # Detect successful cross
    if player.ycor() > 280:
        player.reset()
        scoreboard.current_level()
        for car in cars:
            car.increase_speed()

screen.exitonclick()
