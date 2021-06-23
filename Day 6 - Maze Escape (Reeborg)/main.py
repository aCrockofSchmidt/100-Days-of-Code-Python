# open this link: https://tinyurl.com/fsbdzk

def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
while front_is_clear():
    move()
turn_left()    

while not at_goal():
    if wall_on_right():        
        if wall_in_front():
            turn_left()
        else:
            move()
    else:
        turn_right()
        move()