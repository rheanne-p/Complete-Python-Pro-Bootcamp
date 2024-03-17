from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Objects
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

# Variables
turn_on = True

# TODO 1. Print report
print(f"{coffee_maker.report()} + {money_machine.report()}")

while turn_on is True:
    # TODO 2. Prompt user
    order_name = input(f"What would you like to order? ({menu.get_items()}): ")
    if order_name == "report":
        print(f"{coffee_maker.report()} + {money_machine.report()}")
    elif order_name == "off":
        turn_on = False
    else:
        drink_object = menu.find_drink(order_name)
        # the method find_drink takes in an argument of str
        # it returns a value of the type object
        # the object is located in the MenuItem, where all drinks' data are stored
        # TODO 3. Check resources sufficient?
        sufficient_resources = coffee_maker.is_resource_sufficient(drink_object)
        # TODO 4. Check transaction successful?
        if sufficient_resources is True:
            cost = drink_object.cost
            if money_machine.make_payment(cost):
                coffee_maker.make_coffee(drink_object)
