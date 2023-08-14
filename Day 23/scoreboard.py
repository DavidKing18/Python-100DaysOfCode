from turtle import Turtle

FONT = ("Courier", 24, "bold")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.penup()
        self.score = 1
        self.current_level()

    def current_level(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", True, align='center', font=FONT)
        self.score += 1

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", True, align='center', font=FONT)
