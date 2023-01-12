''' PROJECT - SECRET AUCTION PROGRAM'''
from replit import clear
from art import logo

print(logo)
print("Welcome to the secret auction program. 👀 ")

bid_record = {}


def add_bid(name, bid):
    bid_record[name] = bid


def highest_bid(dict):
    highest_bid = 0
    for bidder in dict:
        bid_amount = dict[bidder]
        if bid_amount > highest_bid:
            highest_bid = dict[bidder]
            highest_bidder = bidder
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.\n")


more_bids = True
while more_bids:
    name_of_bidder = input("What is your name?: ")
    bid_price = int(input("What's your bid?: $"))
    add_bid(name=name_of_bidder, bid=bid_price)
    more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n").lower()
    if more_bidders == 'yes':
        more_bids = True
        clear()
    elif more_bidders == 'no':
        clear()
        highest_bid(bid_record)
        more_bids = False
    else:
        print("You have entered an invalid input.")
        more_bids = False
