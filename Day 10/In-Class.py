""" LESSON1 - Functions with Outputs"""


def format_name(f_name, l_name):
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name("DaVId", "adELEkE")
print(formatted_string)
print()

''' LESSON 2 - Returning multiple outputs in a function.'''

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")


def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You didn't enter a valid input."
    formatted_f_name = f_name.title()
    formatted_l_name = l_name.title()
    return f"{formatted_f_name} {formatted_l_name}"


formatted_string = format_name(first_name, last_name)
print(formatted_string)
