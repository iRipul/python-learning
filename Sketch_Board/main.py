from turtle import Turtle, Screen

tim = Turtle()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def turn_left():
    tim.left(10)


def turn_right():
    tim.right(10)


def clear():
    tim.pu()
    tim.clear()
    tim.home()
    tim.pd()


wd = Screen()
wd.listen()
wd.onkey(key="w", fun=move_forwards)
wd.onkey(key="s", fun=move_backwards)
wd.onkey(key="c", fun=clear)
wd.onkey(key="d", fun=turn_left)
wd.onkey(key="a", fun=turn_right)
wd.exitonclick()
