# Python Higher Order Functions & Event listeners

from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(9)


screen.listen()
screen.onkey(key='space', fun=move_forwards)
screen.exitonclick()

# Object State and Instances

timmy = Turtle()
teddy = Turtle()
timmy.color('blue')
teddy.color('red')


