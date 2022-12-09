from turtle import Screen
from snake import Snake
from food import Food
from bonus_food import BonusFruit
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
bonus_food = BonusFruit()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

is_game_on = True
while is_game_on:
    snake.move()
    # place a bonus food after 5 normal food
    if scoreboard.current_score() > 0 \
            and scoreboard.current_score() % 10 == 0 \
            and not bonus_food.isvisible():
        bonus_food.spawn()

    if scoreboard.current_score() % 10 != 0 and bonus_food.isvisible():
        bonus_food.hide()

    # detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.grow()
        scoreboard.add()

    if bonus_food.isvisible() and snake.head.distance(bonus_food) < 15:
        bonus_food.hide()
        snake.grow()
        scoreboard.add(4)

    # # detect collision with wall
    # if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
    #     is_game_on = False
    #     scoreboard.game_over()

    # detect collision with tail
    for segment in snake.snake_segments[1:]:
        if snake.head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

    screen.update()
    time.sleep(0.1)
screen.exitonclick()
