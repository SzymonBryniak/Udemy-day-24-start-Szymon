from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")

for i in range(3):
    t = Turtle()
    t.shape('square')
    t.color('green')
    t.penup()
    t.setpos(x=-20*i, y=0)





screen.exitonclick()