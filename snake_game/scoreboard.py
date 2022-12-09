from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto((-50, 270))
        self.update_score()

    def add(self, number=1):
        self.score += number
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, "left", ("Courier", 20, "normal"))

    def game_over(self):
        self.goto(-80, 0)
        self.write("GAME OVER", False, "left", ("Courier", 30, "normal"))

    def current_score(self):
        return self.score
