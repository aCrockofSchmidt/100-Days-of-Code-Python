# import colorgram

# extract the colors from the chosen image

# colors = colorgram.extract("hirst_image.jpg", 1000)
#
# color_palette = []
#
# for item in range(len(colors)):
#     color_tuple = (colors[item].rgb.r, colors[item].rgb.g, colors[item].rgb.b)
#     color_palette.append(color_tuple)
#
# print(color_palette)


# create a dot painting based on a Damien Hirst original

from turtle import Turtle, Screen
from random import choice

# create object and establish initial attributes

tim = Turtle()
tim.shape("turtle")
tim.speed(10)
tim.penup()
tim.screen.colormode(255)


def start_coord(z):
    """this function takes user dot count 'z' and determines a starting coordinate"""
    start = z * -50 / 2
    return start


def draw_painting(x_dots, y_dots):
    """this function takes user input for number of dots and creates a painting using random colours"""

# colour palette derived from online image using colorgram module

    color_list = [(36, 107, 165), (243, 78, 38), (152, 57, 85), (113, 163, 210), (219, 155, 91), (200, 61, 27),
              (25, 132, 58), (246, 204, 76), (224, 119, 152), (183, 150, 53), (46, 53, 121), (220, 69, 98),
              (114, 198, 156), (147, 36, 29), (91, 113, 191), (73, 40, 33), (111, 42, 50), (252, 203, 0),
              (247, 154, 144), (156, 212, 202), (38, 32, 66), (155, 210, 219), (44, 34, 46), (35, 55, 46),
              (56, 173, 161), (98, 93, 3), (44, 156, 187), (10, 111, 51), (229, 169, 182), (177, 186, 218),
              (8, 113, 119)]

# determine starting coordinates for turtle

    x_start = start_coord(x_dots)
    y_start = start_coord(y_dots)
    tim.goto(x_start, y_start)

# draw dot painting

    for up in range(y):
        up = y_start + up * 50

        for over in range(x):
            over = x_start + over * 50
            tim.goto(over, up)
            tim.dot(20, choice(color_list))

# ask for number of dots to create based on X - Y grid

x = int(tim.screen.numinput("X-Axis", "How many dots along x-axis (input integer)? "))
y = int(tim.screen.numinput("Y-Axis", "How many dots along y-axis (input integer)? "))

# run program

draw_painting(x, y)
tim.hideturtle()

screen = Screen()
screen.exitonclick()
