""" TREASURE ISLAND GAME """

print('''
  ,d                                                                       
  88                                                                       
MM88MMM 8b,dPPYba,  ,adPPYba, ,adPPYYba, ,adPPYba, 88       88 8b,dPPYba,  
  88    88P'   "Y8 a8P_____88 ""     `Y8 I8[    "" 88       88 88P'   "Y8  
  88    88         8PP""""""" ,adPPPPP88  `"Y8ba,  88       88 88          
  88,   88         "8b,   ,aa 88,    ,88 aa    ]8I "8a,   ,a88 88          
  "Y888 88          `"Ybbd8"' `"8bbdP"Y8 `"YbbdP"'  `"YbbdP'Y8 88          
                                                                         ''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

# https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.
# drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

# Write your code below this line 👇
path1 = input('You\'re at a cross road. Where do you want to go? Type"left" or "right".\n')
if path1.lower() == "left":  # Game Continues
    path2 = input(
        'You\'ve arrived at a lake. There is an island in the middle of the lake. Type "wait" to wait for a boat. '
        'Type "swim" to swim across.\n')
    if path2.lower() == "wait":  # Game Continues
        path3 = input(
            "You arrive at the island unharmed. There is a house with 3 doors. One red, one yellow and one blue. "
            "Which colour do you choose? \n")
        if path3.lower() == "yellow":  # Game Success
            print("You Win!!!")
            print()
            print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
            ''')
        elif path3.lower() == "red":  # Game Over
            print("Burned by fire. Game Over!!")
        elif path3.lower() == "blue":  # Game Over
            print("Eaten by beasts. Game Over!!")
        else:
            print("Game Over!!")
    else:  # Game Over
        print("You've been attacked by a trout. Game Over!!")
else:  # Game Over
    print("You have fallen into an endless pit. Game Over!!")
