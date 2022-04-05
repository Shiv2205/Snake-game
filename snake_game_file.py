import time
from turtle import Screen
from food import Food
from scoreboard import Scoreboard
from snake import Snake


def snake_game():
    screen = Screen()
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