from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 0.02


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.create_car()

    def create_car(self):
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.color(random.choice(COLORS))
        self.goto(300, random.randint(-250, 250))

    def move_car(self):
        self.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        global STARTING_MOVE_DISTANCE
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        self.backward(STARTING_MOVE_DISTANCE)
