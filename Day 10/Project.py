from replit import clear
from art import logo
# Calculator


def add(n1, n2):
	return n1 + n2

def subtract(n1, n2):
	return n1 - n2

def multiply(n1, n2):
	return n1 * n2

def divide(n1, n2):
	return n1 / n2

operations = {
	"+": add,
	"-": subtract,
	"*": multiply,
	"/": divide
}
def calculator():
	print(logo)
	num1 = float(input("What's the first number?: "))
	for symbol in operations:
		print(symbol)
	operation_symbol = input("Pick an operation from the line above: ")
	num2 = float(input("What's the second number?: "))
	calculation_function = operations[operation_symbol]
	answer = calculation_function(num1, num2)		
	print(f"{num1} {operation_symbol} {num2} = {answer}")
	
	should_continue = True
	while should_continue:
		should_proceed = input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation.: ").lower()
		if should_proceed == 'y':
			should_continue = True
			operation_symbol = input("Pick another operation: ")
			num3 = float(input("What's the next number?: "))
			calculation_function = operations[operation_symbol]
			next_answer = calculation_function(answer, num3)
			print(f"{answer} {operation_symbol} {num3} = {next_answer}")
			answer = next_answer
		else:
			should_continue = False
			clear()
			calculator()

calculator()