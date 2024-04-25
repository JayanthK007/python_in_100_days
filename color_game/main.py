# import colorgram

# colors=colorgram.extract(r'download.jpg',10)
# color_list=[]
# for color in colors:
#     r=color.rgb.r
#     g=color.rgb.g
#     b=color.rgb.b
#     color_list.append((r,g,b))

# print(color_list)

import turtle
import random
from turtle import Turtle,Screen    

color_list=[(251, 240, 247), (236, 243, 250), (236, 226, 85), (211, 159, 109), (115, 176, 211), (202, 5, 69), (231, 53, 126), (195, 77, 20)]

turtle.colormode(255)
tut=Turtle()

screen=Screen()

tut.speed(0)
tut.penup()
tut.goto(-200,-200)
tut.pendown()
tut.hideturtle()
for _ in range(10):
    for _ in range(10):
        tut.dot(20,random.choice(color_list))
        tut.penup()
        tut.forward(50)
        tut.pendown()
    tut.penup()    
    tut.goto(-200,tut.ycor()+50)
    tut.pendown()
        



screen.exitonclick()
