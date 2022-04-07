from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.goto(0, 270)
        self.score = 0
        self.highScore = 0
        self.color("white")
        self.update_score()
        self.hideturtle()

    def update_score(self):
        self.clear()
        self.write(f"Score = {self.score}  ||  High Score = {self.highScore}", align="center",
                   font=("Courier", 24, "normal"))

    def reset(self):
        if self.score > self.highScore:
            self.highScore = self.score
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER...", align="center", font=("Courier", 24, "normal"))
