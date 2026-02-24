# Question 2: Simple Calculator
# Difficulty: Easy | Points: 2 | Time: 15 min
# Create a program that:
# 1. Asks user for two numbers
# 2. Performs and displays: Addition, Subtraction, Multiplication, Division, Modulus,
# Exponentiation
# Sample Output:
# Enter first number: 10
# Enter second number: 3
# Results:
# 10 + 3 = 13
# 10 - 3 = 7
# 10 * 3 = 30
# 10 / 3 = 3.33
# 10 % 3 = 1
# 10 ^ 3 = 1000

# --- Write your solution below this line ---

print("\n\n\n=== Q02: Simple Calculator ===\n\n\n")

try:
    # Asks user to enter 2 numbers
    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    print("\nResults:")

    # Addition
    print(f"{num1} + {num2} = {num1 + num2}")

    # Subtraction
    print(f"{num1} - {num2} = {num1 - num2}")

    # Multiplication
    print(f"{num1} * {num2} = {num1 * num2}")

    # Division - check for zero before dividing
    if num2 == 0:
        print(f"{num1} / {num2} = Cannot divide by zero")
    else:
        print(f"{num1} / {num2} = {num1 / num2:.2f}")

    # Modulus - check for zero before using %
    if num2 == 0:
        print(f"{num1} % {num2} = Cannot modulus by zero")
    else:
        print(f"{num1} % {num2} = {num1 % num2}")

    # Exponentiation
    print(f"{num1} ^ {num2} = {num1 ** num2}")

except ValueError:
    print("Error: Please enter valid numbers only.")


# OUTPUT:

# PS C:\Users\...\Documents\Genai\Assignment2> python q02_simple_calculator.py
# Enter first number: 10
# Enter second number: 3

# Results:
# 10.0 + 3.0 = 13.0
# 10.0 - 3.0 = 7.0
# 10.0 * 3.0 = 30.0
# 10.0 / 3.0 = 3.33
# 10.0 % 3.0 = 1.0
# 10.0 ^ 3.0 = 1000.0