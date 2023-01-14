# Challenge - Etch-A-Sketch App

from turtle import Turtle, Screen

ted = Turtle()
screen = Screen()


def move_forward():
    ted.forward(10)


def move_backward():
    ted.backward(10)


def turn_counter_clockwise():
    ted.left(10)


def turn_clockwise():
    ted.right(10)


def clear_drawing():
    ted.clear()
    ted.penup()
    ted.goto(0, 0)  # OR ted.home()
    ted.pendown()


screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_backward)
screen.onkey(key="a", fun=turn_counter_clockwise)
screen.onkey(key="d", fun=turn_clockwise)
screen.onkey(key="c", fun=clear_drawing)
screen.exitonclick()