from turtle import Turtle

PADDLE_WIDTH = 5
PADDLE_LEN = 1
PADDLE_COLOR = "white"
NORTH = 90
SOUTH = 270
PADDLE_STEP = 20


class Paddle(Turtle):
    def __init__(self, x, y):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=PADDLE_WIDTH, stretch_len=PADDLE_LEN)
        self.color(PADDLE_COLOR)
        self.penup()
        self.speed("fastest")
        self.place(x, y)

    def place(self, x, y):
        self.goto(x, y)

    def move_up(self):
        if self.ycor() < 235:
            y_pos = self.ycor() + PADDLE_STEP
            self.goto(self.xcor(), y_pos)

    def move_down(self):
        if self.ycor() > -235:
            y_pos = self.ycor() - PADDLE_STEP
            self.goto(self.xcor(), y_pos)
