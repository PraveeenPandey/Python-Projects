from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()

is_on = True

while is_on :
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()
    if choice == "off" :
        is_on = False
    elif choice == "report" :
        print(coffee_maker.report())
        print(money_machine.report())
    else:
        drink = menu.find_drink(choice)
        is_ingredients_sufficient = coffee_maker.is_resource_sufficient(drink)
        is_payment = money_machine.make_payment(drink.cost)
        if is_ingredients_sufficient and is_payment :
            make_cofee = coffee_maker.make_coffee(drink)
