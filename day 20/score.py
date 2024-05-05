from turtle import Turtle
ALIGNMENT='center'
FONT=("Arial", 14, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.goto(0, 280)
        self.penup()
        self.hideturtle()
        self.color("white")
        self.value = 0
        with open("data.txt") as file:
            self.high_score=file.read()
        self.update_score()

    def update_score(self):
        self.clear()  # Clear the previous score before updating
        with open("data.txt") as file:
            self.high_score=file.read()
        self.write(f"score = {self.value} High Score = {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.value>int(self.high_score):
            with open("data.txt",'w') as file:
                file.write(str(self.value))
        self.value=0
        self.update_score()        

    # def game_over(self):
    #     self.goto(0,0)
    #     self.write("GAME OVER!",align=ALIGNMENT,font=FONT)    

    def increase_score(self):
        self.value += 1
        self.update_score()
