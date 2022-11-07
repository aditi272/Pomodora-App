import math
from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer= None
# ---------------------------- TIMER RESET ------------------------------- # 
def resetfunc():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text="00:00")
    timer_label.config(text='Timer')
    tick_label.config(text="")
    reps = 0


#--------------------------- TIMER MECHANISM ------------------------------- #
def countfunc():
 global reps
 reps+=1
 work_sec = WORK_MIN*60
 short_break_sec = SHORT_BREAK_MIN*60
 long_break_sec = LONG_BREAK_MIN*60

 if reps %8==0:
     timer_label.config(text="Break",font=(FONT_NAME,30,"normal"),fg=RED)
     count_down(long_break_sec)
 elif reps%2==0:
     timer_label.config(text="Break", font=(FONT_NAME, 30, "normal"), fg=PINK)
     count_down(short_break_sec)
 else:
     timer_label.config(text="Work", font=(FONT_NAME, 30, "normal"), fg=GREEN)
     count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count/60)
    count_sec = count%60
    if(count_sec < 10):
        count_sec=f"0{count_sec}"
    canvas.itemconfig(timer_text ,text=f"{count_min}:{count_sec}")
    if(count>0):
       timer = window.after(1000, count_down,count-1)
    else:
        countfunc()
        marks = " "
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += "✅"
        tick_label.config(text=marks)
# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)

#Canvas widget in tkinter
#It allows us to place an image onto our program and also place text on top of that
canvas = Canvas(width=200,height=224,bg=YELLOW,highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=img)
timer_text=canvas.create_text(100,130,text="00:00",fill="white",font=(FONT_NAME,35,"bold"))

canvas.grid(column=1,row=1)


timer_label = Label(text="Timer",font=(FONT_NAME,30,"normal"))
timer_label.config(fg=GREEN,bg=YELLOW)

timer_label.grid(column=1,row=0)

tick_label = Label(text="✅",fg=GREEN,bg=YELLOW)
tick_label.grid(column=1,row=3)


start_button = Button(text="Start",font=(FONT_NAME,'8','normal'),command=countfunc)
reset_button = Button(text="Reset",font=(FONT_NAME,'8','normal'),command=resetfunc)
start_button.grid(column=0,row=2)

reset_button.grid(column=2,row=2)
start_button.config(bg="#ffffff",borderwidth=0)
reset_button.config(bg="#ffffff",borderwidth=0)







window.mainloop()
