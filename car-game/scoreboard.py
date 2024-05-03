from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-250,250)
        self.score = 0
        self.points()

    def inc_score(self):
        self.score+=1

    def points(self):  
        self.clear()  
        self.write(f"Level : {self.score}",align="left",font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over! ",align="center",font=FONT)