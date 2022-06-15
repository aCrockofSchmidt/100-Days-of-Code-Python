from turtle import Turtle

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("orange")
        self.penup()
        self.x_move = 5
        self.y_move = 5
        self.speed_of_ball = 0.1

    def ball_move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def ball_bounce(self):
        self.y_move *= -1

    def paddle_bounce(self):
        self.x_move *= -1
        self.speed_of_ball *= 0.9

    def ball_reset(self):
        self.goto(0, 0)
        self.speed_of_ball = 0.1
        self.paddle_bounce()

