# TURTLE RACING GAME

from turtle import Turtle, Screen
import random
screen = Screen()
user_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ").lower()
screen.setup(width=500, height=400)

is_race_on = False

colors = ['red', 'orange', 'green', 'blue', 'indigo', 'violet', 'yellow']
names = ['tim', 'tej', 'trent', 'tom', 'tron', 'trey', 'tye']
y_coordinates = [-150, -100, -50, 0, 50, 100, 150]
all_turtles = []

for index in range(0, 7):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_coordinates[index])
    new_turtle.color(colors[index])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True


while is_race_on:

    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won! The {winning_color} turtle is the winner!")
            else:
                print(f"You've lost! The {winning_color} turtle is the winner!")

        rand_distance = random.randint(0, 10)
        turtle.forward(rand_distance)

screen.exitonclick()
