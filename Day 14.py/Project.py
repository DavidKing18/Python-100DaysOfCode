from random import choice
from art import logo, vs
from game_data import data 
from replit import clear

first_identity = choice(data)
score = 0
print(logo)
print("Welcome to my #who'sGotMoreFollowers? game!\nLet's go!!")

should_continue = True
while should_continue:
    data.remove(first_identity)
    second_identity = choice(data)
    data.append(first_identity)
    second_identity = choice(data)

    name1 = first_identity['name'] 
    followers1 = first_identity['follower_count']
    description1 = first_identity['description']
    country1 = first_identity['country']
        # Repeated format - Could use a function here
    name2 = second_identity['name']
    followers2 = second_identity['follower_count']
    description2 = second_identity['description']
    country2 = second_identity['country']

    print(f"Compare A: {name1}, a {description1}, from {country1}.")
    print(vs)
    print(f"Against B: {name2}, a {description2}, from {country2}.")
    response = input("Who has more followers on IG? Type 'A' or 'B': ").lower()
	
    def check(user_response):
        if user_response == 'a':
            return (followers1 > followers2)
        elif user_response  == 'b':
            return (followers2 > followers1)    

    if check(response) == True:
        score += 1
        first_identity = second_identity
        clear()
        print(logo)
        print(f"You're right! Current score: {score}")

    elif check(response) == False:
        should_continue = False
        clear()
        print(logo)
        print(f"Sorry, that's wrong. Final score: {score}")