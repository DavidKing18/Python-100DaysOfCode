from random import randint
from art import logo
from replit import clear


def run_game():
    print(logo)
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    level_choice = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
    attempts = 0
    if level_choice == 'easy':
        attempts += 10
    elif level_choice == 'hard':
        attempts += 5
    else:
        print("You have entered an invalid input.")

    computer_choice = randint(1, 101)
    game_end = False
    while not game_end:
        if attempts > 0:
            print(f"You have {attempts} attempt(s) remaining to guess the number.")
            user_guess = int(input("Make a guess: "))
            if user_guess == computer_choice:
                print(f"You got it! The answer was {computer_choice}")
                game_end = True
            elif user_guess > computer_choice:
                print("Too high.")
                if attempts > 1:
                    print("Guess again.")
                attempts -= 1
            elif user_guess < computer_choice:
                print("Too low.")
                if attempts > 1:
                    print("Guess again.")
                attempts -= 1
        if attempts == 0:
            game_end = True
            print(f"You've run out of guesses, answer was {computer_choice}, you lose.")

        if (game_end is True) or (attempts == 0):
            replay = input("Do you want to play again? Type 'yes' or 'no': ").lower()
            if replay == 'yes':
                clear()
                run_game()
            game_end = True


run_game()
