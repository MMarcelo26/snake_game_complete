from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.write(f"Placar: {self.score}", align=ALIGNMENT, font=FONT)
        self.hideturtle()

    def mudar_score(self):
        self.write(f"Placar: {self.score}", align=ALIGNMENT, font=FONT)

    def aumentar_score(self):
        self.score += 1
        self.clear()
        self.mudar_score()
        self.write(f"Placar: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",align=ALIGNMENT, font=FONT)