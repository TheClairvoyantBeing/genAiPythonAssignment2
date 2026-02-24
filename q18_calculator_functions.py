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

def add(a, b):      return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def modulus(a, b):  return "cant % by 0" if b == 0 else a % b
def power(a, b):    return a ** b

def divide(a, b):
    if b == 0: return "cant divide by 0"
    return round(a / b, 2)

def calculator():
    ops = {1: add, 2: subtract, 3: multiply, 4: divide, 5: modulus, 6: power}
    while True:
        print("\n=== CALCULATOR ===")
        print("1.Add\n2.Sub\n3.Mul\n4.Div\n5.Mod\n6.Pow\n7.Exit\n")
        try:
            ch = int(input("Choice: "))
            if ch == 7:
                print("bye!")
                break
            if ch not in ops:
                print("pick 1-7")
                continue
            a = float(input("Num 1: "))
            b = float(input("Num 2: "))
            print(f"= {ops[ch](a, b)}")
        except ValueError:
            print("numbers only")

calculator()


# OUTPUT:
# Choice: 4
# Num 1: 10
# Num 2: 3
# = 3.33
#
# Choice: 7
# bye!
