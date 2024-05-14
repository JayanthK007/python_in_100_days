from tkinter import *


# def button_clicked():
#     my_label.config(text=input.get())


# window=Tk()
# window.title('My First GUI Program')
# window.minsize(500,300)

# #label
# my_label=Label(text="I am a label")
# my_label.grid(column=0,row=0)

# #button
# button=Button(text='click me',command=button_clicked)
# button.grid(column=1,row=1)

# #entry
# input=Entry(width=10)
# input.grid(column=3,row=3)

# button1=Button(text='hide it',command=button_clicked)
# button1.grid(column=2,row=0)
def calculate():
    number=int(input.get())
    my_label.config(text=f"Miles is equal to {number*1.6} Km")

window=Tk()
window.title('Mile to Km Converter')
window.minsize(100,100)

input=Entry(width=10)
input.pack()

my_label=Label(text=f'Miles is equal to 0 Km')
my_label.pack()

button=Button()
button.config(text="convert",command=calculate)
button.pack()


window.mainloop()

