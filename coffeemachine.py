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

total_coins = 0
machine_on = True

#functions
def check_resources(option):
    ingredients = MENU[option]['ingredients']
    if ingredients.get('water', 0) > resources['water']:
        return 0, 'water'
    elif ingredients.get('milk', 0) > resources['milk']:
        return 0, 'milk'
    elif ingredients.get('coffee', 0) > resources['coffee']:
        return 0, 'coffee'
    return 1, 'null'

def commands():
    global machine_on
    
    option = input("What would you like? (espresso/latte/cappuccino)")
    #options commands
    if option == "espresso" or option == "latte" or option == "cappuccino":
        ingredients = MENU[option]['ingredients']
        a,b = check_resources(option)
        if a != 0:
            print('\n')
        else:
            print(f'Not enough {b}. Shutting off machine')
            machine_on = False
    #off command
    elif option == 'off':
        machine_on = False
    #report command
    elif option == 'report':
        print_report()
    return option

def payment(cost):
    global machine_on
    quarters = int(input('Please insert x quarters 0.25: '))
    dimes = int(input('Please insert x dimes 0.10: '))
    nickels = int(input('Please insert x nickels 0.05: '))
    pennies = int(input('Please insert x pennies 0.01: '))
    total = quarters*0.25+dimes*0.10+nickels*0.05+pennies*0.01
    if cost > total:
        print('not enough money, refunded')
        machine_on = 0
    else:
        print(f'total amount inserted: {total:.2f}. Returning {total - cost:.2f}')
    
    return

def turn_off_machine():
    return

def print_report():
    print(f' Water: {resources['water']}ml\n Milk: {resources['milk']}ml\n Coffee: {resources['coffee']}g\n Money: ${total_coins} \n')
    return

def make_coffee(option):
    global resources
    print(f"Enjoy your: {option}")
    ingredients = MENU[option]['ingredients']
    resources['water'] -= ingredients.get('water',0)
    resources['milk'] -= ingredients.get('milk',0)
    resources['coffee'] -= ingredients.get('coffee',0)

    
    return



def main():
    
    if machine_on:
        option = commands()
    if machine_on:
        cost = MENU[option]['cost']
        print(f'Cost of {option}: ${cost} ')
    if machine_on:
        payment(cost)
    if machine_on:
        make_coffee(option)

    
        

#main
while machine_on:
    main()