from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine


def main():
    is_on=True
    coffee=CoffeeMaker()
    money=MoneyMachine()
    menu=Menu()
    while is_on:
        choice=input(f"What would you like? ({menu.get_items()}):")
        if choice=="off":
            is_on=False
        elif choice=="report":
            coffee.report()
            money.report()
        elif choice in menu.get_items():
            drink= menu.find_drink(choice)
            if coffee.is_resource_sufficient(drink) and money.make_payment(drink.cost):
                coffee.make_coffee(drink)




if __name__=='__main__':
    main()