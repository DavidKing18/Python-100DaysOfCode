from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.r_score = 0
        self.l_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-200, 220)
        self.write(f"Player 1: {self.l_score}", True, align='center', font=('Courier', 20, "bold"))
        self.goto(200, 220)
        self.write(f"Player 2: {self.r_score}", True, align='center', font=('Courier', 20, "bold"))

    def l_point(self):
        self.l_score += 1
        self.clear()
        self.update_scoreboard()

    def r_point(self):
        self.r_score += 1
        self.clear()
        self.update_scoreboard()

    def call_winner(self, winner):
        self.home()
        self.write(f"{winner} wins🎉", True, align="center", font=("Courier", 50, "bold"))
