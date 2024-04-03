from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
game_is_on = True
snake = []

for i in range(5):
    t = Turtle()
    snake.append(t)
    t.shape('square')
    t.color('green')
    t.penup()
    t.setpos(x=-20*i, y=0)

while game_is_on:
    for s in snake:
        s.forward(20)





screen.exitonclick()