'''LESSON 1 - FUNTIONS WITH INPUTS'''

def greet():
	print("Good Morning!!!")
	print("Good Afternoon!!")
	print("Good Night!")

greet()
print()

def greet(name):
	print(f"Good Morning, {name}")
	print("How are you today?")

greet("David")
print()


'''LESSON 2 - POSITIONAL VS. KEYWORD ARGUMENTS'''

def greet_with(name, location):
	print(f"Hello, {name}!")
	print(f"How's the weather in {location}?")

greet_with(location = "Venezuela", name = "Brian")
