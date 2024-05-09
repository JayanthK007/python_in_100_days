import turtle
import pandas


screen=turtle.Screen()
screen.title("U.S. States Game")
image="blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)
data=pandas.read_csv("50_states.csv")
all_states=data.state.to_list()
count=0
while count!=49:
    answer=turtle.textinput(title=f"{count}/50 states correct",prompt="What's another state name?").title()
    if answer in all_states:
        count+=1
        series_state=data[data.state == answer]
        new_tut=turtle.Turtle()
        new_tut.hideturtle()
        new_tut.penup()
        new_tut.goto(int(series_state.iloc[0,1]),int(series_state.iloc[0,2]))
        new_tut.write(answer)



screen.exitonclick()


