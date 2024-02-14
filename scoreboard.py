from turtle import Turtle
from ball import Ball

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-75, 230)
        self.write(self.l_score, align="center", font=("arial", 40, "normal"))
        self.goto(75, 230)
        self.write(self.r_score, align="center", font=("arial", 40, "normal"))

    def track_rscore(self):
        self.r_score += 1
        self.update_scoreboard()

    def track_lscore(self):
        self.l_score += 1
        self.update_scoreboard()