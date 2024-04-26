from turtle import Turtle,Screen
import random

screen=Screen()
# def move_forward():
#     new_turtles.forward(10)

# def move_backward():
#     new_turtles.backward(10)    

# def clockwise():
#     new_turtles.right(45)

# def counter_clockwise():
#     new_turtles.left(45)

# def move_to_center():
#     new_turtles.reset()
    
# def circle():
#     new_turtles.circle(25)    

# screen.listen()
# screen.onkey(move_forward,"w")
# screen.onkey(move_backward,'s')
# screen.onkey(counter_clockwise,'a')
# screen.onkey(clockwise,'d')
# screen.onkey(move_to_center,"c")
# screen.onkey(circle, "f")


screen.setup(width=500,height=400)
user_bet=screen.textinput(title="Make your bet",prompt='Which color turtle will win the race? Enter the color')
colors=['red','orange','yellow', 'green','blue','purple']
distance=[-70,-40,-10,20,50,80]
all_turtles=[]

for index in range(6):
    new_turtles=Turtle('turtle',)
    new_turtles.color(colors[index])
    new_turtles.penup()
    new_turtles.goto(x=-230,y=distance[index])
    all_turtles.append(new_turtles)

is_game_on=False

if user_bet:
    is_game_on=True

while is_game_on: 
    for turtle in all_turtles: 
        if turtle.xcor()>230:
            is_game_on=False
            Winning_color=turtle.pencolor()
            if Winning_color==user_bet:
                print(f"You won! The {Winning_color} turtle is the winner.")  
            else:
                print(f'You lose! The {Winning_color} turtle is winner')    
        rand_dist=random.randint(0,10)
        turtle.forward(rand_dist)
        


screen.exitonclick()