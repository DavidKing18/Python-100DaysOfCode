''' EXERCISE 1 - HEADS OR TAILS '''

#Remember to use the random module
#Hint: Remember to import the random module here at the top of the file. 🎲
	 
#Write the rest of your code below this line 👇
import random

random_integer = random.randint(0, 1)
if random_integer == 0:
    print("Tails")
else:
    print("Heads")
print()


''' EXERCISE 2 - Banker Roulette'''

# Import the random module here
import random
# Split string method
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
random_index = random.randint(0, len(names)-1)
sponsor = names[random_index]
print(f"{sponsor} is going to buy the meal today!")


''' EXERCISE 3 - TREASURE MAP '''

# 🚨 Don't change the code below 👇
row1 = ["⬜️","️⬜️","️⬜️"]
row2 = ["⬜️","⬜️","️⬜️"]
row3 = ["⬜️️","⬜️️","⬜️️"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
horizontal = int(position[0]) - 1 # Accesses the first digit of the input which is the intended horizontal position only 1 greater because of indexing in python, hence the " - 1 ".
vertical = int(position[1]) - 1 # Accesses the second digit of the input which is the intended vertical position only 1 greater because of indexing in python, hence the " - 1 ".

map[vertical][horizontal] = "X" # Uses the map variable to modify or changed the value of the intended position. 

#Write your code above this row 👆

# 🚨 Don't change the code below 👇
print(f"{row1}\n{row2}\n{row3}")
print()