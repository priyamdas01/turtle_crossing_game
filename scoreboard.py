from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.color("black")
        self.penup()
        self.goto(-210, 260)
        self.update_scoreboard()

    def increase_level(self):
        self.score += 1

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"game over", align="center", font=FONT)
