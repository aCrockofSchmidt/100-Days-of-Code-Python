#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
import art

print(art.logo)

print("\nWelcome to the Number Guessing Game!\nI am thinking of a number (integers only) between 1 and 100")

difficulty = input("\nChoose the difficulty level. Type 'easy' or 'hard': ")

if difficulty == 'easy':
  turn = 10
else:
  turn = 5

number = random.randint(1,100)

while turn > 0:
  print(f"\nYou have {turn} turns remaining.")
  guess = int(input("\nGuess an number: "))
  
  if guess > number:
    print("Too High!")
  elif guess < number:
    print("Too Low!")
  else:
    print(f"\nThat's the number! It was {number}. CONGRATS!")
    turn = -1
  
  turn -= 1

if turn == 0:
  print("\nSorry, but you are out of turns. You lose the game.")
