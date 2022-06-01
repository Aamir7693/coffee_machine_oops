from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine
mymenu=Menu()
money=MoneyMachine()
mycoffee=CoffeeMaker()
inp=input(f"What would you like to drink :{mymenu.get_items()}")
drink=mymenu.find_drink(inp)
is_on=True

while(is_on)
if drink:

    if mycoffee.is_resource_sufficient(drink):
        cond=money.make_payment(drink.cost)
        if cond==True:
            print(mycoffee.make_coffee(drink))


