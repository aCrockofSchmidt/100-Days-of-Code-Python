#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random
from replit import clear

EASY = 10
HARD = 5

def difficulty_setting():
  """determines the number of guesses a player is allowed"""
  difficulty = input("\nChoose a difficulty. Type 'easy' or 'hard': ")
  
  if difficulty == "easy":
    return EASY
  else:
    return HARD

def evaluate_guess(turns, number_to_guess):
  """evaluates the player's guess and returns feedback"""
  while turns > 0:
    print(f"\nYou have {turns} turns remaining to guess the number.")
    player_guess = int(input("\nMake a guess: "))
    if player_guess > number_to_guess:
      print("Too high.")
    elif player_guess < number_to_guess:
      print("Too low.")
    else:
      return "\nYou got it!"
    turns -= 1
  return "\nYou ran out of turns. You lose."

def game_play():
  """basic game play"""
  clear()
  print(logo)

  print("\nWelcome to the Number Guessing Game!")
  print("\nI'm thinking of a number between 1 and 100.")
  
  number_to_guess = random.randint(1,100)
  print(f"\nPsst. {number_to_guess} is the random number.")
  
  turns = difficulty_setting()

  print(evaluate_guess(turns, number_to_guess) + f" The number was {number_to_guess}") 


continue_playing = True

while continue_playing:
  want_to_play = input("\nWould you like to play a number guessing game ('yes' or 'no'): ")
  if want_to_play == "no":
    print("\nGoodbye")
    continue_playing = False
  else:
    game_play()
