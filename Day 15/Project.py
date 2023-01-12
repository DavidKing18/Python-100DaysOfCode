from main import MENU, resources


def statement_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_water(coffee):
    if MENU[coffee]['ingredients']['water'] <= resources['water']:
        return True
    return False


def check_milk(coffee):
    if MENU[coffee]['ingredients']['milk'] <= resources['milk']:
        return True
    return False


def check_coffee(coffee):
    if MENU[coffee]['ingredients']['coffee'] <= resources['coffee']:
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
        if check_water(coffee_type) == check_coffee(coffee_type) == True:
            return True
        return False
    elif not order == 'espresso':
        if check_water(coffee_type) == check_milk(coffee_type) == check_coffee(coffee_type) == True:
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
    if coffee_type == 'espresso':
        if check_water(coffee_type) == check_coffee(coffee_type) == True:
            print("Sorry, there is not enough water nor coffee.")
        elif not check_water("espresso"):
            print("Sorry, there is not enough water.")
        elif not check_coffee("espresso"):
            print("Sorry, there is not enough milk.")
    else:
        if check_water(coffee_type) == check_milk(coffee_type) == check_coffee(coffee_type) == True:
            print("Sorry, there is not enough water, coffee nor milk.")
        elif check_water(coffee_type) == check_milk(coffee_type) == False:
            print("Sorry, there is not enough water nor milk.")
        elif check_water(coffee_type) == check_coffee(coffee_type) == False:
            print("Sorry, there is not enough water nor coffee.")
        elif check_milk(coffee_type) == check_coffee(coffee_type) == False:
            print("Sorry, there is not enough coffee nor milk.")
        elif not check_water(coffee_type):
            print("Sorry, there is not enough water.")
        elif not check_milk(coffee_type):
            print("Sorry, there is not enough milk.")
        elif not check_coffee(coffee_type):
            print("Sorry, there is not enough cofffee.")


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

    elif order == 'espresso':
        if enough_resource(order):
            amount_paid = sum_up()
            if can_buy(order):
                money += MENU[order]['cost']
                run_machine(order)
            else:
                print("Sorry that's not enough money. Money refunded.👀")
        else:
            failed_output_statement(order)

    elif order == 'latte':
        if enough_resource(order):
            amount_paid = sum_up()
            if can_buy(order):
                money += MENU[order]['cost']
                run_machine(order)
            else:
                print("Sorry that's not enough money. Money refunded.👀")
        else:
            failed_output_statement(order)

    elif order == 'cappuccino':
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
        print("You have entered an invalid input. Again? 🙂")
