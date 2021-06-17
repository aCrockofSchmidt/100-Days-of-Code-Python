print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

left_right = input("\nTo begin your journey, you must choose a direction to head off in.\n Type 'left' or 'right' to start the hunt! ")

if left_right.lower() != "left":
  print("\nOh no! You've fallen into a chasm and died. **GAME OVER**")
else:
  swim_wait = input("\nYour progress has been stymied by a smelly, green lake.\n Do you wish to swim across it or wait to ride across on the troll ferry?\n Type 'swim' or 'wait' to continue. ")

  if swim_wait.lower() != "wait":
    print("\nOh no! You've been sucked into the abyss and died. **GAME OVER**")
  else:
    which_door = input("\nYou've arrived at a mysterious castle which has three doors.\n Each door is a different colour.\n Type 'yellow', 'red', or 'blue' to choose a door. ")

    if which_door.lower() == "red":
      print("\nOh no! You've tumbled into a pit of lava and died. **GAME OVER**")
    elif which_door.lower() == "blue":
      print("\nOh no! You've been disemboweled by a hideous creature and died. **GAME OVER**")
    elif which_door.lower() == "yellow":
      print("\nCongratulations! You've found the treasure. **YOU WIN**")
    else:
      print("\nYou don't follow instructions well.\n **GAME OVER**")



#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload