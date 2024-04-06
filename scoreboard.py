from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.position = (0, 280)

    def display_score(self):
        self.penup()
        self.goto(self.position)
        self.write("score = 0", align="center", font=("Verdana", 15, "normal"))


