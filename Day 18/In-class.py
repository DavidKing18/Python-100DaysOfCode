# # UNDERSTANDING TURTLE GRAPHICS AND HOW TO USE THE DOCUMENTATION
# from turtle import Turtle, Screen
#
# tim = Turtle()
# # tim.shape('turtle')
# # tim.color('black')
# # tim.forward(100)
# # tim.right(90)
#
#
# # Turtle Challenge 1 - Draw a Square
# for i in range(4):
#     tim.forward(100)
#     tim.right(90)
#
#
# # Importing Modules, Installing packages and working with aliases.
#
# # import turtle
# # tim = turtle.Turtle()
#
# # from turtle import Turtle
#
# # tim = Turtle()
# tom = Turtle()
# terry = Turtle()
#
# import turtle as t
#
# tim = t.Turtle
#
# import heroes
# print(heroes.gen())
import turtle
# # Turtle Challenge 2 - Draw a Dashed Line
# from turtle import Turtle, Screen
# ted = Turtle()
#
# for i in range(15):
#     ted.pendown()
#     ted.forward(10)
#     ted.penup()
#     ted.forward(10)


# # Turtle Challenge 3 - Drawing different shapes
# from turtle import Turtle, Screen
# from random import choice
# tee = Turtle()
#
# sum_of_angles = 360
# sides = 3
# colors = ["light blue", "cyan", "red", "green",
#           "yellow", "brown", "pink", "black"]
#
# for _ in range(8):
#     random_color = choice(colors)
#     tee.pencolor(random_color)
#     for _ in range(sides):
#         tee.forward(100)
#         tee.right(sum_of_angles / sides)
#     sides += 1


# # Turtle Challenge 4 - Random Walk
# from turtle import Turtle, Screen
# from random import choice
#
# tej = Turtle()
# tej.pensize(10)
# paths = [0, 90, 180, 270]
# colors = ["light blue", "cyan", "red", "green",
#           "yellow", "brown", "pink", "black"]
# tej.speed('fastest')
#
# for _ in range(200):
#     tej.pencolor(choice(colors))
#     direction = choice(paths)
#     tej.setheading(direction)
#     tej.forward(50)
#
# screen = Screen()
# screen.exitonclick()


# # Python Tuples and How to generate random RBG colors
# import turtle as t
# from turtle import Screen
# import random
# tej = t.Turtle()
# t.colormode(255)
#
#
# def random_color():
#     r = random.randint(0, 255)
#     g = random.randint(0, 255)
#     b = random.randint(0, 255)
#     return r, g, b
#
#
# tej.pensize(10)
# paths = [0, 90, 180, 270]
# colors = ["light blue", "cyan", "red", "green",
#           "yellow", "brown", "pink", "black"]
# tej.speed('fastest')
#
# for _ in range(200):
#     tej.pencolor(random_color())
#     direction = random.choice(paths)
#     tej.setheading(direction)
#     tej.forward(50)


# Turtle Challenge 5 - Draw a spirograph
import turtle as t
import random

tron = t.Turtle()
turtle.colormode(255)
tron.speed('fastest')


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tron.pencolor(random_color())
        tron.circle(100)
        tron.left(size_of_gap)  # Or tron.setheading(tron.heading + size_of_gap)


draw_spirograph(5)

screen = t.Screen()
screen.exitonclick()