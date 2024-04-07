from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.position = (0, 278)
        self.hideturtle()
        self.coll = 0

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def display_score(self):
        self.penup()
        self.goto(self.position)

        self.write(f"score = {self.coll}", align=ALIGNMENT, font=FONT)


