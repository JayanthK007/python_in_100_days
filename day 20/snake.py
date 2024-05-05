from turtle import Turtle


START_POS=[(0,0),(-20,0),(-40,0)] #x and y coordinates
MOVE_DIST=20
UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    
    def  __init__(self):
        self.segments=[]
        self.create_snake()
        self.head=self.segments[0]

    def create_snake(self) :
        for  pos in START_POS:
            self.add_segment(pos)
            

    def add_segment(self,position):
        self.new_segment=Turtle('square')
        self.new_segment.color('white')
        self.new_segment.penup()
        self.new_segment.goto(position)
        self.segments.append(self.new_segment)

    def reset(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head=self.segments[0]    

    def extend(self):
        self.add_segment(self.segments[-1].pos())

    def move(self):
        for seg_num in range(len(self.segments)-1,0,-1):
            new_x=self.segments[seg_num-1].xcor()
            new_y=self.segments[seg_num-1].ycor() 
            self.segments[seg_num].goto(new_x,new_y)
        self.head.forward(MOVE_DIST)        

    def up(self):
        if self.head.heading()!=DOWN:
            self.head.setheading(UP)
        self.move()    

    def down(self):
        if  self.head.heading()!=UP:
            self.head.setheading(DOWN)
        self.move()

    def right(self):
        if   self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
        self.move()  
        
    def left(self):
        if  self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
        self.move()      
