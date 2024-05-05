from turtle import Turtle,Screen
import time
from snake import Snake
from food import Food
from score import Score

screen=Screen()
screen.setup(width=600,height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)

my_snake=Snake()
food=Food()
score=Score()

screen.listen()
screen.onkey(my_snake.up,"Up")
screen.onkey(my_snake.down,"Down")
screen.onkey(my_snake.left,"Left")
screen.onkey(my_snake.right,"Right")

is_game_on=True

while is_game_on:
    screen.update()
    time.sleep(0.1)
    my_snake.move()  

    #detect collision with food
    if my_snake.head.distance(food) <15:
        food.refresh()
        score.increase_score()
        score.update_score()
        my_snake.extend()

    #detect collison with wall
    if my_snake.head.xcor()>280 or my_snake.head.ycor()>280 or my_snake.head.xcor()<-280  or my_snake.head.ycor()<-280:
        score.reset()
        my_snake.reset()

    #detect collision with tail (self-eating)
    for segment in my_snake.segments[1:]:
        if my_snake.head.distance(segment)<10:
           score.reset()
           my_snake.reset()

screen.exitonclick()