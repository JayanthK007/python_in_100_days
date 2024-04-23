MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

coins={
    'quarter':.25,
    'dime': .10,
    'nickel': .05,
    'pennies': .01
}
def process_coins(money,choice):
    quarter=float(input('How many quarters?: '))
    dimes=float(input('How many dimes?: '))
    nickels=float(input('How many nickels?: '))
    pennies=float(input('How many pennies?: '))
    total=(quarter*coins['quarter'])+(dimes*coins['dime'])+(nickels*coins['nickel'])+pennies*coins['pennies']
    if total>MENU[choice]['cost']:
        money=round(total-MENU[choice]['cost'],2)
        print(f"Here is ${money} dollars in change.")
        print(f'Here is your {choice} 🍵 Enjoy')
        return MENU[choice]['cost']
    else:
        print("Sorry that's not enough money. Money refunded.")
        return 0

def report(money):
    for key,val in  resources.items():
        if key=='water' or key=='milk':
            print(f'{key}: {val}ml')
        else:    
            print(f'{key}: {val}g')
            print(f'Money: ${money}' ) 

def make_coffee(money,choice):
    for key,val in MENU[choice]['ingredients'].items():
        if(resources[key] < val):
            print(f'Sorry there is not enough {key}')
            return 0
    print("Please insert coins")
    for key,val in MENU[choice]['ingredients'].items():
        resources[key]-=val
    return process_coins(money,choice)   
      



def main():
    money=0
    while True:
        choice=input("What would you like? (espresso/latte/cappuccino):")
        if choice=="off":
            break
        elif choice=="report":
            report(money)
        elif choice=='latte' or choice=='espresso' or choice=='cappuccino':
            money+=make_coffee(money,choice)    


if __name__=="__main__":
    main()