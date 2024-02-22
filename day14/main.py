import art
import game_data
import random


def clear():
    print("\n" * 50)


def initialise_data():
    random.shuffle(game_data.data)
    for i in range(2):
        data_to_compare.append(game_data.data[i])


def follower_difference_count(icon_a, icon_b):
    compare = [icon_a["follower_count"], icon_b["follower_count"]]

    for i in range(len(compare)):
        for j in range(len(compare) - i -1):
            if compare[j] > compare[j+1]:
                temp = compare[j]
                compare[j] = compare[j+1]
                compare[j+1] = temp
    difference = compare[1] - compare[0]
    return difference


def next_round():
    global data_to_compare

    if data_to_compare[0] == game_data.data[0] or data_to_compare[1] == game_data.data[0]:
        random.shuffle(game_data.data)

    data_to_compare.pop(0)
    data_to_compare.append(game_data.data[0])

    clear()
    if user_is_correct != "":
        print(
            f"{user_is_correct} {correct_answer} has more followers than {incorrect_answer} with {follower_difference} followers.\n")



def prompt():
    print(art.logo)

    print(f"Round: {total_rounds}")
    print(f"Current score: {user_score}")
    if data_a_description.startswith(vowels):
        print(f"Compare A: {data_a_name}, an {data_a_description}, from {data_a_country}")
    else:
        print(f"Compare A: {data_a_name}, a {data_a_description}, from {data_a_country}")

    print(art.vs)

    if data_b_description.startswith(vowels):
        print(f"Against B: {data_b_name}, an {data_b_description}, from {data_b_country}")
    else:
        print(f"Against B: {data_b_name}, a {data_b_description}, from {data_b_country}")

def game_over():
    clear()
    print(art.logo)
    print(f"\nThanks for playing!\n"
          f"Your total score is: {user_score}\n"
          f"Rounds played: {total_rounds - 1}")


play = True
data_to_compare = []
initialise_data()

user_score = 0
total_rounds = 1
user_is_correct = ""
correct_answer = ""
incorrect_answer = ""


while play:
    follower_difference = follower_difference_count(data_to_compare[0], data_to_compare[1])
    vowels = ('a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U')

    data_a = data_to_compare[0]
    data_a_name = data_to_compare[0]["name"]
    data_a_follower = data_to_compare[0]["follower_count"]
    data_a_description = data_to_compare[0]["description"]
    data_a_country = data_to_compare[0]["country"]

    data_b = data_to_compare[1]
    data_b_name = data_to_compare[1]["name"]
    data_b_follower = data_to_compare[1]["follower_count"]
    data_b_description = data_to_compare[1]["description"]
    data_b_country = data_to_compare[1]["country"]

    valid_answer = False
    while not valid_answer:
        prompt()
        user_answer = input("Who has more Followers? Type 'A' or 'B' or type '1' to exit: ").lower()
        if user_answer == "a":
            if data_a_follower > data_b_follower:
                user_is_correct = "You are right!"
                correct_answer = data_a_name
                incorrect_answer = data_b_name
                user_score += 1
                valid_answer = True
            else:
                user_is_correct = "Incorrect answer."
                correct_answer = data_b_name
                incorrect_answer = data_a_name
                valid_answer = True
        elif user_answer == "b":
            if data_b_follower > data_a_follower:
                user_is_correct = "You are right!"
                correct_answer = data_b_name
                incorrect_answer = data_a_name
                user_score += 1
                valid_answer = True
            else:
                user_is_correct = "Incorrect answer"
                correct_answer = data_a_name
                incorrect_answer = data_b_name
                valid_answer = True
        elif user_answer == "1":
            play = False
            game_over()
            break
        else:
            print("Invalid input. Type 'A' or 'B' to select answer or type '1' to exit.")

    if not play:
        break

    total_rounds += 1
    next_round()

