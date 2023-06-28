############### Blackjack Project #####################

# Difficulty Normal 😎: Use all Hints below to complete the project.
# Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
# Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
# Difficulty Expert 🤯: Only use Hint 1 to complete the project. 😭😭😭

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

# Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
# Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

import random
from art import logo
from replit import clear

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def play():
    want_to_play = input("Do you want to play a game of Blackjack? Type 'y' or 'n': ").lower()
    if want_to_play == "y":
        clear()
        print(logo)
        user_cards = []
        for card in range(2):
            user_cards.append(random.choice(cards))

        def count(card_list):
            """
               Takes a list of cards and returns the total value of the cards.
               """
            if (sum(card_list) == 21) and (len(card_list) == 2):
                return 0
            if (11 in card_list) and (sum(card_list) > 21):
                card_list.remove(11)
                card_list.append(1)
            return sum(card_list)

        print(f"    Your cards: {user_cards}, current score: {count(user_cards)}")

        computer_cards = []
        for card in range(2):
            computer_cards.append(random.choice(cards))
        print(f"    Computer's first card: {computer_cards[0]}")

        def inGame():
            if (count(user_cards) != 21) or (count(computer_cards) != 21):
                if count(user_cards) > 21:
                    print(f"    Your final hand: {user_cards}, final score: {count(user_cards)}")
                    print(f"    Computer's final hand: {computer_cards}, final score: {count(computer_cards)}")
                    print("You went over. You lose 😭")
                    play()
                elif count(computer_cards) > 21:
                    print(f"    Your final hand: {user_cards}, final score: {count(user_cards)}")
                    print(f"    Computer's final hand: {computer_cards}, final score: {count(computer_cards)}")
                    print("Opponent went over. You win 😀")
                    play()
                else:
                    want_another_card = input("Type 'y' to get another card, type 'n' to pass: ").lower()
                    if want_another_card == 'y':
                        user_cards.append(random.choice(cards))
                        print(f"    Your cards: {user_cards}, current score: {count(user_cards)}")
                        print(f"    Computer's first card: {computer_cards[0]}")
                        if count(computer_cards) < count(user_cards):
                            computer_cards.append(random.choice(cards))
                        inGame()
                    elif want_another_card == 'n':
                        if count(computer_cards) < count(user_cards):
                            computer_cards.append(random.choice(cards))
                        if count(computer_cards) > 21:
                            print(f"    Your final hand: {user_cards}, final score: {count(user_cards)}")
                            print(f"    Computer's final hand: {computer_cards}, final score: {count(computer_cards)}")
                            print("Opponent went over. You win 😀")
                            play()
                        elif count(user_cards) > count(computer_cards):
                            print(f"    Your final hand: {user_cards}, final score: {count(user_cards)}")
                            print(f"    Computer's final hand: {computer_cards}, final score: {count(computer_cards)}")
                            print("You win 😀")
                            play()
                        elif count(user_cards) < count(computer_cards):
                            print(f"    Your final hand: {user_cards}, final score: {count(user_cards)}")
                            print(f"    Computer's final hand: {computer_cards}, final score: {count(computer_cards)}")
                            print("You lose 😤")
                            play()
                        else:
                            print(f"    Your final hand: {user_cards}, final score: {count(user_cards)}")
                            print(f"    Computer's final hand: {computer_cards}, final score: {count(computer_cards)}")
                            print("Draw 😅")
                            play()
                    else:
                        print("You have entered an invalid input")
            elif count(user_cards) == count(computer_cards):
                print(f"    Your cards: {user_cards}, current score: {count(user_cards)}")
                print(f"    Computer's first card: {computer_cards[0]}")
                print(f"    Your final hand: {user_cards}, final score: {count(user_cards)}")
                print(f"    Computer's final hand: {computer_cards}, final score: {count(computer_cards)}")
                print("Draw")
                play()
            elif count(user_cards) == 21:
                print(f"    Your cards: {user_cards}, current score: {count(user_cards)}")
                print(f"    Computer's first card: {computer_cards[0]}")
                print(f"    Your final hand: {user_cards}, final score: {count(user_cards)}")
                print(f"    Computer's final hand: {computer_cards}, final score: {count(computer_cards)}")
                print("Blackjack! You win 😀")
                play()
            elif count(computer_cards) == 21:
                print(f"    Your cards: {user_cards}, current score: {count(user_cards)}")
                print(f"    Computer's first card: {computer_cards[0]}")
                print(f"    Your final hand: {user_cards}, final score: {count(user_cards)}")
                print(f"    Computer's final hand: {computer_cards}, final score: {count(computer_cards)}")
                print("Lose, opponent has Blackjack 🤯")
                play()

        inGame()


play()
