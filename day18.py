from turtle import Turtle,Screen
import random
import turtle


turtle.colormode(255)

tim=Turtle()
tim.shape("turtle")

# for _ in range(20):
#     tim.forward(10)
#     tim.color('white')
#     tim.forward(10)
#     tim.color('black')


# for i in range(3,11):
#     tim.color((random.randint(0, 255), 
#           random.randint(0, 255), 
#           random.randint(0, 255)))
#     for _ in range(i):
#         angle=360/i
#         tim.forward(100)
#         tim.right(angle)


# angle=[0,90,180,270]
# count=0
# tim.pensize(5)
# tim.speed('fastest')
# while count<=300:
#     tim.color((random.randint(0, 255), 
#           random.randint(0, 255), 
#           random.randint(0, 255)))
#     count+=1     
#     tim.forward(30)
#     tim.setheading(random.choice(angle))


# tim.speed(0)
# def draw(size):
#     for _ in range(360//size):
#         tim.color((random.randint(0,255),random.randint(0,255),random.randint(0,255)))
#         tim.circle(100)
#         tim.setheading(tim.heading()+size)
        
        
# draw(5)
 
# screen=Screen()
# screen.exitonclick()