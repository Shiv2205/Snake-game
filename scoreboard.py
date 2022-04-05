from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.score = -1
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", align="center", font=("Courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER...", align="center", font=("Courier", 24, "normal"))

