from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.snake_segments = []
        self.create_snake()
        self.head = self.snake_segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def grow(self):
        last_segment_position = self.snake_segments[-1].position()
        self.add_segment(last_segment_position)

    def add_segment(self, position):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.goto(position)
        self.snake_segments.append(new_segment)

    def move(self):
        for seg_num in range(len(self.snake_segments) - 1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        if self.head.xcor() > 300:
            self.head.goto(-300, self.head.ycor())
        elif self.head.xcor() < -300:
            self.head.goto(300, self.head.ycor())
        elif self.head.ycor() < -300:
            self.head.goto(self.head.xcor(), 300)
        elif self.head.ycor() > 300:
            self.head.goto(self.head.xcor(), -300)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(0)
