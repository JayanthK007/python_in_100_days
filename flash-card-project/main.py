from tkinter import *
import pandas
from random import *

BACKGROUND_COLOR = "#B1DDC6"
french_data={}
current_data={}


try:
    data=pandas.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data= pandas.read_csv("data/french_words.csv")
    french_data=original_data.to_dict(orient='records')
else:       
    french_data=data.to_dict(orient='records')


def generate_unknown_word():
    global current_data,flip_timer
    window.after_cancel(flip_timer)
    french_data.remove(current_data)
    data=pandas.DataFrame(french_data)
    data.to_csv('data/words_to_learn.csv',index=False)
        
    generate_random()


def generate_random():
    global current_data ,flip_timer
    window.after_cancel(flip_timer)
    current_data=choice(french_data)
    canvas.itemconfig(card_image,image=old_img)
    canvas.itemconfig(card_title,text="French",font=('arial',40,'italic'),fill="black")
    canvas.itemconfig(card_word,text=current_data['French'],font=('arial',60,'bold'),fill="black")
    flip_timer=window.after(3000,change_img)



def change_img():
    global current_data
    canvas.itemconfig(card_image,image=new_img)
    canvas.itemconfig(card_title,text="English",font=('arial',40,'italic'),fill="white")
    canvas.itemconfig(card_word,text=current_data['English'],font=('arial',60,'bold'),fill="white")

#------------------------ UI SETUP ------------------------------------#
window=Tk()
window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer=window.after(3000,change_img)


canvas=Canvas(width=800,height=526,bg=BACKGROUND_COLOR,highlightthickness=0)
old_img=PhotoImage(file='./images/card_front.png')
new_img=PhotoImage(file="images/card_back.png")
card_image=canvas.create_image(400,263,image=old_img)
card_title=canvas.create_text(400,150,text="",font=('arial',40,'italic'))
card_word=canvas.create_text(400,263,text="",font=("arial",60,'bold'))
canvas.grid(row=0,column=0,columnspan=2)

wrong_button_img=PhotoImage(file='images/wrong.png')
wrong_button=Button(image=wrong_button_img,highlightthickness=0,bg=BACKGROUND_COLOR,command=generate_random)
wrong_button.grid(row=1,column=0)

right_button_img=PhotoImage(file="images/right.png")
right_button=Button(image=right_button_img,highlightthickness=0,bg=BACKGROUND_COLOR,command=generate_unknown_word)
right_button.grid(row=1,column=1)

generate_random()
window.mainloop()