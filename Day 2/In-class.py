'''Lesson 1'''
# Integer

print(123 + 345)

print(123_456_789 * 1)

# Float

print(3.14159)

# Boolean
True
False


'''Lesson 2'''

# num_char = len(input("What is your name?"))
# new_num_char = str(num_char)
# print("Your name has " + new_num_char + " characters.")
# print(type(num_char))

a = str(123)
print(type(a))
a = float(123)
print(type(a))

print(70 + float("100.5"))
print(str(70) + str(100))


'''Lesson 3'''

3 + 5 # Addition 
7 - 4 # Subtraction
3 * 2 # Multiplication 
6 / 3 # Division - Results in a float
2 ** 3 #Exponential

# Order of Operation - PEMDAS
# Parenthesis - ()
# Exponential - **
# Multiplication - *
# Division - (/)
# Addition - (+)
# Subtraction - (-)

print(3 * 3 + 3 / 3 - 3) # 7.0
print(3 * (3 + 3) / 3 - 3) # 3.0


'''Lesson 4'''
print(round(8/3, 2))
print(8//3)


result = 4 / 2
result /=2
result *= 3
print(result)

score = 0

# User scores a point
score += 1
print(score)
# user looses two points
score -= 2
print(score)


# String Formatting
score = 0
height = 1.8
isWinning = True
#f-String
print(f"Your score is {score}, your height is {height}, you are winning? {isWinning}")
