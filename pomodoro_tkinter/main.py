from tkinter import *
import math
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps=0
timer = None
def start_timer():
    global reps
    reps+=1
    if reps%8==0:
        count_down(LONG_BREAK_MIN*60)
        tlabel.config(text="Break",fg=RED)
    elif reps%2==0:
        count_down(SHORT_BREAK_MIN*60)
        tlabel.config(text="Break",fg=PINK)
    else:
        count_down(WORK_MIN*60)
        tlabel.config(text="Break",fg=GREEN)
def reset():
    tk.after_cancel(timer)
    canvas.itemconfig(time,text="00:00")
    tlabel.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps=0
def count_down(count):
    count_min=math.floor(count/60)
    count_sec=count%60
    if count_sec==0:
        count_sec="00"
    elif count_sec<10:
        count_sec="0"+str(count_sec)
    canvas.itemconfig(time,text=f"{count_min}:{count_sec}")
    if count>0:
        global timer
        timer=tk.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        for i in range(math.floor(reps/2)):
            mark+="✔"
        check_marks.config(text=mark)


tk=Tk()
tk.title("POMODORO APP")
tk.config(padx=100,pady=100,bg=YELLOW)
tlabel=Label(text="TIMER",fg=GREEN,bg=YELLOW,font=(FONT_NAME,50))
tlabel.grid(column=1,row=0)
canvas=Canvas(width=200,height=225,bg=YELLOW,highlightthickness=0)
a=PhotoImage(file="tomato.png")
canvas.create_image(100,112,image=a)
time=canvas.create_text(102,130,text="00:00",fill="white", font=(FONT_NAME,35,"bold"))
canvas.grid(column=1,row=1)
sbutton=Button(text="Start",command=start_timer)
sbutton.grid(column=0,row=3)
rbutton=Button(text="Reset",command=reset)
rbutton.grid(column=3,row=3)
check_marks=Label(fg=GREEN,bg=YELLOW)
check_marks.grid(column=1,row=3)




tk.mainloop()