'''Exercise 1 - Data Types'''

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

#Check the data type of two_digit_number
# print(type(two_digit_number))

#Get the first and second digits using subscripting then convert string to int.
first_digit = int(two_digit_number[0])
second_digit = int(two_digit_number[1])

#Add the two digits together
sum_of_digits = first_digit + second_digit

print(sum_of_digits)



'''Exercise 2 - BMI Calculator'''
# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
height_as_float = float(height)
weight_as_float = float(weight)
result = weight_as_float/(height_as_float**2)
print(int(result))



'''Exercise 3 - Life in Weeks'''

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

yearsLeft = 90 - int(age)
monthsLeft = yearsLeft * 12
weeksLeft = yearsLeft * 52
daysLeft = yearsLeft * 365

message = f"You have {daysLeft} days, {weeksLeft} weeks, and {monthsLeft} months left."
print(message)