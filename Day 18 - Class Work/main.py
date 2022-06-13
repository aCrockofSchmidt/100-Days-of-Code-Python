from turtle import Turtle, Screen

tim = Turtle()
tim.shape("turtle")
# tim.color("orangered")

# draw a 100 x 100 square

# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
# tim.right(90)
# tim.forward(100)
#
# for _ in range(4):
#     tim.forward(100)
#     tim.left(90)

# draw a dashed line

# for _ in range(50):
#     tim.pendown()
#     tim.forward(5)
#     tim.penup()
#     tim.forward(5)

# draw a triangle, square, pentagon, hexagon, heptagon, octagon, nonagon, and decagon - each random color, 100 length

# import random
#
# for sides in range(3, 11):
#     angle = 360 / sides
#     #tim.color(random.random(), random.random(), random.random())
#     tim.screen.colormode(255)
#     tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#
#     for _ in range(sides):
#         tim.forward(100)
#         tim.right(angle)

# create a random walk with random colors, thicker lines, faster speed

# import random
#
# orientation = [0, 90, 180, 270]
# tim.speed(0)
# tim.width(7)
#
# for _ in range(250):
#     tim.screen.colormode(255)
#     tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
#     tim.setheading(random.choice(orientation))
#     tim.forward(25)

# make a spirograph

import random

tim.speed(0)

def draw_circle(orientation):
    tim.screen.colormode(255)
    tim.color(random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    tim.setheading(orientation)
    tim.circle(100)

for angle in range(0,361,5):
    draw_circle(angle)

screen = Screen()
screen.exitonclick()
