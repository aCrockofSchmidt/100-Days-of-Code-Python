from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 260)
        self.starting_level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Level: {self.starting_level}", align="left", font=FONT)

    def scorekeeping(self):
        self.clear()
        self.starting_level += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=FONT)

