from replit import clear
from art import logo

print(logo)

bid_dictionary = {}
replay = "yes"

while replay == "yes":
  bidder = input("What is your name? ")
  bid = input ("What is your bid? $")
  bid_dictionary[bidder] = bid
  replay = input("Are there any more bidders (yes or no)? ")
  clear()

winning_bid = 0
winning_name = ""

for name in bid_dictionary:
  if float(bid_dictionary[name]) > winning_bid:
    winning_bid = float(bid_dictionary[name])
    winning_name = name

print(f"Winner is {winning_name.upper()} with a winning bid of ${winning_bid:.2f}")





