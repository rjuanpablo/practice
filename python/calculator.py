# Functions
def adittion(a, b):
	return a + b

def subtraction(a, b):
	return a - b

def multiplication(a, b):
	return a * b

def division(a, b):
	return a / b

# Show menú
print("Select an option:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

# Select option
option = input("Choose an option (1/2/3/4): ")

# Enter numbers to operate
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Select function
if option == '1':
	print(num1, "+", num2, "=", addition(num1, num2))

elif option == '2':
	print(num1, "-", num2, "=", subtraction(num1, num2))

elif option == '3':
	print(num1, "*", num2, "=", multiplication(num1, num2))

elif option == '4':
	if num2 == 0:
    	print("Error: Cannot divide by zero")
	else:
    	print(num1, "/", num2, "=", division(num1, num2))

else:
	print("Invalid option")
