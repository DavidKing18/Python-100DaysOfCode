# ################################################
# # How to Create Lists using List Comprehension
# ################################################
#
# numbers = [1, 2, 3]
# new_numbers = [number + 1 for number in numbers]
# print(new_numbers)
#
# name = "Angela"
# letters = [letter for letter in name]
# print(letters)
#
# numbers = [number * 2 for number in range(1, 5)]
# print(numbers)

# Conditional List Comprehension

# names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]
# short_names = [name for name in names if len(name) < 5]
# print(short_names)
#
# new_names = [name.upper() for name in names if len(name) > 5]
# print(new_names)
#
# ################################################
# #       HOW TO USE DICTIONARY COMPREHENSION
# ################################################

names = ["Alex", "Beth", "Caroline", "Dave", "Eleanor", "Freddie"]

# import random
#
# students_score = {student: random.randint(1, 100) for student in names}
# print(students_score)
#
# passed_students = {student: score for (student, score) in students_score.items() if score > 59}
# print(passed_students)

################################################
#    HOW TO ITERATE OVER A PANDAS DATAFRAME
################################################

import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# #  Looping through dictionaries:
# for (key, value) in student_dict.items():
#     print(key, value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)
print()

# Loop through a data frame
for (key, value) in student_data_frame.items():
    print(key)
    print(value)
print()

#  Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    print(row)
    print(row.student)
    if row.student == "Angela":
        print(row)
