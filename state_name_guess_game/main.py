import turtle
from turtle import Turtle, Screen
import pandas
import time

screen = Screen()
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
writer = Turtle()
writer.hideturtle()
writer.penup()

data = pandas.read_csv("50_states.csv")
total_states = len(data)


def get_state_data(state):
    return data[data.state == state]


guessed_states = []

while len(guessed_states) < 50:
    user_input = screen.textinput(title=f"{len(guessed_states)} / 50 States Correct", prompt="What's the another state's name? ").title()
    if user_input == "Exit":
        # create a csv which has missing states which user did not guess
        file_name = "states_to_learn.csv"
        all_states = data.state.to_list()
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        pandas.DataFrame(missing_states).to_csv(file_name)
        break

    state_data = get_state_data(user_input)
    if len(state_data) > 0:
        guessed_states.append(user_input)
        name = state_data.state.item()
        x_cor = int(state_data.x)
        y_cor = int(state_data.y)
        writer.goto(x_cor, y_cor)
        writer.write(f"{name}", False, "center", ("Courier", 10, "normal"))
        time.sleep(0.5)
screen.mainloop()
