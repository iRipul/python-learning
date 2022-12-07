from turtle import Turtle, Screen
import random

wd = Screen()
wd.setup(width=500, height=400)

turtles_list = []
colors = ["red", "green", "blue", "orange", "cyan", "purple"]
pos = [-100, -70, -40, -10, 20, 50]
for num in range(0,6):
    new_turtle = Turtle()
    new_turtle.penup()
    new_turtle.shape("turtle")
    new_turtle.color(colors[num])
    new_turtle.goto(x=-230, y=pos[num])
    turtles_list.append(new_turtle)

user_bet = wd.textinput(title="Make a bet.", prompt="Which turtle will win the race? Enter a color.")
is_race_on = False

if user_bet:
    is_race_on = True
is_user_win = False
while is_race_on:
    for turtle in turtles_list:
        turtle.forward(random.randint(1, 10))
        if turtle.xcor() >= 230:
            is_race_on = False
            winner = turtle.pencolor()
            if turtle.pencolor() == user_bet:
                is_user_win = True
                break


print(f"{winner.capitalize()} turtle reached the winning line")
if is_user_win:
    print("You Win!")
else:
    print("You Lose!")
wd.exitonclick()
