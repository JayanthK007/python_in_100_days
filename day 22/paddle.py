from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.penup()
        self.color('white')
        self.shape('square') 
        self.goto(x,y)
        self.turtlesize(stretch_len=1,stretch_wid=5)

    def move_forward(self):
        # if -260<=self.ycor()<=260:
            self.goto(self.xcor(),self.ycor()+20)

    def move_backward(self):
        # if -260<=self.ycor()<=260:
            self.goto(self.xcor(),self.ycor()-20)    