""" LESSON 1 - THE PYTHON DICTINOARY: DEEP DIVE"""

programing_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

print(programing_dictionary["Function"])

# Adding new items to dictionary
programing_dictionary["Loop"] = "The action of doing something over and over again."

print(programing_dictionary)

# Create an empty dictionary.
empty_dictionary = {}

# wipe an existing dictionary
# programing_dictionary = {}
# print(programing_dictionary)

# Edit an item in a dictionary
programing_dictionary["Bug"] = "A moth in your computer."

# Loop through a dictionary
for key in programing_dictionary:
    print(key)
    print(programing_dictionary[key])
