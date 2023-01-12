''' EXERCISE 1 - AVERAGE HEIGHT '''
print("AVERAGE HEIGHT CALCULATOR!! ")
# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights: ").split()
for n in range(0, len(student_heights)):
    student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


# Write your code below this row 👇
total_height = 0
number_of_students = 0
for height in student_heights:
    total_height += height
    number_of_students += 1
avereage_height = total_height / number_of_students
avereage_height_approx = round(avereage_height)
print(f"Average heigt is: {avereage_height_approx}")
print()

'''EXERCISE 2 - HIGH SCORE'''
print("Highest Score Calculator-----")
# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
    student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

# Write your code below this row 👇

highest_score = 0
for score in student_scores:
    if score > highest_score:
        highest_score = score

print(f"The highest score in the class is: {highest_score}")

# # Another way to do it:
# highest_score = max(student_scores)
# print(f"The highest score in the class is: {highest_score}")
print()

'''EXERCISE 3 - ADDING EVEN NUMBERS'''
print("Sum of even numbers from 1 to 100: ")
# Write your code below this row 👇
total = 0
for even_number in range(0, 101, 2):
    total += even_number
print(total)

## Another way to do it:
# total = 0
# for number in range(1, 101):
#     if number % 2 == 0:
#         total += number
# print(total)
print()

'''EXERCISE 4 - FIZZBUZZ'''
print("FizzBuzz Game!! ")
# Write your code below this row 👇

for number in range(1, 101):
    if (number % 3 == 0) and (number % 5 == 0):  # Divisible by 3 and 5
        print("FizzBuzz")
    elif number % 3 == 0:  # Divisible by 3
        print("Fizz")
    elif number % 5 == 0:  # Divisible by 5
        print("Buzz")
    else:  # Not divisible by 3 nor 5
        print(number)
