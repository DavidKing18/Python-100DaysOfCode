""" DEBUGGING  """
from random import randint


# Describe Problem
def my_function():
    for i in range(1, 21):  # before fix: for i in range(1, 20): >> stop number (20) is omitted in range function
        if i == 20:
            print("You got it")


my_function()
print()

# Reproduce the Bug

dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
dice_num = randint(0, 5)  # before fix: dice_num = randint(1, 6) >> 6 is beyond range of list.
print(dice_imgs[dice_num])
print()

# Play Computer
year = int(input("What's your year of birth? "))
if 1980 < year < 1994:
    print("You are a millennial.")
elif year >= 1994:  # before fix: elif year > 1994: >>> no code/bucket catches when the year is 1994
    print("You are a Gen Z.")
print()

# Fix the Errors
age = int(input(
    "How old are you?"))  # before fix: age = input("How old are you?") >>> input needs to be converted to integer
# value because of later comparison.
if age > 18:
    print(
        f"You can drive at age {age}.")  # before fix: line was not properly indented and was missing the f-string
    # declaration ('f').
print()

# Print is Your Friend
pages = int(input("Number of pages: "))
word_per_page = int(input(
    "Number of words per page: "))  # before fix: word_per_page == int(input("Number of words per page: ")) >>>
# assigment error: used two equator signs (comparison) instead of one.
total_words = pages * word_per_page
print(total_words)
print()


# Use a Debugger
def mutate(a_list):
    b_list = []
    for item in a_list:
        new_item = item * 2
        b_list.append(new_item)  # before fix: was indented outside for loop
    print(b_list)


mutate([1, 2, 3, 5, 8, 13])
print()
