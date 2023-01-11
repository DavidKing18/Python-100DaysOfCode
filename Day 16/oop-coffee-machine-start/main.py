from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffeeMachine = CoffeeMaker()
coffeeMenu = Menu()
CashierMachine = MoneyMachine()

run_machine = True
while run_machine:
    choice = input('What would you like? (espresso/latte/cappuccino/): ').lower()
    if choice == 'off':
        run_machine = False
    elif choice == 'report':
        coffeeMachine.report()
        CashierMachine.report()
    elif choice == "espresso" or choice == 'latte' or choice == 'cappuccino':
        drink = coffeeMenu.find_drink(choice)
        if coffeeMachine.is_resource_sufficient(drink):
            if CashierMachine.make_payment(drink.cost):
                coffeeMachine.make_coffee(drink)
    else:
        print('You have entered an invalid input. Again?🙂')