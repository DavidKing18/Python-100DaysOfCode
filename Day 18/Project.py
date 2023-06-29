import colorgram
import turtle
import turtle as t
import random

colors = colorgram.extract('image.jpeg', 30)

rgb_colors = []
for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)

ted = t.Turtle()
turtle.colormode(255)
ted.hideturtle()

color_list = rgb_colors

for y in range(-5, 5):
    ted.penup()
    ted.goto(-250, 50*y)
    for x in range(-5, 6):
        ted.dot(20, random.choice(color_list))
        ted.penup()
        ted.goto(50*x, 50*y)

screen = t.Screen()
screen.exitonclick()
