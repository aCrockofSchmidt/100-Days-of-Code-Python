MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# adding a dictionary to track income
# this could just as easily have been added to the existing resources library
# but I wanted to keep it separate to show that it was something I added to existing start code from class
#
# after watching teacher solution, I learned what needed to be done to avoid using a new dictionary for income
# I needed to specify "global" with my variable inside the function .... d'oh!
#
#income = {
#    "total_income": 0
#}

def check_transaction(choice, total_inserted):
    """this function receives the users order and total money inserted
    determines if they've submitted enough money, calculated any change,
    and if order is fullfilled it subtracts used ingredients from resources library"""

    if MENU[choice]['cost'] > total_inserted:
        print("Sorry, that's not enough money. Money refunded.")
    else:
        customer_change = total_inserted - MENU[choice]['cost']
        print(f"Here is your change ${customer_change:.2f}")

        resources['water'] -= MENU[choice]['ingredients']['water']
        if choice != "espresso":
            resources['milk'] -= MENU[choice]['ingredients']['milk']
        resources['coffee'] -= MENU[choice]['ingredients']['coffee']
        global total_income
        total_income += MENU[choice]['cost']

        print(f"Here is your {choice}. Enjoy!\n")

def ask_for_coins(choice):
    """this function receives the user order and asks for payment
    and then determines total payment made"""

    print("Please insert coins.")

    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    total_inserted = quarters * 0.25 + dimes * 0.10 + nickels * 0.05 +  pennies * 0.01

    check_transaction(choice, total_inserted)

def check_resources(choice):
    """this function receives user order and determines if there are enough resources available to fulfill order"""

    if resources['water'] < MENU[choice]['ingredients']['water']:
        print("Sorry, there is not enough water.")
    elif choice != "espresso" and resources['milk'] < MENU[choice]['ingredients']['milk']:
        print("Sorry, there is not enough milk.")
    elif resources['coffee'] < MENU[choice]['ingredients']['coffee']:
        print("Sorry, there is not enough coffee.")
    else:
        ask_for_coins(choice)

machine_on = True
total_income = 0

while machine_on == True:
    customer_choice = input("What would you like? (espresso/latte/cappuccino): ")

    if customer_choice.lower() == "off":
        print("Turning off machine.")
        machine_on = False

    elif customer_choice.lower() == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']} g")
        print(f"Money: ${total_income}")

    else:
        check_resources(customer_choice)
