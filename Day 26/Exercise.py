################################################
#               SQUARING NUMBERS
################################################

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above 👆

# Write your 1 line code 👇 below:

squared_numbers = [num * num for num in numbers]

# Write your code 👆 above:

print(squared_numbers)

################################################
#           FILTERING EVEN NUMBERS
################################################

numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
# 🚨 Do Not Change the code above

# Write your 1 line code 👇 below:

result = [number for number in numbers if number % 2 == 0]

# Write your code 👆 above:

print(result)

################################################
#               DATA OVERLAP
################################################

with open("file1.txt") as file1:
    list1 = file1.readlines()

with open("file2.txt") as file2:
    list2 = file2.readlines()

result = [int(number) for number in list1 if number in list2]

# Write your code above 👆

print(result)

################################################
#           DICTIONARY COMPREHENSION 1
################################################

sentence = "What is the Airspeed Velocity of an Unladen Swallow?"
# Don't change code above 👆

# Write your code below:

words_in_sentence = sentence.split()
result = {word: len(word) for word in words_in_sentence}

print(result)

################################################
#           DICTIONARY COMPREHENSION 2
################################################

weather_c = {
    "Monday": 12,
    "Tuesday": 14,
    "Wednesday": 15,
    "Thursday": 14,
    "Friday": 21,
    "Saturday": 22,
    "Sunday": 24,
}
# 🚨 Don't change code above 👆

# Write your code 👇 below:

weather_f = {day: (temp_c * 9 / 5) + 32 for day, temp_c in weather_c.items()}

print(weather_f)
