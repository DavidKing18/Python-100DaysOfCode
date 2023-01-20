from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 265)
        self.show_score()

    def show_score(self):
        self.clear()
        self.write(f"Score: {self.score}  High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.show_score()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open('data.txt', mode="w") as data:
                data.write(str(self.high_score))
        self.score = 0
        self.show_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(f"GAME OVER.", align=ALIGNMENT, font=FONT)

    def bonus_score(self):
        self.score += 2
        self.clear()
        self.show_score()