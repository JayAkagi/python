while True:
    from random import randint

    rock = '''
        _______
    ---'   ____)
          (_____)
          (_____)
          (____)
    ---.__(___)
    '''

    paper = '''
        _______
    ---'   ____)____
              ______)
              _______)
             _______)
    ---.__________)
    '''

    scissors = '''
        _______
    ---'   ____)____
              ______)
           __________)
          (____)
    ---.__(___)
    '''
    options = [rock, paper, scissors]
    user_input = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors"))
    if user_input < 3:
        user_choice = options[user_input]
        print(user_choice)

        computer_input = randint(0, 2)
        computer_choice = options[computer_input]
        print("Computer chose:\n")
        print(computer_choice)

        if user_choice == rock and computer_choice == scissors:
            print("You win!")
        elif user_choice == paper and computer_choice == rock:
            print("You win!")
        elif user_choice == scissors and computer_choice == paper:
            print("You win!")
        elif user_choice == computer_choice:
            print("Tie")
        else:
            print("You lose.")
    else:
        print("Invalid options")



