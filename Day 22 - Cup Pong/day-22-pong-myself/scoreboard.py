from turtle import Turtle


class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.speed("fastest")
        self.hideturtle()
        self.penup()
        self.sety(240)
        self.color("white")
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def add_l_score(self):
        self.l_score += 1
        self.update_scoreboard()

    def add_r_score(self):
        self.r_score += 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"{self.l_score}  {self.r_score}", align="center", font=("Consolas", 40, "normal"))


class Line(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.setheading(90)
        self.penup()
        self.sety(-280)
        self.pensize(5)

    def draw_line(self):
        for _ in range(30):
            self.pendown()
            self.forward(20)
            self.penup()
            self.forward(20)
