#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password_lets = ""
password_syms = ""
password_nums = ""

for letter in range(1, nr_letters + 1):
  password_lets += letters[random.randint(0,len(letters)-1)]

for symbol in range(1, nr_symbols + 1):
  password_syms +=  symbols[random.randint(0,len(symbols)-1)]

for number in range(1, nr_numbers + 1):
  password_nums += numbers[random.randint(0,len(numbers)-1)]

password = password_lets + password_syms + password_nums
print(f"\n Your easy password is: {password}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

hpassword_lets = ""
hpassword_syms = ""
hpassword_nums = ""

for letter in range(1, nr_letters + 1):
  hpassword_lets += letters[random.randint(0,len(letters)-1)]

for symbol in range(1, nr_symbols + 1):
  hpassword_syms +=  symbols[random.randint(0,len(symbols)-1)]

for number in range(1, nr_numbers + 1):
  hpassword_nums += numbers[random.randint(0,len(numbers)-1)]

temp_password = hpassword_lets + hpassword_syms + hpassword_nums
final_password = ""
total_digits = nr_letters + nr_symbols + nr_numbers

for digit in range(1, total_digits + 1):
  final_password += temp_password[random.randint(0,total_digits - 1)]

print(f"\n Your complex password is: {final_password}")