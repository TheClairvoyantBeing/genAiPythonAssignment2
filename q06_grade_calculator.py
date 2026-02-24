# Question 6: Grade Calculator
# Difficulty: Easy-Medium | Points: 4 | Time: 20 min
# Ask users for marks in 5 subjects (out of 100 each). Calculate and display:
# 1. Marks in each subject
# 2. Total marks (out of 500)
# 3. Percentage
# 4. Grade
# 5. Result: Pass/Fail (Pass if all subjects >= 40)
# Grade Scale:
# 90-100% : A+ (Outstanding)
# 80-89% : A (Excellent)
# 70-79% : B (Good)
# 60-69% : C (Average)
# 50-59%: D (Pass)
# Below 50%: F (Fail)

# --- Write your solution below this line ---

print("\n\n\n=== Q06: Grade Calculator ===\n\n\n")

marks = []

# Collect marks for 5 subjects using a loop
for i in range(1, 6):
    while True:
        try:
            mark = float(input(f"Enter marks for Subject {i} (out of 100): "))

            # Edge case: checks for marks as it must be between 0 and 100
            if mark < 0 or mark > 100:
                print("Error: Marks must be between 0 and 100. Try again.")
            else:
                marks.append(mark)
                break

        except ValueError:
            print("Error: Please enter a valid number.")

# Calculate total and percentage
total      = sum(marks)
percentage = (total / 500) * 100

# Check if all subjects have passing marks (>= 40)
is_pass = all(mark >= 40 for mark in marks)

# Determine grade based on percentage
if percentage >= 90:
    grade = "A+ (Outstanding)"
elif percentage >= 80:
    grade = "A (Excellent)"
elif percentage >= 70:
    grade = "B (Good)"
elif percentage >= 60:
    grade = "C (Average)"
elif percentage >= 50:
    grade = "D (Pass)"
else:
    grade = "F (Fail)"

# Display the grade report
print("\n=== GRADE REPORT ===")
for i, mark in enumerate(marks, 1):
    print(f"Subject {i} : {mark}")
print("-------------------")
print(f"Total     : {total} / 500")
print(f"Percentage: {percentage:.2f}%")
print(f"Grade     : {grade}")
print(f"Result    : {'PASS' if is_pass else 'FAIL'}")


# OUTPUT:
# PS C:\Users\...\Documents\Genai\Assignment2> python q06_grade_calculator.py
# Enter marks for Subject 1 (out of 100): 50
# Enter marks for Subject 2 (out of 100): 25
# Enter marks for Subject 3 (out of 100): 75
# Enter marks for Subject 4 (out of 100): 90
# Enter marks for Subject 5 (out of 100): 35

# === GRADE REPORT ===
# Subject 1 : 50.0
# Subject 2 : 25.0
# Subject 3 : 75.0
# Subject 4 : 90.0
# Subject 5 : 35.0
# -------------------
# Total     : 275.0 / 500
# Percentage: 55.00%
# Grade     : D (Pass)
# Result    : FAIL