""" Debugging Odd or Even Checker """

number = int(input("Which number do you want to check?"))

if number % 2 == 0:  # before fix: if number % 2 = 0: >>> Single equator sign.
    print("This is an even number.")
else:
    print("This is an odd number.")
print()

""" Debugging Leap Year """

year = int(input(
    "Which year do you want to check?"))  # before fix: year = input("Which year do you want to check?") >>>  input was read as a string

if year % 4 == 0:
    if year % 100 == 0:
        if year % 400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")
print()

""" Debugging FizzBuzz """

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):  # Before fix: if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:  # Before fix: if number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:  # Before fix: if number % 5 == 0:
        print("Buzz")
    else:
        print(number)  # Before fix: print([number])
