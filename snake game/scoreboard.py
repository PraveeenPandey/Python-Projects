from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 24, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Score is {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def update_scoreboard(self):
        self.write(f"Score is {self.score}", align=ALIGNMENT, font=FONT)

    def track_score(self):
        self.score += 10
        self.clear()
        self.update_scoreboard()
        
    def game_over(self):
        self.goto(0, 0)
        self.write("Game Over", align="center", font=FONT)
        
