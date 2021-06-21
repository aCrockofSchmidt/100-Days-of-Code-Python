import random

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

images = [rock, paper, scissors]

player_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors."))

# if player_choice == 0:
#   print(rock)
# elif player_choice == 1:
#   print(paper)
# else:
#   print(scissors)

print(images[player_choice])

computer_choice = random.randint(0,2)
print("Computer chose:")

# if computer_choice == 0:
#   print(rock)
# elif computer_choice == 1:
#   print(paper)
# else:
#   print(scissors)

print(images[computer_choice])

if player_choice == computer_choice:
  print("Draw")
elif (player_choice == 0 and computer_choice == 2) or (player_choice == 1 and computer_choice == computer_choice == 0) or (player_choice == 2 and computer_choice == 1):
  print("You Win!")
else:
  print("You Lose!")