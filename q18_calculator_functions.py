# Question 18: Calculator Functions
# Difficulty: Medium | Points: 7 | Time: 30 min
# Create a calculator using functions.
# Required Functions:
# 1. add(a, b)
# 2. subtract(a, b)
# 3. multiply(a, b)
# 4. divide(a, b) - handle division by zero
# 5. modulus(a, b)
# 6. power(a, b)
# 7. calculator() - main function with menu
# The calculator() function should display a menu, take user input, call the appropriate function,
# and display the result. Include an Exit option.

# --- Write your solution below this line ---

print("\n\n\n=== Q18: Calculator Functions ===\n\n\n")

import math  # only used for bonus: square root

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def modulus(a, b):  return "cant % by 0" if b == 0 else a % b
def power(a, b):    return a ** b

def divide(a, b):
    if b == 0: return "cant divide by 0"
    return round(a / b, 2)

def square_root(a, _=None):   # bonus - only needs one number
    if a < 0: return "cant sqrt a negative"
    return round(math.sqrt(a), 4)

def calculator():
    ops = {1: add, 2: subtract, 3: multiply, 4: divide, 5: modulus, 6: power, 7: square_root}
    while True:
        print("\n=== CALCULATOR ===")
        print("1.Add\n2.Sub\n3.Mul\n4.Div\n5.Mod\n6.Pow\n7.Sqrt (BONUS)\n8.Exit\n")
        try:
            ch = int(input("Choice: "))
            if ch == 8:
                print("bye!")
                break
            if ch not in ops:
                print("pick 1-8")
                continue
            a = float(input("Num 1: "))
            if ch == 7:   # sqrt only needs one number
                print(f"= {square_root(a)}")
            else:
                b = float(input("Num 2: "))
                print(f"= {ops[ch](a, b)}")
        except ValueError:
            print("numbers only")

calculator()


# OUTPUT:

# PS C:\Users\...\Documents\Genai\Assignment2> python q18_calculator_functions.py

# === CALCULATOR ===
# 1.Add
# 2.Sub
# 3.Mul
# 4.Div
# 5.Mod
# 6.Pow
# 7.Sqrt (BONUS)
# 8.Exit

# Choice: 1
# Num 1: 89+21
# numbers only

# === CALCULATOR ===
# 1.Add
# 2.Sub
# 3.Mul
# 4.Div
# 5.Mod
# 6.Pow
# 7.Sqrt (BONUS)
# 8.Exit

# Choice: 1
# Num 1: 89
# Num 2: 21
# = 110.0

# === CALCULATOR ===
# 1.Add
# 2.Sub
# 3.Mul
# 4.Div
# 5.Mod
# 6.Pow
# 7.Sqrt (BONUS)
# 8.Exit

# Choice: 2
# Num 1: 56   
# Num 2: 96
# = -40.0

# === CALCULATOR ===
# 1.Add
# 2.Sub
# 3.Mul
# 4.Div
# 5.Mod
# 6.Pow
# 7.Sqrt (BONUS)
# 8.Exit

# Choice: 3
# Num 1: 3
# Num 2: 5
# = 15.0

# === CALCULATOR ===
# 1.Add
# 2.Sub
# 3.Mul
# 4.Div
# 5.Mod
# 6.Pow
# 7.Sqrt (BONUS)
# 8.Exit

# Choice: 4
# Num 1: 5
# Num 2: 2
# = 2.5

# === CALCULATOR ===
# 1.Add
# 2.Sub
# 3.Mul
# 4.Div
# 5.Mod
# 6.Pow
# 7.Sqrt (BONUS)
# 8.Exit

# Choice: 4
# Num 1: 5
# Num 2: 0
# = cant divide by 0

# === CALCULATOR ===
# 1.Add
# 2.Sub
# 3.Mul
# 4.Div
# 5.Mod
# 6.Pow
# 7.Sqrt (BONUS)
# 8.Exit

# Choice: 5
# Num 1: 8
# Num 2: 2
# = 0.0

# === CALCULATOR ===
# 1.Add
# 2.Sub
# 3.Mul
# 4.Div
# 5.Mod
# 6.Pow
# 7.Sqrt (BONUS)
# 8.Exit

# Choice: 5
# Num 1: 3
# Num 2: 0
# = cant % by 0

# === CALCULATOR ===
# 1.Add
# 2.Sub
# 3.Mul
# 4.Div
# 5.Mod
# 6.Pow
# 7.Sqrt (BONUS)
# 8.Exit

# Choice: 6
# Num 1: 9
# Num 2: 3
# = 729.0

# === CALCULATOR ===
# 1.Add
# 2.Sub
# 3.Mul
# 4.Div
# 5.Mod
# 6.Pow
# 7.Sqrt (BONUS)
# 8.Exit

# Choice: 7
# Num 1: 81
# = 9.0

# === CALCULATOR ===
# 1.Add
# 2.Sub
# 3.Mul
# 4.Div
# 5.Mod
# 6.Pow
# 7.Sqrt (BONUS)
# 8.Exit

# Choice: 8
# bye!