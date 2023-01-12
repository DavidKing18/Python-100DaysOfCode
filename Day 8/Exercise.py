'''EXERCISE 1 - PAINT AREA CALCULATOR'''

# Write your code below this line 👇
import math

print("PAINT AREA CALCULATOR: ")


def paint_calc(height, width, cover):
    area_of_wall = height * width
    cans_of_paint = area_of_wall / cover
    cans_approx = math.ceil(cans_of_paint)
    print("You'll need {} cans of paint.".format(cans_approx))


# Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)
print()

'''EXERCISE 2 - PRIME NUMBERS'''

print("PRIME NUMBER CHECKER: ")


# Write your code below this line 👇
def prime_checker(number):
    if number <= 1:
        print("It's not a prime number.")
    elif number == 2:
        print("It's a prime number.")
    elif number > 2:
        for num in range(2, number):
            if number % num == 0:
                check = "It's not a prime number."
                break
            check = "It's a prime number."
        print(check)


# Write your code above this line 👆

# Do NOT change any of the code below👇
n = int(input("What number do you want to check? "))
prime_checker(number=n)
