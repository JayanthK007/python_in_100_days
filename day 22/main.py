from turtle import Turtle,Screen
from paddle import Paddle
from ball import Ball
import time
from score import ScoreBoard

screen=Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title("Pong Game")
screen.tracer(0) 

paddle_1=Paddle(370,0)
paddle_2=Paddle(-370,0)
ball=Ball()
left_score=ScoreBoard(-100,200)
right_score=ScoreBoard(100,200)


screen.listen()
screen.onkey(paddle_1.move_forward,"Up")
screen.onkey(paddle_1.move_backward,"Down")
screen.onkey(paddle_2.move_forward, "w")
screen.onkey(paddle_2.move_backward, "s")


is_game_on=True
left_score.start()
right_score.start()
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    

    # detect collision with the wall
    if -280>ball.ycor() or ball.ycor()>280:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(paddle_1)<50 and ball.xcor()>340 or ball.distance(paddle_2)<50 and  ball.xcor()<-340 :
        ball.bounce_x()   

    #detect if player miss ball
    if ball.xcor()>380:
        ball.reset_pos()
        left_score.l_points()

    if  ball.xcor()<-380:
        ball.reset_pos()
        right_score.r_points()

screen.exitonclick()

