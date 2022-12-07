import turtle
import random
from turtle import Turtle, Screen

turtle.colormode(255)
tim = Turtle()
tim.pu()
tim.hideturtle()


def random_color():
    return random.choice(rgb_colors)


rgb_colors = [(236, 224, 80), (197, 7, 71), (195, 164, 13), (201, 75, 15), (231, 54, 132),
              (110, 179, 216), (217, 163, 101), (27, 105, 168), (35, 186, 109), (19, 29, 168),
              (13, 23, 66), (212, 135, 177), (233, 223, 7), (199, 33, 132), (13, 183, 212), (230, 166, 199)]

tim.setheading(225)
tim.forward(300)
tim.setheading(0)

for dot_count in range(1, 101):
    tim.dot(20, random_color())
    tim.forward(50)
    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

Screen().exitonclick()
