from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN =5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #
def reset_timer():
    window.after_cancel(timer)
    title_label.config(text="Timer", fg = GREEN, font=(FONT_NAME, 50) , bg = YELLOW)
    checkmark.config(text="", fg = GREEN, bg = YELLOW)
    canvas.itemconfig(live_timer, text="00:00")
    global reps
    reps = 0
# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global reps
    reps += 1
    if reps % 8 == 0:
        count_down(LONG_BREAK_MIN * 60)
        title_label.config(text="Relax", fg=RED)

    elif reps % 2 != 0:
        count_down(WORK_MIN * 60)
        title_label.config(text="Focus", fg = GREEN)
    else:
        count_down(SHORT_BREAK_MIN * 60)
        title_label.config(text="Relax", fg = RED)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(live_timer, text=f"{count_min}:{count_sec}")
    if (count > 0):
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        for _ in range(math.floor(reps/2)):
            marks += "✔"
        checkmark.config(text=marks,fg = GREEN , bg = YELLOW)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady= 50 ,bg=YELLOW)

# label
title_label = Label(text = "Timer" , fg = GREEN, font=(FONT_NAME, 50) , bg = YELLOW)
title_label.grid(row = 0, column= 1)

# canvas
canvas = Canvas(width=200, height=224 , bg = YELLOW, highlightthickness=0)
img = PhotoImage(file = "tomato.png")
canvas.create_image(103, 112,image = img)
canvas.grid(column=1, row = 1)
live_timer =  canvas.create_text(103,130, text="00:00" , fill = "white" , font=(FONT_NAME, 35, "bold"))


# start button
start_button = Button(text="Start", command=start_timer)
start_button.grid(column=0, row = 2)
# stop Button
end_button = Button(text ="Reset", command=reset_timer)
end_button.grid(column=2, row=2)
# check mark

checkmark = Label(text = "", fg = GREEN, bg=YELLOW)
checkmark.grid(column=1,row=3)

window.mainloop()