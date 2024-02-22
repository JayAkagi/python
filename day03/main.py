print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
user_input = str("")
valid_choice = False


choice1 = input("Would you like to go left or right?: ")
user_input = choice1.lower()

if user_input == "right":
    print("Game over, you fell into a hole.")
    valid_choice = False
elif user_input == "left":
    choice2 = input("You end up in a lake. Do you want to swim or wait for a boat to come?")
    user_input = choice2.lower()
    valid_choice = True
else:
    print("Invalid option.")
    valid_choice = False

if valid_choice:
    if user_input == "swim":
        print("Game over, you were attacked by a trout.")
        valid_choice = False
    elif user_input == "wait":
        choice3 = input("After crossing the lake, you found 3 doors. Which one will you open? Red, Blue or Yellow?")
        user_input = choice3.lower()
        valid_choice = True
    else:
        print("Invalid option.")
        valid_choice = False

if valid_choice:
    if user_input == "red":
        print("Game over, you got burned by scorching flames after you opened the door.")
    elif user_input == "blue":
        print("Game over, a horde of beasts started running at you and mawed you alive after you opened the door.")
    elif user_input == "yellow":
        print("You found the treasure! You win!")
    else:
        print("Invalid option")
