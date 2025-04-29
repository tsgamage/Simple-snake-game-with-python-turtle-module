import time
from turtle import Screen

from scoreboard import Scoreboard
from snake import Snake
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()
food = Food()
score_board = Scoreboard()

screen.listen()

current_direction = ""

_game_running = True
while _game_running:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Controlling the snake
    screen.onkey(snake.left, "a")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.down, "s")

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend_a_segment()

    # Detect collision with wall
    hit_right_wall = snake.head.xcor() > 280
    hit_left_wall = snake.head.xcor() < -300
    hit_top_wall = snake.head.ycor() > 280
    hit_bottom_Wall = snake.head.ycor() < -280

    if hit_right_wall or hit_left_wall or hit_top_wall or hit_bottom_Wall:
        _game_running = False
        score_board.game_over()

screen.exitonclick()
