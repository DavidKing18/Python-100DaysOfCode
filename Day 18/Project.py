# import colorgram
#
# colors = colorgram.extract('image.jpeg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
# print(rgb_colors)

import turtle
import turtle as t
import random

ted = t.Turtle()
turtle.colormode(255)

color_list = [(238, 234, 227), (239, 231, 236), (231, 234, 240), (230, 239, 234), (203, 162, 101), (205, 165, 24),
              (150, 60, 93), (122, 181, 203), (221, 205, 118), (51, 15, 24), (186, 153, 168), (139, 28, 50),
              (12, 19, 46), (20, 104, 153), (50, 120, 70), (9, 28, 20), (166, 69, 46), (53, 18, 13), (67, 164, 97),
              (114, 177, 157), (153, 28, 23), (211, 180, 199), (159, 205, 211), (184, 105, 95), (184, 99, 111),
              (31, 43, 107), (235, 201, 7), (161, 208, 194), (18, 101, 52), (222, 180, 171)]

for y in range(0, 10):
    ted.pen()
    ted.goto(0, 50*y)
    for x in range(0, 10):
        ted.dot(20, random.choice(color_list))
        ted.penup()
        ted.goto(50*x, 50*y)

screen = t.Screen()
screen.exitonclick()
