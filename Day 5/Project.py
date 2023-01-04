'''PASSWORD GENERATOR PROJECT '''

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

password = []
count4letters = 0
for letter in letters:
    if count4letters < nr_letters:
        password.append(random.choice(letters))
    count4letters += 1

count4numbers = 0
for number in numbers:
    if count4numbers < nr_numbers:
        password.append(random.choice(numbers))
    count4numbers += 1

count4symbols = 0
for symbol in symbols:
    if count4symbols < nr_symbols:
        password.append(random.choice(symbols))
    count4symbols += 1

random.shuffle(password)
password_in_string = "".join(password)
print(f"Here is your password: {password_in_string}")


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P