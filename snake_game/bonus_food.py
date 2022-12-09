from turtle import Turtle
from food import Food
import random


class BonusFruit(Food):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color("yellow")
        self.speed("fastest")
        self.hide()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def spawn(self):
        self.refresh()
        self.showturtle()

    def hide(self):
        self.goto(-1500, 0)
        self.hideturtle()
