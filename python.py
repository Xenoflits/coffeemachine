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
    "water": 30,
    "milk": 200,
    "coffee": 100,
}

total_coins = 0
machine_on = True

#functions
def check_resources(option):
    if option['water'] > resources['water']:
        return 0, 'water'
    elif option['milk'] > resources['milk']:
        return 0, 'milk'
    elif option['coffee'] > resources['coffee']:
        return 0, 'coffee'
    return 1, 'null'

def calculate_coin_amount():
    return

def turn_off_machine():
    return

def print_report():
    print(f' Water: {resources['water']}ml\n Milk: {resources['milk']}ml\n Coffee: {resources['coffee']}g\n Money: ${total_coins} \n')
    return

def make_coffee():
    return



def main():
    global machine_on
    option = input("What would you like? (espresso/latte/cappuccino)")
    if option == "espresso" or option == "latte" or option == "cappuccino":
        ingredients = MENU[option]['ingredients']
        price = MENU[option]['cost']
        a,b = check_resources(ingredients)
        if a != 0:
            print('resources enough')
        else:
            print(f'Not enough {b}. Shutting off machine')
            machine_on = False
    elif option == 'off':
        machine_on = False
    elif option == 'report':
        print_report()
    
        

    
        return

#main
while machine_on:
    main()