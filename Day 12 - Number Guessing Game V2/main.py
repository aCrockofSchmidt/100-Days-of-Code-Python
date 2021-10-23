"""
My original solution for this task was short and eloquent (?) but did not make use of any functions. The instructors solution DID use functions. That solution was longer and perhaps a bit uglier, but it's possible that means it's a better solution in this instance. Regardless, I'd like to refactor my original code to utilize functions
"""

import random
import art

# determine the number of turns a player gets to solve puzzle
def set_difficulty():
  difficulty = input("\nChoose the difficulty level. Type 'easy' or 'hard': ")
  if difficulty == 'easy':
    return 10
  else:
    return 5

# determine if players guess is correct
def check_guess(guess, number, turns):
  if guess > number:
    print("Too High!")
    return turns - 1
  elif guess < number:
    print("Too Low!")
    return turns - 1
  else:
    print(f"\nThat's the number! It was {number}. CONGRATS!")

# establishes the game play sequence
def play_game():
  print(art.logo)
  print("\nWelcome to the Number Guessing Game!\nI am thinking of a number (integers only) between 1 and 100")

  number = random.randint(1,100)
  guess = 0
  turns = set_difficulty()

  # print(f"\nPssst ... the number is {number}")
 
  while guess != number:
    print(f"\nYou have {turns} turns remaining.")
    guess = int(input("\nGuess a number: "))
    
    turns = check_guess(guess, number, turns)

    if turns == 0:
      print("\nSorry, but you are out of turns. You lose the game.")
      return
    elif guess != number:
      print("Guess again!")

# start game play
play_game()