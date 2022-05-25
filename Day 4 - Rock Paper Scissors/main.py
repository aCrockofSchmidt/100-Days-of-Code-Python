rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

image_list = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for ROCK, 1 for PAPER, or 2 for SCISSORS. "))

if player_choice >= 3 or player_choice < 0:
  print("You chose an invalid number, you lose.")
else:
  print(image_list[player_choice])

  computer_choice = int(random.randint(0,2))
  print("\nComputer chose " + image_list[computer_choice])


  if player_choice == computer_choice:
    print("Tie")
  elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
    print("You Win!")
  else:
    print("You Lose")