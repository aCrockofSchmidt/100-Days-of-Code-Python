import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

# create annotation object
annotate = turtle.Turtle()
annotate.penup()
annotate.hideturtle()

# add map image for use as the turtle
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# import raw state data
state_data = pandas.read_csv("50_states.csv")
all_states = state_data.state.to_list()
guessed_states = []
score = 0


game_on = True

while game_on:
    answer_state = screen.textinput(title=f"{score}/50 States Correct", prompt="What's another state's name?")

    # this if statement identifies when the player has clicked cancel rather than entering a state name
    if answer_state is None:
        annotate.goto(0, 0)
        annotate.write("GAME OVER", align="center", font=("Courier", 25, "bold"))
        pandas.DataFrame(all_states).to_csv("states_to_learn.csv")
        game_on = False

    elif answer_state.title() in all_states:
        x_coord = int(state_data.x[state_data.state == answer_state.title()])
        y_coord = int(state_data.y[state_data.state == answer_state.title()])
        annotate.goto(x_coord, y_coord)
        annotate.write(answer_state)
        score += 1
        guessed_states.append(answer_state.title())
        all_states.remove(answer_state.title())

    # this if statement identifies when the player has guessed all fifty states and won the game
    if score == 50:
        annotate.goto(0, 0)
        annotate.write("CONGRATS! You got them all!", align="center", font=("Courier", 25, "bold"))
        game_on = False


# keeps screen open similar to exitonclick but the latter is no good when the game requires mouse clicks
turtle.mainloop()



# the code below finds x/y coords for each state BUT
# this has already been done and included in the CSV file
# def get_mouse_click_coor(x, y):
#     """returns x and y coordinates of mouse click on main screen"""
#     print(x, y)
#
# turtle.onscreenclick(get_mouse_click_coor)
