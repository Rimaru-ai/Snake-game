from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 16, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 200)
        self.write(f"GAME OVER\nFinal Score: {self.score}", align="center", font=("Courier", 18, "bold"))
