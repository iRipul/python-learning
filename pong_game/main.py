from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

from pong_game.scoreboard import Scoreboard

RIGHT_UP = "Up"
RIGHT_DOWN = "Down"
LEFT_UP = "w"
LEFT_DOWN = "s"

screen = Screen()
screen.setup(height=600, width=800)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_paddle = Paddle(x=350, y=0)
left_paddle = Paddle(x=-350, y=0)
ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(right_paddle.move_up, RIGHT_UP)
screen.onkey(right_paddle.move_down, RIGHT_DOWN)
screen.onkey(left_paddle.move_up, LEFT_UP)
screen.onkey(left_paddle.move_down, LEFT_DOWN)

game_is_on = True

while game_is_on:
    # time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # detect upper wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # detect collision with handle
    if ball.distance(left_paddle) < 50 and ball.xcor() < -320 \
            or ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        ball.speed_boost()

    # right player miss
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    # left player miss
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()

screen.exitonclick()
