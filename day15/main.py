#COFFEE MACHINE

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
profit = 0

def is_resource_enough(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Not enough {item}")
            return False
    return True

def process_coins():
    total = int(input("Enter pound coins: ")) * 1
    total += int(input("Enter fifty pence coins: ")) * 0.5
    total += int(input("Enter twenty pence coins: ")) * 0.2
    total += int(input("Enter ten pence coins: ")) * 0.1
    total += int(input("Enter five pence coins: ")) * 0.05
    total += int(input("Enter two pence coins: ")) * 0.02
    total += int(input("Enter one pence coins: ")) * 0.01
    return total

def is_transaction_successful(money_recieved, drink_cost):
    global profit
    if money_recieved >= drink_cost:
        change = round(money_recieved - drink_cost, 2)
        print(f"Youre change: {change}")
        profit += drink_cost
        return True
    else:
        required_coins = drink_cost - money_recieved
        print(f"Sorry you still need {required_coins}. Money refunded: {money_recieved}")
        return False

def make_coffee(drink_name, order_ingredients):
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕. Enjoy!")

is_on = True
while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino):").lower()

    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']} ml")
        print(f"Milk: {resources['milk']} ml")
        print(f"Coffee: {resources['coffee']}")
        print(f"Profit: {profit}")
    elif choice == "espresso" or choice == "latte" or choice == "cappuccino":
        drink = MENU[choice]
        if is_resource_enough(drink['ingredients']):
            payment = process_coins()
            if is_transaction_successful(payment, drink['cost']):
                make_coffee(choice, drink['ingredients'])
    else:
        print("Invalid option")

