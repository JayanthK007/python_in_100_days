import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player=Player()
score=Scoreboard()
car=CarManager()

screen.listen()
screen.onkey(player.move,'Up')

game_is_on = True


while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_car()
    #detect turtle crossed all cars
    if player.ycor()==player.endline():
        score.inc_score()
        score.points()
        player.goto(0,-280)
        car.level_up()

    #detect collison with car 
    for cars in car.all_cars:
        if player.distance(cars)<30:
            score.game_over() 
            game_is_on=False

screen.exitonclick()

