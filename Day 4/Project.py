import random

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
''' ROCK-PAPER-SCISSORS GAME'''
# Write your code below this line 👇

print("Welcome to My Rock, Paper, Scissors Game!!!")
user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
if (user_choice == "0") or (user_choice == "1") or (user_choice == "2"):
    print("You chose: ")
if user_choice == "0":
    print(rock)
elif user_choice == "1":
    print(paper)
elif user_choice == "2":
    print(scissors)
else:
    print("You have entered and invalid input")

if (user_choice == "0") or (user_choice == "1") or (user_choice == "2"):
    print("Computer chose: ")
    computer_choice = random.randint(0, 2)
    if computer_choice == 0:
        print(rock)
    elif computer_choice == 1:
        print(paper)
    elif computer_choice == 2:
        print(scissors)

    if user_choice == str(computer_choice):
        print("Draw!")
    elif ((user_choice == "0") and (computer_choice == 1)) or ((user_choice == "1") and (computer_choice == 2)) or (
            (user_choice == "2") and (computer_choice == 0)):
        print("You Loose!")
    elif ((user_choice == "0") and (computer_choice == 2)) or ((user_choice == "1") and (computer_choice == 0)) or (
            (user_choice == "2") and (computer_choice == 1)):
        print("You Win!")
    print()
