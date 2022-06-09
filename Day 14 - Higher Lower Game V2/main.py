# import modules

import art
import random
from game_data import data
from replit import clear

def choose_celeb_index():
  return random.randint(0,len(data)-1)

def determine_result(a_celeb_count, b_celeb_count, player_guess):
  
  if a_celeb_count > b_celeb_count:
    winning_celeb = "A"
  else:
    winning_celeb = "B"

  if player_guess == winning_celeb:
    return True
  else:
    return False
  
def game_play(a_index):

  keep_playing = True
  current_score = 0

  while keep_playing:
    
    b_index = choose_celeb_index()
    while b_index == a_index:
      print("HOLY CRAP")
      b_index = choose_celeb_index()
  
    print(f"\nCompare A: {data[a_index]['name']}, a {data[a_index]['description']}, from {data[a_index]['country']}.")
    print(art.vs)
    print(f"\nCompare B: {data[b_index]['name']}, a {data[b_index]['description']}, from {data[b_index]['country']}.")
    
    player_guess = input("\nWho has more followers? Type 'A' or 'B': ").upper()
  
    a_celeb_count = data[a_index]['follower_count']
    b_celeb_count = data[b_index]['follower_count']
        
    if determine_result(a_celeb_count, b_celeb_count, player_guess):
      current_score += 1
      a_index = b_index
      clear()
      print(art.logo)
      print(f"\nThat's correct!  You're current score is {current_score}")
    else:
      clear()
      print(art.logo)
      print(f"\nSorry, that is wrong.  You're final score is {current_score}")
      keep_playing = False

a_index = choose_celeb_index()
print(art.logo)
game_play(a_index)
  


