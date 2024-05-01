from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score=0
        self.r_score=0
        self.goto(x,y)
        self.start()
    
    def start(self):
        self.write(f'{self.l_score}',align='center',font=('Courier', 80, 'normal'))
        self.write(f'{self.r_score}',align='center',font=('Courier', 80, 'normal'))



    def l_points(self):
        self.clear()
        self.l_score+=1
        self.write(f'{self.l_score}',align='center',font=('Courier', 80, 'normal'))

    def r_points(self):
        self.clear()
        self.r_score+=1
        self.write(f'{self.r_score}',align='center',font=('Courier', 80, 'normal'))