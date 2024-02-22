import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
           'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?: "))
nr_symbols = int(input("How many symbols would you like?: "))
nr_numbers = int(input("How many numbers would you like?: "))

# ----------------------- Easy Version ------------------
print("\nEasy Version: ")
password = ""
for letter in range(1, nr_letters + 1):
    password += letters[random.randint(0, len(letters) - 1)]
for symbol in range(1, nr_symbols + 1):
    password += symbols[random.randint(0, len(symbols) - 1)]
for number in range(1, nr_numbers + 1):
    password += numbers[random.randint(0, len(numbers) - 1)]

print(password)

# ----------------------- Hard Version -------------------
print("\nHard Version: ")
password_char = []

for letter in range(1, nr_letters + 1):
    char = random.choice(letters)
    password_char.append(char)
for symbol in range(1, nr_symbols + 1):
    char = random.choice(symbols)
    password_char.append(char)
for number in range(1, nr_numbers + 1):
    char = random.choice(numbers)
    password_char.append(char)

random.shuffle(password_char)
generated_password = ''.join(password_char)
print(generated_password)
