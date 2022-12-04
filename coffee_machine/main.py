from data_file import MENU, resources
from artwork import logo


def turn_off_machine():
    return False


def machine_initialization():
    return [MENU, resources]


def get_report(available_resources):
    return f"Water: {available_resources['water']}ml\nMilk: {available_resources['milk']}ml\n" \
           f"Coffee: {available_resources['coffee']}g\nMoney: ${available_resources['money']} "


def check_resources(available_resources, requirement):
    for ingredient in requirement:
        if available_resources[ingredient] < requirement[ingredient]:
            print(f"Sorry there is not enough {ingredient.capitalize()}.")
            return False
    return True


def process_coins():
    """takes coins and return total amount collected"""
    print("Please insert coins.")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickles = int(input("How many nickles? "))
    pennies = int(input("How many pennies? "))
    return (quarters * 0.25) + (0.1 * dimes) + (0.05 * nickles) + (0.01 * pennies)


def make_transaction(amount_received, cost_of_drink, available_resources):
    if amount_received >= cost_of_drink:
        available_resources["money"] += cost_of_drink
        return True
    else:
        return False


def issue_refund(received_amount, cost):
    refund = received_amount - cost
    return round(refund, 2)


def make_drink(recipe, available_resources):
    ingredients = recipe["ingredients"]
    for ingredient in ingredients:
        available_resources[ingredient] -= ingredients[ingredient]
    return available_resources


def turn_on_machine():
    print(logo)
    boostrap_state = machine_initialization()
    menu = boostrap_state[0]
    available_resources = boostrap_state[1]
    is_machine_on = True

    while is_machine_on:
        user_selection = input("What would you like? (espresso/latte/cappuccino): ").lower()
        if user_selection == "off":
            print("Turning off, Have a nice day!")
            is_machine_on = turn_off_machine()
        elif user_selection == "report":
            print(get_report(available_resources))
        elif user_selection == "espresso" or user_selection == "latte" or user_selection == "cappuccino":
            is_available = check_resources(available_resources, menu[user_selection]["ingredients"])
            if not is_available:
                print("Money Refunded.")
            else:
                print(f"The price for {user_selection} is ${menu[user_selection]['cost']}")
                received_amount = process_coins()
                is_transaction_successful = make_transaction(received_amount, menu[user_selection]["cost"],
                                                             available_resources)
                if is_transaction_successful:
                    available_resources = make_drink(menu[user_selection], available_resources)
                    refund = issue_refund(received_amount, menu[user_selection]["cost"])
                    if refund > 0:
                        print(f"Here is ${refund} in change.")
                    print(f"Here is your {user_selection.capitalize()}. Enjoy! ”")
                else:
                    print("Sorry that's not enough money. Money refunded.")
        else:
            print("You have entered an invalid option. Please select a correct option from the menu")


turn_on_machine()
