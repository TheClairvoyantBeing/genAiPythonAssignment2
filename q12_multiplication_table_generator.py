# Question 12: Multiplication Table Generator
# Difficulty: Easy-Medium | Points: 4 | Time: 20 min
# Create a program that asks the user for a number and a range, then displays the multiplication table.
# Sample Output:
# Enter number: 7
# Enter range (end): 12
# Multiplication Table of 7
# 7 x 1 = 7
# 7 x 2 = 14
# ...
# 7 x 12 = 84
# Bonus (+3 points): Create a full multiplication table (1-10 for all numbers 1-10) in grid format.

# --- Write your solution below this line ---

print("\n\n\n=== Q12: Multiplication Table Generator ===\n\n\n")

try:
    num = int(input("Enter number: "))
    end = int(input("Enter range (end): "))

    print(f"\nMultiplication Table of {num}")
    for i in range(1, end+1):
        print(f"{num} x {i} = {num*i}")

except ValueError:
    print("numbers only pls")


# OUTPUT:
# PS C:\Users\...\Documents\Genai\Assignment2> python q12_multiplication_table_generator.py
# Enter number: 17
# Enter range (end): 15

# Multiplication Table of 17
# 17 x 1 = 17
# 17 x 2 = 34
# 17 x 3 = 51
# 17 x 4 = 68
# 17 x 5 = 85
# 17 x 6 = 102
# 17 x 7 = 119
# 17 x 8 = 136
# 17 x 9 = 153
# 17 x 10 = 170
# 17 x 11 = 187
# 17 x 12 = 204
# 17 x 13 = 221
# 17 x 14 = 238
# 17 x 15 = 255