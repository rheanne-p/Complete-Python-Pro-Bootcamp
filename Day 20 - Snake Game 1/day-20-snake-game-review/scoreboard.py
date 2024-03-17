from turtle import Turtle
FONT = ("Consolas", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("white")
        self.goto(x=0, y=260)
        self.update_score()

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(arg=f"Score: {self.score}", move=False, align="center", font=FONT)


class GameOver(Scoreboard):
    def __init__(self):
        super().__init__()
        self.clear()
        self.goto(x=0, y=0)
        self.write(arg="Game Over :(", move=False, align="center", font=FONT)
