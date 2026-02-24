# Question 20: Number System Functions
# Difficulty: Hard | Points: 9 | Time: 45 min
# Create the following mathematical functions:
# 1. factorial(n) - return n!
# 2. is_prime(n) - return True if prime
# 3. fibonacci(n) - return nth Fibonacci number
# 4. sum_of_digits(n) - return sum of digits
# 5. reverse_number(n) - return number reversed
# 6. is_armstrong(n) - check if Armstrong number (e.g., 153 = 1³ + 5³ + 3³)
# 7. gcd(a, b) - greatest common divisor
# 8. lcm(a, b) - least common multiple
# 9. is_perfect_number(n) - sum of divisors equals n (e.g., 6 = 1+2+3)
# 10. math_menu() - menu to test all functions
# Each function should be callable individually from the menu with appropriate user input.

# --- Write your solution below this line ---

print("\n\n\n=== Q20: Number System Functions ===\n\n\n")

# 1. Factorial
def factorial(n):
    if n < 0:  return None
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# 2. Is Prime
def is_prime(n):
    if n < 2: return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0: return False
    return True

# 3. Fibonacci - returns the nth number (0-indexed)
def fibonacci(n):
    if n < 0:   return None
    if n == 0:  return 0
    if n == 1:  return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b

# 4. Sum of digits
def sum_of_digits(n):
    return sum(int(d) for d in str(abs(n)))

# 5. Reverse a number
def reverse_number(n):
    return int(str(abs(n))[::-1])

# 6. Armstrong number (each digit raised to power = no. of digits)
def is_armstrong(n):
    digits = str(abs(n))
    power  = len(digits)
    return sum(int(d) ** power for d in digits) == n

# 7. GCD - Euclidean algorithm
def gcd(a, b):
    while b:
        a, b = b, a % b
    return abs(a)

# 8. LCM - uses GCD
def lcm(a, b):
    return abs(a * b) // gcd(a, b)

# 9. Perfect number
def is_perfect_number(n):
    if n < 2: return False
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

# 10. Main menu
def math_menu():
    while True:
        print("\n=== NUMBER SYSTEM FUNCTIONS ===")
        print("1.  Factorial")
        print("2.  Is Prime?")
        print("3.  Fibonacci (nth term)")
        print("4.  Sum of Digits")
        print("5.  Reverse Number")
        print("6.  Is Armstrong?")
        print("7.  GCD")
        print("8.  LCM")
        print("9.  Is Perfect Number?")
        print("10. Exit")

        try:
            ch = int(input("\nChoice: "))

            if ch == 10:
                print("bye!")
                break

            elif ch == 1:
                n = int(input("Enter n: "))
                result = factorial(n)
                print(f"{n}! = {result}" if result is not None else "No factorial for negatives")

            elif ch == 2:
                n = int(input("Enter n: "))
                print(f"{n} is {'PRIME' if is_prime(n) else 'NOT prime'}")

            elif ch == 3:
                n = int(input("Enter position (0-indexed): "))
                result = fibonacci(n)
                print(f"Fibonacci({n}) = {result}" if result is not None else "Position must be >= 0")

            elif ch == 4:
                n = int(input("Enter n: "))
                print(f"Sum of digits of {n} = {sum_of_digits(n)}")

            elif ch == 5:
                n = int(input("Enter n: "))
                print(f"Reverse of {n} = {reverse_number(n)}")

            elif ch == 6:
                n = int(input("Enter n: "))
                print(f"{n} is {'an Armstrong' if is_armstrong(n) else 'NOT an Armstrong'} number")

            elif ch == 7:
                a = int(input("Enter a: "))
                b = int(input("Enter b: "))
                print(f"GCD({a}, {b}) = {gcd(a, b)}")

            elif ch == 8:
                a = int(input("Enter a: "))
                b = int(input("Enter b: "))
                print(f"LCM({a}, {b}) = {lcm(a, b)}")

            elif ch == 9:
                n = int(input("Enter n: "))
                print(f"{n} is {'a PERFECT' if is_perfect_number(n) else 'NOT a perfect'} number")

            else:
                print("pick 1-10")

        except ValueError:
            print("numbers only pls")

math_menu()


# OUTPUT:

# PS C:\Users\...\Documents\Genai\Assignment2> python q20_number_system_functions.py

# === NUMBER SYSTEM FUNCTIONS ===
# 1.  Factorial
# 2.  Is Prime?
# 3.  Fibonacci (nth term)
# 4.  Sum of Digits
# 5.  Reverse Number
# 6.  Is Armstrong?
# 7.  GCD
# 8.  LCM
# 9.  Is Perfect Number?
# 10. Exit

# Choice: 1
# Enter n: 5
# 5! = 120

# === NUMBER SYSTEM FUNCTIONS ===
# 1.  Factorial
# 2.  Is Prime?
# 3.  Fibonacci (nth term)
# 4.  Sum of Digits
# 5.  Reverse Number
# 6.  Is Armstrong?
# 7.  GCD
# 8.  LCM
# 9.  Is Perfect Number?
# 10. Exit

# Choice: 2
# Enter n: 17
# 17 is PRIME

# === NUMBER SYSTEM FUNCTIONS ===
# 1.  Factorial
# 2.  Is Prime?
# 3.  Fibonacci (nth term)
# 4.  Sum of Digits
# 5.  Reverse Number
# 6.  Is Armstrong?
# 7.  GCD
# 8.  LCM
# 9.  Is Perfect Number?
# 10. Exit

# Choice: 3
# Enter position (0-indexed): 7
# Fibonacci(7) = 13

# === NUMBER SYSTEM FUNCTIONS ===
# 1.  Factorial
# 2.  Is Prime?
# 3.  Fibonacci (nth term)
# 4.  Sum of Digits
# 5.  Reverse Number
# 6.  Is Armstrong?
# 7.  GCD
# 8.  LCM
# 9.  Is Perfect Number?
# 10. Exit

# Choice: 4
# Enter n: 1234
# Sum of digits of 1234 = 10

# === NUMBER SYSTEM FUNCTIONS ===
# 1.  Factorial
# 2.  Is Prime?
# 3.  Fibonacci (nth term)
# 4.  Sum of Digits
# 5.  Reverse Number
# 6.  Is Armstrong?
# 7.  GCD
# 8.  LCM
# 9.  Is Perfect Number?
# 10. Exit

# Choice: 5
# Enter n: 12345
# Reverse of 12345 = 54321

# === NUMBER SYSTEM FUNCTIONS ===
# 1.  Factorial
# 2.  Is Prime?
# 3.  Fibonacci (nth term)
# 4.  Sum of Digits
# 5.  Reverse Number
# 6.  Is Armstrong?
# 7.  GCD
# 8.  LCM
# 9.  Is Perfect Number?
# 10. Exit

# Choice: 6
# Enter n: 153
# 153 is an Armstrong number

# === NUMBER SYSTEM FUNCTIONS ===
# 1.  Factorial
# 2.  Is Prime?
# 3.  Fibonacci (nth term)
# 4.  Sum of Digits
# 5.  Reverse Number
# 6.  Is Armstrong?
# 7.  GCD
# 8.  LCM
# 9.  Is Perfect Number?
# 10. Exit

# Choice: 7
# Enter a: 12
# Enter b: 8
# GCD(12, 8) = 4

# === NUMBER SYSTEM FUNCTIONS ===
# 1.  Factorial
# 2.  Is Prime?
# 3.  Fibonacci (nth term)
# 4.  Sum of Digits
# 5.  Reverse Number
# 6.  Is Armstrong?
# 7.  GCD
# 8.  LCM
# 9.  Is Perfect Number?
# 10. Exit

# Choice: 8
# Enter a: 4
# Enter b: 6
# LCM(4, 6) = 12

# === NUMBER SYSTEM FUNCTIONS ===
# 1.  Factorial
# 2.  Is Prime?
# 3.  Fibonacci (nth term)
# 4.  Sum of Digits
# 5.  Reverse Number
# 6.  Is Armstrong?
# 7.  GCD
# 8.  LCM
# 9.  Is Perfect Number?
# 10. Exit

# Choice: 9
# Enter n: 28
# 28 is a PERFECT number

# === NUMBER SYSTEM FUNCTIONS ===
# 1.  Factorial
# 2.  Is Prime?
# 3.  Fibonacci (nth term)
# 4.  Sum of Digits
# 5.  Reverse Number
# 6.  Is Armstrong?
# 7.  GCD
# 8.  LCM
# 9.  Is Perfect Number?
# 10. Exit

# Choice: 10
# bye!