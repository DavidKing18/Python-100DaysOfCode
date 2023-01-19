from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.setheading(90)
        self.color('white')
        self.penup()
        self.shape('turtle')
        self.goto(STARTING_POSITION)

    def go_up(self):
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        self.setheading(180)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def move_right(self):
        self.setheading(0)
        self.forward(MOVE_DISTANCE)
        self.setheading(90)

    def go_down(self):
        if self.ycor() >= -270:
            self.backward(MOVE_DISTANCE)

    def reset(self):
        self.goto(STARTING_POSITION)
