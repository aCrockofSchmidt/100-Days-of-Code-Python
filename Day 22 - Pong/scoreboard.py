from turtle import Turtle
ALIGN = "center"
FONT = ("Courier", 50, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("red")
        self.penup()
        self.goto(0, 200)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"{self.left_score}        {self.right_score}", align=ALIGN, font=FONT)

    def current_score(self, x_coord):
        self.clear()
        if x_coord > 0:
            self.left_score += 1
            self.update_scoreboard()
        else:
            self.right_score += 1
            self.update_scoreboard()

    def game_over(self, winner):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGN, font=FONT)
        self.goto(0, -30)
        self.write(f"{winner}", align="center", font=("Courier", 30, "normal"))
