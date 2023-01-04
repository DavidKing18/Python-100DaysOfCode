# Excercise 1
print("Day 1 - Python Print Function")
print("The function is declared like this:")
print("print('what to print')")
print()


# Excercise 2

#1. Missing double quotes before the word Day.
print("Day 1 - String Manipulation")

#2. Outer double quotes changed to single quotes.
print('String Concatenation is done with the "+" sign.')

#3. Extra indentation removed
print('e.g. print("Hello " + "world")')

#4. Extra ( in print function removed.
print("New lines can be created with a backslash and n.")

# OR----

# print("Day 1 - String Manipulation" + "\n" + "String Concatenation is done with the " + '"+"' + " sign." + "\n" + 'e.g. print("Hello " + "world")' + "\n" + "New lines can be created with a backslash and n.")
print()


# Exercise 3
#This code prints the number of characters in a user's name.
print( len( input("What is your name? ") ) )
print()
#Notes
#If input was "Jack"
#1st: print(len("Jack"))
#2nd: print(4)


# Exercise 4
# 🚨 Don't change the code below 👇
a = input("a: ")
b = input("b: ")
# 🚨 Don't change the code above 👆
####################################
#Write your code below this line 👇
c = b
b = a
a = c
#Write your code above this line 👆
####################################
# 🚨 Don't change the code below 👇
print("a: " + a)
print("b: " + b)


