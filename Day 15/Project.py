from main import MENU, resources


def statement_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_ingredient(ingredient, coffee):
    if MENU[coffee]['ingredients'][ingredient] <= resources[ingredient]:
        return True
    return False


def sum_up():
    amount_in_dollars = (quarters / 4) + (dimes / 10) + (nickels / 20) + (pennies / 100)
    return amount_in_dollars


def remove_from_resource(coffee_type):
    resources["water"] -= MENU[coffee_type]['ingredients']['water']
    resources["coffee"] -= MENU[coffee_type]['ingredients']['coffee']
    if not order == 'espresso':
        resources["milk"] -= MENU[coffee_type]['ingredients']['milk']


def enough_resource(coffee_type):
    if coffee_type == "espresso":
        if check_ingredient("water", coffee_type) and check_ingredient("coffee", coffee_type):
            return True
        return False
    elif not order == 'espresso':
        if check_ingredient("water", coffee_type) and check_ingredient("milk", coffee_type) \
                and check_ingredient("coffee", coffee_type):
            return True
        return False


def can_buy(coffee_type):
    return amount_paid >= MENU[coffee_type]['cost']


def run_machine(coffee_type):
    remove_from_resource(coffee_type)
    change = "{:.2f}".format(amount_paid - MENU[coffee_type]['cost'])
    print(f"Here is ${change} in change.")
    print(f"Here is your {order} ☕. Enjoy!")


def failed_output_statement(coffee_type):
    unavailable_ingredients = []
    for ingredient in resources:
        if coffee_type == "espresso" and ingredient == "milk":
            break
        elif not check_ingredient(ingredient, coffee_type):
            unavailable_ingredients.append(ingredient)
    print(f"sorry, there is not enough {' & '.join(unavailable_ingredients)}")


money = 0
machine_on = True

while machine_on:
    order = input("Hi there! I'm a Coffee Machine.\nWhat would you like? (espresso/latte/cappuccino): ").lower()
    if (order == 'latte') or (order == 'espresso') or (order == 'cappuccino'):
        if enough_resource(order):
            print("Please insert coins.")
            quarters = int(input("How many quarters?: "))
            dimes = int(input("How many dimes?: "))
            nickels = int(input("How many nickels?: "))
            pennies = int(input("How many pennies?: "))
    if order == "report":
        statement_report()

    elif order == "espresso" or order == 'latte' or order == 'cappuccino':
        if enough_resource(order):
            amount_paid = sum_up()
            if can_buy(order):
                money += MENU[order]['cost']
                run_machine(order)
            else:
                print("Sorry that's not enough money. Money refunded.👀")
        else:
            failed_output_statement(order)

    elif order == 'refill':
        resources["water"] = 300
        resources["milk"] = 200
        resources["coffee"] = 100

    elif order == "off":
        machine_on = False

    else:
        print("You have entered an invalid input. Try again? 🙂")
