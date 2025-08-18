import random
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

# Setup
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My snake game")
screen.tracer(0)

snake = Snake()
food = Food()
scoreboard = Scoreboard()


# Key bindings
screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

# Game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.increase_score()

    # Check for collision with wall
    head = snake.segments[0]
    if abs(head.xcor()) > 290 or abs(head.ycor()) > 290:
        game_is_on = False

    #collision with itself
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            game_is_on = False


scoreboard.game_over()
screen.exitonclick()
