# Step 5
from replit import clear
import random
import hangman_art
from hangman_words import list_of_words
print("wow")
clear()
# TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
words = list_of_words
stages = hangman_art.stages

# TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
hangman_logo = hangman_art.logo
print(hangman_logo)
print(
    "WELCOME TO MY HANGMAN GAME!! \n INSTRUCTION: You have 6 chances to guess a word. Length of the word is up to "
    "you. Goodluck!\n")
desired_word_length = int(input("How many letters do you want in the word? "))

word_list = []
for word in words:
    if len(word) == desired_word_length:
        word_list.append(word)
chosen_word = random.choice(word_list)
word_length = len(chosen_word)

end_of_game = False
lives = 6

# Testing code


# Create blanks
display = []
guessed = []
for _ in range(word_length):
    display += "_"

while not end_of_game:
    guess = input("Guess a letter: ").lower()

    clear()
    # TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print(f"You've already guessed {guess}")
    guessed.append(guess)
    # Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    # Check if user is wrong.
    if guess not in chosen_word:
        # TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the
        #  word.
        print(f"You guessed {guess}, that's not in the word. You lose a life.\nNumber of lives left: {lives - 1}")
        lives -= 1
        if lives == 0:
            end_of_game = True
            print(f"The word was '{chosen_word}'. You lose.")

    # Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    # Check if user has got all letters.
    if "_" not in display:
        end_of_game = True
        print("You win.")

    # TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stages[lives])
