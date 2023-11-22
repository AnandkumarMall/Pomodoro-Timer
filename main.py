from tkinter import *
import math
import time

PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#DDFFBB"
BLUE = "#04364A"
SKIN = "#251B37"
YELLOW = "#F7E987"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
counter = 0
c = "✔"
clock = None
new_time = [WORK_MIN, SHORT_BREAK_MIN, LONG_BREAK_MIN]

window = Tk()
window.title("Pomodoro Timer")
window.config(padx=80, pady=40, bg=BLUE)


def reset():
    window.after_cancel(clock)
    global counter
    counter = 0
    canvas.itemconfig(timer, text="00:00")
    title.config(text="Timer", fg=GREEN)


def count_dow(count):
    global c
    global clock
    count_m = math.floor(count / 60)
    count_s = count % 60
    if count_s < 10:
        count_s = f"0{count_s}"
    canvas.itemconfig(timer, text=f"{count_m}:{count_s}")
    if count > 0:
        clock = window.after(1000, count_dow, count - 1)
    else:
        if counter % 2 == 0:
            tick.config(text=c)
            c += c
        start_timer()


def start_timer():
    global counter
    counter += 1
    if counter % 8 == 0:
        title.config(text="Long Break", fg=RED)
        count_dow(LONG_BREAK_MIN * 60)
    elif counter % 2 == 0:
        title.config(text="Short Break", fg=PINK)
        count_dow(SHORT_BREAK_MIN * 60)
    else:
        title.config(text="Work")
        count_dow(WORK_MIN * 60)


title = Label(text="Timer", bg=BLUE, fg=GREEN, font=(FONT_NAME, 40, "bold"))
title.grid(column=1, row=0)
canvas = Canvas(width=200, height=224, bg=BLUE, highlightthickness=0)
tomato = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato)
timer = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)
start = Button(text="Start", bg=RED, fg=GREEN, width=20, command=start_timer)
start.grid(column=0, row=2)
restart = Button(text="Restart", bg=RED, fg=GREEN, width=20, highlightthickness=0, command=reset)
restart.grid(column=2, row=2)
tick = Label(bg=BLUE, fg=GREEN, highlightthickness=0)
tick.grid(column=1, row=3)
window.mainloop()
