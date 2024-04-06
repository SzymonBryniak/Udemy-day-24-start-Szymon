from turtle import Turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]


class Snake:
    def __init__(self):
        self.snake = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            new_segment = Turtle('square')
            new_segment.color('green')
            new_segment.penup()
            new_segment.goto(position)
            self.snake.append(new_segment)

    def move(self):

        for s in range(len(self.snake) - 1, 0, -1):
            new_x = self.snake[s - 1].xcor()
            new_y = self.snake[s - 1].ycor()
            self.snake[s].goto(new_x, new_y)
        self.snake[0].forward(20)

    def up(self):
        self.snake[0].setheading(90)

    def down(self):
        self.snake[0].setheading(270)

    def left(self):
        self.snake[0].setheading(180)

    def right(self):
        self.snake[0].setheading(0)









