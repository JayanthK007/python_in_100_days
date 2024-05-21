from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:
    def __init__(self,quiz_brain:QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20,pady=20,bg=THEME_COLOR)

        self.canvas=Canvas()
        self.canvas.config(width=300,height=250,bg="white")
        self.question_text=self.canvas.create_text(150,125,width=280,text="hello",font=('Arial',20,'italic'),fill=THEME_COLOR)
        self.canvas.grid(row=1,column=0,columnspan=2,pady=50)

        self.label=Label()
        self.label.config(text='Score: 0',bg=THEME_COLOR,fg='white')
        self.label.grid(row=0,column=1)

        self.right_button=Button()
        self.right_button_img=PhotoImage(file='images/true.png')
        self.right_button.config(image=self.right_button_img,highlightthickness=0,command=self.right_answer)
        self.right_button.grid(row=2,column=0)

        self.wrong_button=Button()
        self.wrong_button_img=PhotoImage(file='images/false.png')
        self.wrong_button.config(image=self.wrong_button_img,highlightthickness=0,command=self.wrong_answer)
        self.wrong_button.grid(row=2,column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            self.label.config(text=f'Score: {self.quiz.score}')
            q_text= self.quiz.next_question ()
            self.canvas.itemconfig(self.question_text,text=q_text)
        else:
            self.canvas.itemconfig(self.question_text,text="You've reached the end of the quiz.")
            self.right_button.config(state='disabled')
            self.wrong_button.config(state="disabled")    

    def right_answer(self):
        ans=self.quiz.check_answer('True')
        self.give_feedback(ans)

    def wrong_answer(self):
        ans=self.quiz.check_answer('False')    
        self.give_feedback(ans)

    def give_feedback(self,ans):
        if ans:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        self.window.after(1000,self.get_next_question)  
