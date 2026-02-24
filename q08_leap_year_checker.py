# Question 8: Leap Year Checker
# Difficulty: Medium | Points: 4 | Time: 20 min
# Create a program that checks if a year is a leap year.
# Rules: A year is a leap year if divisible by 4 AND (NOT divisible by 100 OR divisible by 400).
# Test Cases:
# 2024: Leap year
# 2100: NOT leap year
# 2000: Leap year
# 2023: NOT leap year
# Display the year, whether it is a leap year, and the reason why.

# --- Write your solution below this line ---

print("\n\n\n=== Q08: Leap Year Checker ===\n\n\n")

# Keep checking years until user enters 0 to exit
while True:
    try:
        year = int(input("\nEnter a year (or 0 to exit): "))

        if year == 0:
            break

        # Edge case: negative year
        if year < 0:
            print("Error: Please enter a positive year.")
            continue

        # Check leap year — order matters: check 400 first, then 100, then 4
        if year % 400 == 0:
            print(f"{year} is a LEAP YEAR")
            print(f"Reason: {year} is divisible by 400.")

        elif year % 100 == 0:
            # Century year NOT divisible by 400 — e.g. 1900, 2100
            print(f"{year} is NOT a leap year")
            print(f"Reason: {year} is divisible by 100 but not by 400.")

        elif year % 4 == 0:
            print(f"{year} is a LEAP YEAR")
            print(f"Reason: {year} is divisible by 4 and not divisible by 100.")

        else:
            print(f"{year} is NOT a leap year")
            print(f"Reason: {year} is not divisible by 4.")

    except ValueError:
        print("Error: Please enter a valid year.")


# OUTPUT:
# PS C:\Users\...\Documents\Genai\Assignment2> python q08_leap_year_checker.py

# Enter a year (or 0 to exit): 2004
# 2004 is a LEAP YEAR
# Reason: 2004 is divisible by 4 and not divisible by 100.

# Enter a year (or 0 to exit): 2000
# 2000 is a LEAP YEAR
# Reason: 2000 is divisible by 400.

# Enter a year (or 0 to exit): 1900
# 1900 is NOT a leap year
# Reason: 1900 is divisible by 100 but not by 400.

# Enter a year (or 0 to exit): -201
# Error: Please enter a positive year.

# Enter a year (or 0 to exit): 143
# 143 is NOT a leap year
# Reason: 143 is not divisible by 4.

# Enter a year (or 0 to exit): 0