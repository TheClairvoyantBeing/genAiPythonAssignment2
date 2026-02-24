# Question 17: Palindrome Checker
# Difficulty: Medium | Points: 4 | Time: 20 min
# Create a program that checks if a word/number is a palindrome (reads same forwards and backwards).
# Requirements: Check words (ignore case), check numbers, display step-by-step verification.
# Sample Output:
# Enter word/number: Racecar
# Original: Racecar
# Reversed: racecaR
# Result: PALINDROME

# --- Write your solution below this line ---

print("\n\n\n=== Q17: Palindrome Checker ===\n\n\n")

text  = input("Enter word/number: ")
clean = text.replace(" ", "").lower()  # strip spaces + lowercase for fair compare

print(f"Original: {text}")
print(f"Reversed: {text[::-1]}")

if clean == clean[::-1]:
    print("Result: PALINDROME ✔")
else:
    print("Result: NOT a palindrome ✘")


# OUTPUT:
# PS C:\Users\...\Documents\Genai\Assignment2> python q17_palindrome_checker.py

# Enter word/number: hanah
# Original: hanah
# Reversed: hanah
# Result: PALINDROME ✔
