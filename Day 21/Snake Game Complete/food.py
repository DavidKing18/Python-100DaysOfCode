from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        self.color("blue")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def bonus(self):
        self.color("red")
        self.shapesize(1, 1)
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)
