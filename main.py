from turtle import Screen, Turtle
import time
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
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
    screen.update()
    time.sleep(0.1)
    for s in range(len(snake) - 1, 0, -1):
        new_x = snake[s -1].xcor()
        new_y = snake[s -1].ycor()
        snake[s].goto(new_x, new_y)
    snake[0].forward(20)





screen.exitonclick()