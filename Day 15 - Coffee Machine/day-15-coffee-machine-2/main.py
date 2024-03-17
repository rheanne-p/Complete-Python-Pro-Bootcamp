# Data Module
from data import REQUIRED

# Inventory
water = 300
milk = 200
coffee = 100
money = 0


# Report Function
def report():
    global water
    global milk
    global coffee
    global money
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    print(f"Money: ${money}")


# Turn On Variable
turn_on = True

# Prompt User Function
user_choice = ""


def prompt_user():
    global user_choice
    global turn_on
    user_choice = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if user_choice == "espresso" or user_choice == "latte" or user_choice == "cappuccino":
        turn_on = True
    elif user_choice == "report":
        report()
        prompt_user()
    elif user_choice == "off":
        print("Turning off.")
        turn_on = False
        return turn_on
    else:
        print("That's not a valid input.")
        return prompt_user()


# Check Resources Function
def check_resources():
    global user_choice
    if water < REQUIRED[user_choice]["water"]:
        print("Sorry there is not enough water.")
        return prompt_user()
    if milk < REQUIRED[user_choice]["milk"]:
        print("Sorry there is not enough milk.")
        return prompt_user()
    if coffee < REQUIRED[user_choice]["coffee"]:
        print("Sorry there is not enough coffee.")
        return prompt_user()


# Check Money Function
paid_amount = 0


def check_money():
    global money
    if paid_amount < cost:
        print("Sorry that's not enough money.")
        return prompt_user()
    elif paid_amount > cost:
        change = paid_amount - cost
        change = round(change, 2)
        money += cost
        print(f"Here is ${change} in change.")
    else:
        money += paid_amount


# Operating Coffee Machine
# TODO 1. Prompt user
prompt_user()
# TODO 0: Try prompting user within loop, not within function (4:40)

while turn_on is True:
    # TODO 2. Check if enough resources
    check_resources()
    # TODO 3. Process coins
    cost = REQUIRED[user_choice]["cost"]
    print(f"It costs ${cost}. Please insert coins.")
    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickles = int(input("How many nickles?: "))
    pennies = int(input("How many pennies?: "))
    paid_amount = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    check_money()
    # TODO 4. Make coffee, subtract resources
    water -= REQUIRED[user_choice]["water"]
    milk -= REQUIRED[user_choice]["milk"]
    coffee -= REQUIRED[user_choice]["coffee"]
    # TODO 5. Serve drink, after repeats loop
    print(f"Here is your {user_choice} ☕. Enjoy!")
    # TODO 6. Prompt user again
    prompt_user()
    # 4:07 new!!!