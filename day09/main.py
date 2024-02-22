import os
import art

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def find_highest_bidder(bidding_record):
    highest_bid = 0
    for bidder in bidding_record:
        bid_ammount = bidding_record[bidder]
        if bid_ammount > highest_bid:
            highest_bid = bid_ammount
            winner = bidder
    print(f"The winner is {winner} with a bid of £{highest_bid}")

print(art.logo)

auction = True
bids = {}
while auction:
    name = input("Enter bidder's name: ")
    bid_price = int(input("Enter bid price: "))
    bids[name] = bid_price

    valid_response = False
    while not valid_response:
        close_auction = input("is there anyone else wants to add bid? : ").lower()
        if close_auction == "no":
            auction = False
            valid_response = True
            find_highest_bidder(bids)
        elif close_auction == "yes":
            valid_response = True
            clear()
        else:
            print("Invalid Option. Try again.")
            valid_response = False

# print(bids)

