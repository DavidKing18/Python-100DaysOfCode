from turtle import Screen
from paddle import Paddle, CenterLines
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title('Pong')
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()
center_line = CenterLines()

screen.listen()
screen.onkeypress(r_paddle.move_up, 'Up')
screen.onkeypress(r_paddle.move_down, 'Down')
screen.onkeypress(l_paddle.move_up, 'w')
screen.onkeypress(l_paddle.move_down, 's')

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall and bounce
    if (ball.ycor() >= 290) or (ball.ycor() <= -290):
        ball.bounce_y()

    # Detect collision with right paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 320) or (ball.distance(l_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()

    # Detect if right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

    if (scoreboard.l_score > 6) or (scoreboard.r_score > 6):
        game_is_on = False
        if scoreboard.l_score > scoreboard.r_score:
            winner = 'Player 1'
        else:
            winner = 'Player 2'
        scoreboard.call_winner(winner)

screen.exitonclick()
