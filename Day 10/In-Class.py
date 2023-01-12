''' LESSON1 - Functions with Outputs'''


def format_name(f_name, l_name):
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formated_string = format_name("DaVId", "adELEkE")
print(formated_string)
print()

''' LESSON 2 - Returning multiple outputs in a function.'''

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")


def format_name(f_name, l_name):
    if f_name == "" and l_name == "":
        return "You didn't enter a valid input."
    formated_f_name = f_name.title()
    formated_l_name = l_name.title()
    return f"{formated_f_name} {formated_l_name}"


formated_string = format_name(first_name, last_name)
print(formated_string)
