from turtle import Turtle, Screen
from math import sqrt
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_turtle = Turtle()
screen = Screen()
my_turtle.shape("turtle")


def version_1():

    # lift pen before moving
    my_turtle.penup()

    # move turtle to top left corner
    my_turtle.setx(-200)
    my_turtle.sety(100)

    # put pen down before drawing
    my_turtle.pendown()
    for i in range(4):
        my_turtle.forward(400)
        my_turtle.right(90)

    # draw first diagonal
    my_turtle.right(45)
    hypo = sqrt((400 ** 2) * 2)
    my_turtle.forward(hypo)

    # reposition turtle while pen up
    my_turtle.penup()
    my_turtle.right(135)
    my_turtle.forward(400)
    my_turtle.right(135)

    # put pen down and draw 2nd diagonal
    my_turtle.pendown()
    my_turtle.forward(hypo)

    # draw roof
    hypo_roof = sqrt((200 ** 2) * 2)
    for i in range(2):
        my_turtle.left(90)
        my_turtle.forward(hypo_roof)

    screen.exitonclick()


def version_2():
    # lift pen before moving
    my_turtle.penup()

    # move turtle to bottom left corner
    my_turtle.setx(-200)
    my_turtle.sety(-300)

    # put pen down before drawing
    my_turtle.pendown()

    # draw first wall
    my_turtle.left(90)
    my_turtle.forward(400)

    # draw roof
    hypo_roof = sqrt((200 ** 2) * 2)
    for i in range(2):
        my_turtle.right(45 * (i + 1))
        my_turtle.forward(hypo_roof)

    # draw 2nd wall
    my_turtle.right(45)
    my_turtle.forward(400)

    # diagonals and bottom
    hypo = sqrt((400 ** 2) * 2)
    for i in range(2):
        my_turtle.right(135)
        my_turtle.forward(hypo)
        my_turtle.right(135 + (90 * i))
        my_turtle.forward(400)

    screen.exitonclick()


def dashed_line():
    # reposition turtle to left of screen
    my_turtle.penup()
    my_turtle.setx(-400)
    my_turtle.pendown()

    # draw dashed line
    for i in range(10):
        my_turtle.forward(30)
        my_turtle.penup()
        my_turtle.forward(30)
        my_turtle.pendown()

    screen.exitonclick()


def sketch_app():
    # add event listener
    screen.listen()

    # move forward
    def move_forward():
        my_turtle.forward(30)
    screen.onkey(key="w", fun=move_forward)

    # move backward
    def move_backward():
        my_turtle.backward(30)
    screen.onkey(key="s", fun=move_backward)

    # rotate right
    def rotate_right():
        my_turtle.setheading(my_turtle.heading() - 10)
    screen.onkey(key="d", fun=rotate_right)

    # rotate left
    def rotate_left():
        my_turtle.setheading(my_turtle.heading() + 10)
    screen.onkey(key="a", fun=rotate_left)

    # clear screen
    def clean():
        screen.resetscreen()
    screen.onkey(key="c", fun=clean)

    screen.exitonclick()


def snake_game():
    screen.setup(width=600, height=600)
    screen.bgcolor("black")
    screen.title("Snake")
    screen.tracer(0)  # stop automatic update of screen

    python = Snake()
    food = Food()
    scoreboard = Scoreboard()
    screen.listen()

    screen.onkey(python.up, "Up")
    screen.onkey(python.down, "Down")
    screen.onkey(python.left, "Left")
    screen.onkey(python.right, "Right")

    game_is_on = True
    while game_is_on:
        screen.update()
        time.sleep(0.1)
        python.move()

        # detect collision with food
        if python.head.distance(food) < 15:
            food.refresh()
            python.grow()
            scoreboard.update_score()

        # detect collision with walls
        if python.head.xcor() > 290 or python.head.xcor() < -290 or python.head.ycor() > 300 or python.head.ycor() < -290:
            game_is_on = False
            scoreboard.game_over()

        # detect collision with head
        for segment in python.snake[1:]:
            if python.head.distance(segment) < 10:
                game_is_on = False
                scoreboard.game_over()

    screen.exitonclick()


