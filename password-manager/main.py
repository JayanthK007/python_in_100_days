from tkinter import *
from tkinter import messagebox
from random import choice,randint,shuffle
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
#Password Generator Project
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']



    password_list=[choice(letters) for _ in range(randint(8, 10)) ]  
    password_list += [choice(symbols) for _ in range(randint(2, 4))]
    password_list +=[ choice(numbers) for _ in range(randint(2, 4))]
    shuffle(password_list)

    password = "".join(password_list)
    pyperclip.copy(password)
    password_input.insert(0,password)
# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    website = website_input.get()
    email = email_user_name_input.get()
    password = password_input.get()
    
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title='Oops',message='Please don\'t leave any fields empty')
    else:    
        is_ok=messagebox.askokcancel(title=f'{website}',message=f'These are the details entered:\nEmail:{email}\n Passowrd:{password}\n Is it ok to save?')
        
        if is_ok:
            with open("data.txt",'a') as file:
                file.write(f"{website} | {email} | {password}\n")
                website_input.delete(0,'end')
                password_input.delete(0,'end')
# ---------------------------- UI SETUP ------------------------------- #

window=Tk()
window.title("Password Manager")
window.config(padx=50,pady=50)


canvas=Canvas(width=200,height=200)
img=PhotoImage(file='logo.png')
canvas.create_image(100,100,image=img)
canvas.grid(row=0,column=1)

website_label=Label(text="Website: ")
website_label.grid(row=1,column=0)

website_input=Entry(width=35)
website_input.focus()
website_input.grid(row=1,column=1,columnspan=2)

email_user_name=Label(text="Email/Username: ")
email_user_name.grid(row=2,column=0)

email_user_name_input=Entry(width=35)
email_user_name_input.insert(0,'jayanth@gmail.com')
email_user_name_input.grid(row=2,column=1,columnspan=2)

password_label=Label(text='Password: ')
password_label.grid(row=3,column=0)

password_input=Entry(width=17)
password_input.grid(row=3,column=1)

generate_password_button=Button(width=14,text="Generate Password",command=generate_password)
generate_password_button.grid(row=3,column=2)

add_button=Button(width=29,text='Add',command=add_password)
add_button.grid(row=4,column=1,columnspan=2)


window.mainloop()