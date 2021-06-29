from replit import clear
from art import logo
print(logo)

# ADD function
def add(n1, n2):
  return n1 + n2

# SUBTRACT function
def subtract(n1, n2):
  return n1 - n2

# MULTIPLY function
def multiply(n1, n2):
  return n1 * n2

# DIVIDE function
def divide(n1, n2):
  return n1 / n2

# EXPONENT function
def exponent(n1,n2):
  return n1 ** n2

# operations dictionary
operations = {
  "+":add,
  "-":subtract,
  "*":multiply,
  "/":divide,
  "^":exponent
  }

# recursion function

def calculator():

# first input question

  num1 = float(input("What's the first number? "))

# operation question

  for symbol in operations:
    print(symbol)

# replay until user declines

  should_continue = True

  while should_continue:
    operation_symbol = input("Pick an operation: ")

# second input question

    num2 = float(input("What's the next number? "))

# calculate

    answer = operations[operation_symbol](num1, num2)

    print(f"{num1} {operation_symbol} {num2} = {answer}")

# inquiry to continue

    if input(f"\nType 'y' to continue calculating with {answer},\n or type 'n' to start a new calculation: ") =='y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()

calculator()