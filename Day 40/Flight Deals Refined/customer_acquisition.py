import requests

FLIGHT_CLUB_ENDPOINT = "https://api.sheety.co/0ddc17c284692df155ab4b36a99c5004/flightDeals/users"

welcome_message = "Welcome to Dayo's Flight Club.\nWe find the best flight deals and email you."
print(welcome_message)
first_name = input("What is your first name?\n")
last_name = input("What is your last name?\n")

mail_matches = False
while not mail_matches:
    user_email = input("What is your email?\n")
    retyped_user_email = input("Type your email again.\n")
    if user_email == retyped_user_email:
        user_data = {
            'user': {
                'firstName': first_name,
                'lastName': last_name,
                'email': user_email
            }
        }
        response = requests.post(url=FLIGHT_CLUB_ENDPOINT, json=user_data).json()
        print(response)
        print("Success! Your email has been added, look forward to sending you the best deals.")
        mail_matches = True
    else:
        print("Emails don't match 🥴")
