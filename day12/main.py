import random
import art

def difficulty_choice(choice):
    if choice == "easy":
        return 10
    elif choice == "hard":
        return 5
    else:
        return "Invalid difficulty choice. Type easy or hard.\n"

def game():
    continue_play = True
    number_to_guess = random.randint(1, 100)
    print(art.logo)
    attempts = 0
    total_attempts = 0

    while True:
        select_difficulty = input("Select difficulty: easy or hard?")
        validate_difficulty = difficulty_choice(select_difficulty)

        if isinstance(validate_difficulty, int):
            attempts += validate_difficulty
            break
        else:
            print(validate_difficulty)

    print(f"Game mode: {select_difficulty}\n\n"
          f"I'm thinking of a number from 1-100\n")

    while continue_play and attempts > 0:
        print(f"Attempts: {attempts}")
        guess = int(input("make a guess: "))
        if guess > number_to_guess:
            if guess - number_to_guess < 10 or guess - number_to_guess == 10:
                print("That's a little bit high\n")
            else:
                print("Too high\n")
        elif guess < number_to_guess:
            if number_to_guess - guess < 10 or number_to_guess - guess == 10:
                print("That's a little bit low\n")
            else:
                print("Too low\n")
        else:
            print(f"You guessed it right! The number im thinking of is: {number_to_guess}")
            print(f"Total attempts: {total_attempts}\n"
                  f"Attempts left: {attempts}")
            continue_play = False
            break

        attempts -= 1
        total_attempts += 1

        if attempts == 0:
            print("You run out of attempts. Game over")
            continue_play = False

    while continue_play != True:
        play_again = input("Continue? Yes:No").lower()
        if play_again == "no":
            print("Thanks for playing!")
            break
        elif play_again == "yes":
            game()
        else:
            print("Invalid input. Type Yes or No")



game()





