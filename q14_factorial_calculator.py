# Question 14: Factorial Calculator
# Difficulty: Medium | Points: 4 | Time: 20 min
# Calculate factorial of a number using a loop. Factorial: n! = n × (n-1) × (n-2) × ... × 1
# Requirements:
# - Handle 0 and negative numbers
# - Display step-by-step calculation
# Sample Output:
# Enter a number: 5
# 5! = 5 × 4 × 3 × 2 × 1 = 120

# --- Write your solution below this line ---

print("\n\n\n=== Q14: Factorial Calculator ===\n\n\n")

def factorial(n):
    result = 1
    steps  = []
    for i in range(n, 0, -1):
        result *= i
        steps.append(str(i))
    return result, " x ".join(steps)

try:
    num = int(input("Enter a number: "))

    if num < 0:
        print(f"{num}! = Undefined")
    elif num == 0:
        print("0! = 1")
    else:
        result, steps = factorial(num)
        print(f"{num}! = {steps} = {result}")

except ValueError:
    print("numbers only pls")


# OUTPUT:
# PS C:\Users\...\Documents\Genai\Assignment2> python q14_factorial_calculator.py

# Enter a number: 9
# 9! = 9 x 8 x 7 x 6 x 5 x 4 x 3 x 2 x 1 = 362880