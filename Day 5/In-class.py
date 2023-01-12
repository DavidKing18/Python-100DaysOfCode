'''LESSON 1 - USING THE FOR LOOP WITH PYTHON '''
print("LESSON 1: ")
fruits = ["Apple", "Peach", "Pear"]
for fruit in fruits:
    print(fruit)
    print(fruit + " Pie")
print(fruits)
print()

'''LESSON 2 - FOR LOOPS AND RANGE FUNCTION.'''
print("Testing Range Function ------- ")
for number in range(1, 11):
    print(number)
for number in range(1, 11, 3):
    print(number)

total = 0
for number in range(1, 101):
    total += number
print(total)
