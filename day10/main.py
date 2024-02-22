import art
import os

def clear():
    print("\n" * 100)

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1,n2):
    return n1 / n2

def continue_calculat(input):
    if input == "y":
        return True
    elif input == "n":
        return False
    else:
        print("invalid input")

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    print(art.logo)
    num1 = float(input("Enter first number:"))
    for symbol in operations:
        print(symbol)
    proceed = True

    while proceed:
        operation_symbol = input("pick operation")
        num2 = float(input("Enter next number: "))
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")

        calc = input(f"Type 'y' to continue calculting with {answer}. Type 'n' to start new calculation")
        if calc == "y":
            num1 = answer
        elif calc == "n":
            proceed == False
            clear()
            calculator()

calculator()