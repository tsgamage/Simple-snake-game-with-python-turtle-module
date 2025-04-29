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
_game_running = True

snake_steps = 0
while _game_running:
    time.sleep(0.1)
    screen.update()
    snake.move()

    # Controlling the snake
    screen.onkey(snake.left, "a")
    screen.onkey(snake.left, "A")
    screen.onkey(snake.right, "d")
    screen.onkey(snake.right, "D")
    screen.onkey(snake.up, "w")
    screen.onkey(snake.up, "W")
    screen.onkey(snake.down, "s")
    screen.onkey(snake.down, "S")

    # Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        score_board.increase_score()
        snake.extend_a_segment()

    # Detect collision with wall
    hit_right_wall = snake.head.xcor() > 280
    hit_left_wall = snake.head.xcor() < -300
    hit_top_wall = snake.head.ycor() > 280
    hit_bottom_Wall = snake.head.ycor() < -290

    if hit_right_wall or hit_left_wall or hit_top_wall or hit_bottom_Wall:
        _game_running = False
        score_board.game_over()
        score_board.game_over_reason("'You hit the wall'")

    # Detect if the snake hits its own body
    # check this because the snake already hit its own tail in start so we skip 2 moves and start to check if it hit it's tail
    if snake_steps > 2:
        for segment in snake.segments:
            if segment == snake.head:
                continue
            elif segment != snake.head and snake.head.distance(segment) < 10:
                _game_running = False
                score_board.game_over()
                score_board.game_over_reason("'You hit your own tail'")

    snake_steps += 1

screen.exitonclick()
