# Question 4: Age Calculator
# Difficulty: Medium | Points: 4 | Time: 20 min
# Ask user for their birth year and calculate:
# 1. Current age
# 2. Age in months
# 3. Age in days (approx 365 days/year)
# 4. Age in hours
# 5. Age in minutes
# 6. Years until age 100
# Bonus (+2 points): Ask for an exact birth date (day, month, year) and calculate more precisely.

# --- Write your solution below this line ---

print("\n\n\n=== Q04: Age Calculator ===\n\n\n")

# Current year hardcoded (no datetime used)
current_year = 2026

try:
    birth_year = int(input("Enter your birth year: "))

    # Edge case: future year
    if birth_year > current_year:
        print("Error: Birth year cannot be in the future.")
    elif birth_year < 1900:
        print("Error: Birth year seems invalid.")
    else:
        # Calculate age in different units
        age = current_year - birth_year
        months = age * 12
        days = age * 365       # approx, 365 days/year as stated in PDF
        hours = days * 24
        minutes = hours * 60
        years_to_100 = 100 - age

        print(f"\nAge          : {age} years")
        print(f"In Months    : {months} months")
        print(f"In Days      : {days} days (approx.)")
        print(f"In Hours     : {hours} hours (approx.)")
        print(f"In Minutes   : {minutes} minutes (approx.)")
        print(f"Until 100    : {years_to_100} years remaining")

except ValueError:
    print("Error: Please enter a valid year.")


# OUTPUT:
# PS C:\Users\...\Documents\Genai\Assignment2> python q04_age_calculator.py
# Enter your birth year: 2004
#
# Age          : 22 years
# In Months    : 264 months
# In Days      : 8030 days (approx.)
# In Hours     : 192720 hours (approx.)
# In Minutes   : 11563200 minutes (approx.)
# Until 100    : 78 years remaining