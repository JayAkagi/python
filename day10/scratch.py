import art
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

print(art.logo)
total = 0
num1 = int(input("First Number: "))
for func in operations:
    print(func)
operation_symbol = input ("Pick an operation from the line above: ")
num2 = int(input("Second Number: "))
calculation_function = operations[operation_symbol]
result = calculation_function(num1,num2)
total += result

print(f"{num1} {operation_symbol} {num2} = {result}")

continue_calculate_input = input(f"Type 'y' to continue calculating with {result}. Type 'n' to exit").lower()
calculate = continue_calculat(continue_calculate_input)

while calculate:
    operation_symbol = input("pick another operation: ")
    num3 = int(input("Third Number: "))
    calculation_function = operations[operation_symbol]
    result_continuation = calculation_function(result, num3)
    print(f"{result} {operation_symbol} {num3} = {result_continuation}")
    result = result_continuation

    continue_calculate_input = input(f"Type 'y' to continue calculating with {result_continuation}. Type 'n' to exit").lower()
    calculate = continue_calculat(continue_calculate_input)




