alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


    #TODO-3: What happens if the user enters a number/symbol/space?
    #Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
    #e.g. start_text = "meet me at 3"
    #end_text = "•••• •• •• 3"

def caesar(entered_text, shift_amount, cipher_direction):
  output = ""
  if cipher_direction == "encode":
    for i in range(len(entered_text)):
      if entered_text[i] not in alphabet:
        output += entered_text[i]
      elif (alphabet.index(entered_text[i]) + shift_amount) > 25:
        output += alphabet[(alphabet.index(entered_text[i]) + shift_amount) - 26]
      else:
        output += alphabet[alphabet.index(text[i]) + shift]

  elif cipher_direction == "decode":
    for i in range(len(entered_text)):
      if entered_text[i] not in alphabet:
        output += entered_text[i]
      elif (alphabet.index(entered_text[i]) - shift_amount) < 0:
        output += alphabet[(alphabet.index(entered_text[i]) - shift_amount) + 26]
      else:
        output += alphabet[alphabet.index(entered_text[i]) - shift_amount]

  print(f"The {cipher_direction}d text is {output}.")

#TODO-1: Import and print the logo from art.py when the program starts.

from art import logo
print(logo) 

#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'.

replay = "yes"
while replay == "yes":
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))

#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).

  shift = shift % 26
  caesar(entered_text = text, shift_amount = shift, cipher_direction = direction)

  replay = input("\nType 'yes' to play again. Otherwise, type 'no'.\n")

print("goodbye and stay hidden")