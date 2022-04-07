from turtle import Turtle

# Constants
MOVE_DISTANCE = 20


class Snake:

    def __init__(self):
        self.snake = []
        for i in range(3):
            self.add_segment((-20 * i, 0))
        self.head = self.snake[0]

    def add_segment(self, position):
        segment = Turtle("square")
        segment.penup()
        segment.color("green")
        segment.goto(position)
        self.snake.append(segment)

    def grow(self):
        self.add_segment(self.snake[-1].position())

    def move(self):
        for i in range(len(self.snake) - 1, 0, -1):
            self.snake[i].goto(self.snake[i - 1].xcor(), self.snake[i - 1].ycor())
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

