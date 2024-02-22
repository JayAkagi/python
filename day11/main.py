import random
import art

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10]
    return random.choice(cards)

def clear():
    print("\n" * 50)

continue_play = True
while continue_play:
    print(art.logo)
    draw_user_cards = True

    #DEALER CARDS
    dealer_bust = False
    dealer_target = 21
    dealer_hand = []
    dealer_first_card = deal_card()
    dealer_hand.append(dealer_first_card)
    dealer_second_card = deal_card()
    dealer_hand.append(dealer_second_card)
    dealer_total = sum(dealer_hand)
    print(f"Dealer Hand: {dealer_hand[0]}, ?")



    # USER CARDS
    user_bust = False
    draw_cards = True
    user_hand = []
    user_first_card = deal_card()
    user_hand.append(user_first_card)
    user_second_card = deal_card()
    if user_second_card == 11:
        print(f"Your hand: {user_hand}")
        Ace = int(input("Do you want to use A as 1 or 11?"))
        user_second_card = Ace
    user_hand.append(user_second_card)
    user_total = sum(user_hand)

    print(f"Your hand: {user_hand}")
    print(f"Your total: {user_total}")

    if sum(user_hand) < 21:
        draw_cards = True
    elif sum(user_hand) == 21:
        draw_cards = False
    else:
        draw_cards = False
        Bust = True
        print("Bust")
        print(f"You have: {user_total}")

    #user draw cards
    while draw_cards:
        choice = int(input("Press 1 to hit or press 2 to stay."))
        clear()
        if choice == 1:
            user_draw_card = deal_card()
            if user_draw_card == 11 and user_total + 11 <= 21:
                print(f"Your hand: {user_hand}")
                print(f"Your total: {user_total}")
                while True:
                    Ace = int(input("Do you want to use A as 1 or 11?"))
                    if Ace in (1, 11):
                        user_draw_card = Ace
                        break
                    else:
                        print("Please enter either 1 or 11")
            user_hand.append(user_draw_card)
            user_total += user_draw_card
            print(f"Your hand: {user_hand}")
            print(f"Your total: {user_total}")

            if user_total > 21:
                draw_cards = False
                user_bust = True
                print("Bust")
            elif user_total == 21:
                draw_cards = False

        elif choice == 2:
            draw_cards = False
            print(f"Your Hand: {user_hand}")
            print(f"You have: {user_total}")

    # Dealer Draw cards after user finish turn
    if user_bust == False:
        while sum(dealer_hand) < 17:
            dealer_draw_card = deal_card()
            if dealer_draw_card == 11:
                if sum(dealer_hand) + 11 > dealer_target:
                    dealer_draw_card = 1
                else:
                    dealer_draw_card = 11
            dealer_hand.append(dealer_draw_card)
            dealer_total += dealer_draw_card
            if sum(dealer_hand) > dealer_target:
                dealer_bust = True

    print(f"\nDealer hand: {dealer_hand}")
    print(f"Dealer have: {sum(dealer_hand)}")

    if not user_bust:
        if user_total > dealer_total:
            print("You Win!")
        elif user_total == dealer_total:
            print("Draw")
        elif dealer_bust:
            print("Dealer Bust")
            print("You Win!")
        else:
            print("You lose.")
    else:
        print("You Lose")

    while True:
        continue_play = int(input("Type 1 to keep playing. Type 2 to exit."))
        if continue_play == 1:
            clear()
            break
        elif continue_play == 2:
            print(art.logo)
            print("Thanks for playing!")
            continue_play = False
            break
        else:
            print("Invalid input. Please enter '1'(play) or '2'(exit)")


