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

# TODO Prompt user by asking “What would you like?
coffee_machine_on = True
recent_transaction = []
money = 0

pound_coin = 1
fifty_pence = 0.50
twenty_pence = 0.20
ten_pence = 0.10
five_pence = 0.05
two_pence = 0.02
one_pence = 0.01

while coffee_machine_on:
    user_input = input("What would you like? (espresso/latte/cappuccino)").lower()
    if user_input == "espresso" or user_input == "latte" or user_input == "cappuccino":
        selected_drink = MENU[user_input]

        user_pound = int(input("Enter pound coins: "))
        total_user_pound = pound_coin * user_pound
        user_fifty_pence = float(input("Enter fifty pence coins: "))
        total_user_fifty_pence = fifty_pence * user_fifty_pence
        user_twenty_pence = float(input("Enter twenty pence coins: "))
        total_user_twenty_pence = twenty_pence * user_twenty_pence
        user_ten_pence = float(input("Enter ten pence coins: "))
        total_user_ten_pence = ten_pence * user_ten_pence
        user_five_pence = float(input("Enter five pence coins: "))
        total_user_five_pence = five_pence * user_five_pence
        user_two_pence = float(input("Enter two pence coins: "))
        total_user_two_pence = two_pence * user_two_pence
        user_one_pence = float(input("Enter one pence coins: "))
        total_user_one_pence = one_pence * user_one_pence

        total_user_money = total_user_pound + total_user_fifty_pence + \
                           total_user_twenty_pence + total_user_ten_pence + \
                           total_user_five_pence + total_user_two_pence + \
                           total_user_one_pence

        total_user_money = round(total_user_money, 2)

        print(f"You paid: £{total_user_money}")

        if 'water' in selected_drink['ingredients'] and resources['water'] < selected_drink['ingredients']['water']:
            required_water = selected_drink['ingredients']['water'] - resources['water']
            print(f"Not enough water. Coffee machine needs {required_water} of water to make {user_input}")
            print(f"Money refunded: £{total_user_money}")
        elif 'milk' in selected_drink['ingredients'] and resources['milk'] < selected_drink['ingredients']['milk']:
            required_milk = selected_drink['ingredients']['milk'] - resources['milk']
            print(f"Not enough milk. Coffee machine needs {required_milk} of milk to make {user_input}")
            print(f"Money refunded: £{total_user_money}")
        elif 'coffee' in selected_drink['ingredients'] and resources['coffee'] < selected_drink['ingredients'][
            'coffee']:
            required_coffee = selected_drink['ingredients']['coffee'] - resources['coffee']
            print(f"Not enough coffee. Coffee machine needs {required_coffee} of coffee to make {user_input}")
            print(f"Money refunded: £{total_user_money}")
        elif total_user_money < selected_drink['cost']:
            required_money = selected_drink['cost'] - total_user_money
            print(f"Not enough money. You need £{required_money} more for {user_input}. Money refunded: £{total_user_money}")
            print(f"Money refunded: £{total_user_money}")
        else:
            if 'water' in selected_drink['ingredients']:
                resources['water'] -= selected_drink['ingredients']['water']
            if 'milk' in selected_drink['ingredients']:
                resources['milk'] -= selected_drink['ingredients']['milk']
            if 'coffee' in selected_drink['ingredients']:
                resources['coffee'] -= selected_drink['ingredients']['coffee']

            change = 0
            if total_user_money > selected_drink['cost']:
                change = round(total_user_money - selected_drink['cost'], 2)

            if change > 0:
                print(f"Your change: £{change}")

            recent_transaction.append({user_input: selected_drink['cost']})
            money += selected_drink['cost']
            print(f"Here is your {str.capitalize(user_input)}. Enjoy!")

    elif user_input == "report":
        print(f"Water: {resources['water']} ml\n"
              f"Milk: {resources['milk']} ml\n"
              f"Coffee: {resources['coffee']} g\n"
              f"Money: £{money}\n")
        print("Recent Transactions")
        for transaction in recent_transaction:
            for drink, cost in transaction.items():
                print(f"{drink} - £{cost}")
    elif user_input == "off":
        print("Coffee machine turned off.")
        coffee_machine_on = False
