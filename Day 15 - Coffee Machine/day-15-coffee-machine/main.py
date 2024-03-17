# variables
money = 0
run_machine = True
continue_to_order = True
back_to_start = True

# inventory
water = 300
milk = 200
coffee = 100

# starter query
while back_to_start and run_machine:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    # print report or turn off
    if choice == "off":
        run_machine = False
        continue_to_order = False
    elif choice == "report":
        print(f"Water: {water}ml \nMilk: {milk}ml \nCoffee: {coffee}g \nMoney: ${money}")
        continue_to_order = False

while continue_to_order:
    # checking price and expenses
    if choice == "espresso":
        water_expense = 50
        coffee_expense = 18
        milk_expense = 0
        cost = 1.5
    elif choice == "latte":
        water_expense = 200
        milk_expense = 150
        coffee_expense = 24
        cost = 2.5
    elif choice == "cappuccino":
        water_expense = 250
        milk_expense = 100
        coffee_expense = 24
        cost = 3.0
    # printing price
    print(f"The price for the {choice} is ${cost}0.")
    # insert coins
    print("Please insert coins.")
    quarters = float(input("How many quarters? "))
    dimes = float(input("How many dimes? "))
    nickles = float(input("How many nickles? "))
    pennies = float(input("How many pennies? "))
    sum = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    # checking for change or refund
    if sum > cost:
        change = sum - cost
        money += cost
        print(f"Here is ${round(change, 2)} in change.")
    elif sum < cost:
        print("Sorry that's not enough money. Money refunded.")
        continue_to_order = False
    elif sum == cost:
        money += sum
    if continue_to_order:
        # check for enough resources
        if water - water_expense < 0:
            print("Sorry there is not enough water.")
        elif milk - milk_expense < 0:
            print("Sorry there is not enough milk.")
        elif coffee - coffee_expense < 0:
            print("Sorry there is not enough coffee.")
        else:
            # make drink
            water -= water_expense
            milk -= milk_expense
            coffee -= coffee_expense
            print(f"Here is your {choice} ☕. Enjoy!")