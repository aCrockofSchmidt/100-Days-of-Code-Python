from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()

# setup screen

screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("PONG")
screen.tracer(0)

# setup paddle

l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))

# setup ball

ball = Ball()

# setup scoreboard

scoreboard = Scoreboard()

# move paddle

screen.listen()
screen.onkeypress(l_paddle.move_up, "w")
screen.onkeypress(l_paddle.move_down, "s")
screen.onkeypress(r_paddle.move_up, "Up")
screen.onkeypress(r_paddle.move_down, "Down")


game_is_on = True
while game_is_on:
    time.sleep(ball.speed_of_ball)
    screen.update()
    ball.ball_move()

    # detect collision with screen

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.ball_bounce()

    # detect collision with right paddle

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 and ball.x_move > 0\
            or ball.distance(l_paddle) < 50 and ball.xcor() > -320 and ball.x_move < 0:
        ball.paddle_bounce()

    # detect missed ball

    if ball.xcor() > 380 or ball.xcor() < -380:
        scoreboard.current_score(ball.xcor())

        # determine if game is over
        if scoreboard.left_score == 10 and scoreboard.left_score > scoreboard.right_score:
            scoreboard.game_over("Left Paddle Wins!")
            game_is_on = False
        elif scoreboard.right_score == 10 and scoreboard.right_score > scoreboard.left_score:
            scoreboard.game_over("Right Paddle Wins!")
            game_is_on = False
        else:
            ball.ball_reset()



screen.exitonclick()
