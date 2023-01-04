'''EXERCISE 1 - Even or Odd Checker'''
print("Even Or Odd Checker!!")
# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if number % 2 == 0:
    print("This is an even number.")
else:
    print("This is an odd number.")
print()



'''EXERCISE 2 - BMI 2.0'''

print("BMI Checker!!")
# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight/(height**2)
bmiApprox = round(bmi)

if bmi < 18.5:
    print(f"Your BMI is {bmiApprox}, you are underwight.")
elif bmi < 25:
    print(f"Your BMI is {bmiApprox}, you have a normal weight.")
elif bmi < 30:
    print(f"Your BMI is {bmiApprox}, you are slightly overweight.")
elif bmi < 35:
    print(f"Your BMI is {bmiApprox}, you are obese.")
else: 
    print(f"Your BMI is {bmiApprox}, you are clinically obese.")
print()



'''EXERCISE 3 - LEAP YEAR'''

# 🚨 Don't change the code below 👇
print("Leap Year Checker!!")
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

if year % 4 == 0:
    if year % 100 != 0:
        print("Leap year.")
    elif year % 400 ==0:
        print("Leap Year.")
    else:
        print("Not leap year.")
else:
    print("Not leap year.")
print()


'''Exercise 4 - PIZZA ORDER PRACTICE'''
print("PIZZA ORDER PRACTICE!")
# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
add_pepperoni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bill = 0
if size == "S": 
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25

if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    bill += 3
    
if extra_cheese == "Y":
    bill += 1
print(f"Your final bill is: ${bill}.")




'''Exercise 5 - Love Calculator'''

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


combined_names = name1 + name2
T_occurence = combined_names.count("t")
R_occuerence =combined_names.count("r")
U_occuerence =combined_names.count("u")
E_occuerence =combined_names.count("e")

L_occuerence =combined_names.count("l")
O_occuerence =combined_names.count("o")
V_occuerence =combined_names.count("v")
E_occuerence =combined_names.count("e")

score1 = T_occurence + R_occuerence + U_occuerence + E_occuerence

score2 = L_occuerence + O_occuerence + V_occuerence + E_occuerence

love_score = int(str(score1) + str(score2))

if love_score < 10 or love_score > 90:
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif love_score >= 40 and love_score <= 50:
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")


