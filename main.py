from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Snake")
screen.bgcolor("black")

snake_length = 3

snake = Snake()
snake.create_snake(snake_length)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

food = Food()
score = Scoreboard()

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.2)
    snake.move()
    if snake.snake_body[0].distance(food) < 15:
        food.refresh()
        score.add_score()
        snake.add_segment()

    if snake.snake_body[0].xcor() > 280 or snake.snake_body[0].ycor() > 280 or snake.snake_body[0].xcor() < -280 or snake.snake_body[0].ycor() < -280:
        score.high_score_set()
        score.reset()
        snake.reset()

    for segment in snake.snake_body[1:]:
        if snake.snake_body[0].distance(segment) < 10:
            score.high_score_set()
            score.reset()
            snake.reset()

screen.exitonclick()

