from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


machine_on = True

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()

while machine_on:
    user_choice = input(f"What would you like? {menu.get_items()}: ")

    if user_choice.lower() == "off":
        print("Turning machine off.")
        machine_on = False

    elif user_choice.lower() == "report":
        coffee_maker.report()
        money_machine.report()

    else:
        drink_ingredients = menu.find_drink(user_choice)
        if coffee_maker.is_resource_sufficient(drink_ingredients):
            if money_machine.make_payment(drink_ingredients.cost):
                coffee_maker.make_coffee(drink_ingredients)

    # else:
    #     drink_ingredients = menu.find_drink(user_choice)
    #     if coffee_maker.is_resource_sufficient(drink_ingredients) and money_machine.make_payment(drink_ingredients.cost):
    #         coffee_maker.make_coffee(drink_ingredients)