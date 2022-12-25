from tkinter import *
import math
from playsound import playsound

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def start_timer():
    start_btn.config(state="disabled")
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_brk_sec = SHORT_BREAK_MIN * 60
    long_brk_sec = LONG_BREAK_MIN * 60
    # if its 1st, 3rd, 5th, 7th rep
    if reps % 8 == 0:
        # if its 8th rep
        title.config(text="Break", fg=RED)
        playsound("./beep_break.mp3")
        start_countdown(long_brk_sec)
    elif reps % 2 == 0:
        # if its 2nd, 4th, 6th rep
        title.config(text="Break", fg=PINK)
        playsound("./beep_break.mp3")
        start_countdown(short_brk_sec)
    else:
        title.config(text="Timer", fg=GREEN)
        playsound("./beep_work.mp3")
        start_countdown(work_sec)


def start_countdown(count):
    minutes = math.floor(count / 60)
    seconds = count % 60
    if seconds < 10:
        seconds = f"0{seconds}"

    canvas.itemconfig(timer_text, text=f"{minutes}:{seconds}")
    if count > 0:
        global timer
        timer = window.after(1000, start_countdown, count - 1)
    else:
        start_timer()
        marks = ""
        work_sessions = math.floor(reps/2)

        for _ in range(work_sessions):
            marks += "✔︎"
            checkmark.config(text=marks)


def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title.config(text="Timer")
    global reps
    reps = 0
    checkmark.config(text="")
    start_btn.config(state="normal")


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

# Canvas
canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=1, column=1)

# Title
title = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 50), bg=YELLOW)
title.grid(row=0, column=1)

# Button Start
start_btn = Button(text="Start", highlightbackground=YELLOW, command=start_timer)
start_btn.grid(row=2, column=0)
# Button Start
reset_btn = Button(text="Reset", highlightbackground=YELLOW, command=reset_timer)
reset_btn.grid(row=2, column=2)

# checkmark
checkmark = Label(fg=GREEN, font=(FONT_NAME, 30), bg=YELLOW)
checkmark.grid(row=2, column=1)

window.mainloop()
