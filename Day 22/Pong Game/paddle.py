from turtle import Turtle, Screen


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.coordinates = coordinates
        self.shape('square')
        self.color('White')
        self.shapesize(5, 1)
        self.penup()
        self.goto(self.coordinates)

    def move_up(self):
        self.shapesize(1, 5)  # OR
        self.setheading(90)  # new_y = paddle.ycor() + 20
        self.forward(20)  # paddle.goto(paddle.xcor(), new_y)

    def move_down(self):
        self.shapesize(1, 5)  # OR
        self.setheading(270)  # OR new_y = paddle.ycor() - 20
        self.forward(20)  # paddle.goto(paddle.xcor(), new_y)


class CenterLines(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(40, 0.1)
        self.color("white")
        self.goto(0, -70)
        self.circle(70)
