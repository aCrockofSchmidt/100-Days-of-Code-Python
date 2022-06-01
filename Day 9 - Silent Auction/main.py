from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)

bid_dictionary = {}
continue_bidding = True

def winning_bid(dictionary):
  win_bid = 0

  for key in dictionary:
    if float(dictionary[key]) > win_bid:
      winner = key
      win_bid = float(dictionary[key])
    
  clear()
  print(f"The winning bidder is {winner} with a winning bid of ${win_bid:.2f}.")

while continue_bidding:
  bidder_name = input("What is your name? ")
  bidder_bid = input("What is your bid? $")
  bid_dictionary[bidder_name] = bidder_bid
  print(bid_dictionary)

  more_bids = input("Are there any other bidders (yes or no)? ")
  if more_bids == "no":
    winning_bid(bid_dictionary)
    continue_bidding = False
  else:
    clear()