from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Verdana", 15, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.path = r"C:\Users\Szymon Bryniak\Desktop\data.txt"
        self.color("red")
        self.position = (0, 278)
        self.hideturtle()
        self.coll = 0
        self.high_score = 0
        self.score_file()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        if self.coll > int(self.high_score):
            with open(self.path, mode="w") as self.highscore:
                self.highscore.write(str(self.coll))

    def display_score(self):
        self.penup()
        self.goto(self.position)
        self.write(f"score = {self.coll} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def score_file(self):
        with open(self.path, mode="r") as self.highscore:
            self.high_score = self.highscore.read()




