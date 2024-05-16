from tkinter import *
from PIL import ImageTk,Image
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
timer=None
# ---------------------------- TIMER RESET ------------------------------- # 
def reset_timer():
    global timer
    global reps
    reps=0
    window.after_cancel(timer)
    canvas.itemconfig(timer_text,text="00:00")
    label.config(text="TIMER")
    check_box.config(text="")
# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps+=1
    work_sec=WORK_MIN*60
    short_break_sec=SHORT_BREAK_MIN*60
    long_break_sec=LONG_BREAK_MIN*60

    if reps %2 == 1:
        label.config(text="Work",fg=GREEN)
        count_down(work_sec)
    elif reps %2 ==0:
        label.config(text="Short Break",fg=PINK)
        count_down(short_break_sec)
    else:
        label.config(text="Long Break",fg=RED)
        count_down(long_break_sec)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = count//60
    count_sec = count%60
    global reps

    if count_sec<10:
        count_sec=f"0{count_sec}"


    canvas.itemconfig(timer_text,text=f'{count_min}:{count_sec}')
    if count>0:
        global timer
        timer=window.after(1000,count_down,count-1)
    else:
        start_timer()
        mark=""
        for _ in range(reps//2):
            mark+="✔"
        check_box.config(text=mark)    
# ---------------------------- UI SETUP ------------------------------- #
window=Tk()
window.title("Pomodoro")
window.config(padx=100,pady=50,bg=YELLOW)


canvas=Canvas(width=200,height=234,bg=YELLOW,highlightthickness=0)

img=PhotoImage(file='tomato.png')

canvas.create_image(100,112,image=img)
timer_text=canvas.create_text(100,130,text="00:00",fill='white',font=(FONT_NAME,35,'bold'))
canvas.grid(column=1,row=1)


label=Label(text="Timer",fg=GREEN,font=(FONT_NAME,30,'bold'),bg=YELLOW)
label.grid(column=1,row=0)

start_button=Button(highlightthickness=0)
start_button.config(text="Start",command=start_timer)
start_button.grid(column=0,row=2)

end_button=Button(highlightthickness=0)
end_button.config(text="Reset",command=reset_timer)
end_button.grid(column=2,row=2)

check_box=Label(fg=GREEN,font=(FONT_NAME,10,'bold'),bg=YELLOW)
check_box.grid(column=1,row=3)

window.mainloop()
