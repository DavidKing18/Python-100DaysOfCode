from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.right, "r")

game_is_on = True
count = 1


def game_reset():
    global count
    scoreboard.reset()
    snake.reset()
    food.refresh()
    count = 1


while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    scoreboard.show_score()
    x_boundary = snake.head.xcor()
    y_boundary = snake.head.ycor()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        # Big Bonus every five eat.
        if count % 5 == 0:
            scoreboard.bonus_score()
        if (count + 1) % 5 == 0:
            food.bonus()
            scoreboard.increase_score()
        else:
            food.refresh()
            scoreboard.increase_score()
        snake.extend()
        count += 1
    # Detect Collision with wall.
    if (x_boundary > 300 or x_boundary < -300) or (y_boundary > 300 or y_boundary < -300):
        game_reset()

    # Detect collision with tail.
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_reset()

screen.exitonclick()
