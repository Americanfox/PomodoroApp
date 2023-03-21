from tkinter import *
import math
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
def reset_timer():
    window.after_cancel(timer)
    timer_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    check.config(text=" ")
    global reps
    reps = 0




# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    if reps % 8 == 0:
        countdown(long_break_sec)
        timer_label.config(text="Take a Break")
    elif reps % 2 == 0:
        countdown(short_break_sec)
        timer_label.config(text="Take a Break")
    else:
        countdown(work_sec)
        timer_label.config(text="Time to Work")

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def countdown(count):

    count_min = math.floor(count / 60)
    count_sec = count % 60

    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")

    if count > 0:
        window.after(1000, countdown, count - 1)

    else:
        start_timer()
        marks = ""
        work_sessions = math.floor((reps/2))
        for _ in range(work_sessions):
            marks += "✔"
            check.config(text=marks)



# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=150, pady=50, bg=YELLOW)


# Column 1
start = Button(text="Start", bg=YELLOW, fg=RED, font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=start_timer)
start.grid(column=0, row=2)

# Column 2
timer_label = Label(text="Timer", bg=YELLOW, fg=RED, font=(FONT_NAME, 30, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 135, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

check = Label(bg=YELLOW, fg=RED, font=(FONT_NAME, 30, "bold"))
check.grid(column=1, row=3)

# Column 3
reset = Button(text="Reset", bg=YELLOW, fg=RED, font=(FONT_NAME, 15, "bold"), highlightthickness=0, command=reset_timer)
reset.grid(column=2, row=2)

window.mainloop()

# fg to color background
# ✔
#TODO: Day 28 took 1 hour and 35 minutes to complete