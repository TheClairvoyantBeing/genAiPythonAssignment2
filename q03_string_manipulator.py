# Question 3: String Manipulator
# Difficulty: Medium | Points: 4 | Time: 20 min
# Ask user for a sentence and display:
# 1. Original sentence
# 2. Total characters (with spaces)
# 3. Total characters (without spaces)
# 4. Total words
# 5. UPPERCASE
# 6. lowercase
# 7. Title Case
# 8. First word
# 9. Last word
# 10. Reversed sentence
# Sample Output:
# Enter a sentence: Hello World Python
# Original: Hello World Python
# Characters (with spaces): 18
# Characters (without spaces): 16
# Words: 3
# UPPERCASE: HELLO WORLD PYTHON
# lowercase: hello world python
# Title Case: Hello World Python
# First word: Hello
# Last word: Python
# Reversed: nohtyP dlroW olleH

# --- Write your solution below this line ---

print("\n\n\n=== Q03: String Manipulator ===\n\n\n")

# Ask the user to enter a sentence
sentence = input("Enter a sentence: ")

# Handle empty input
if sentence.strip() == "":
    print("Error: You entered an empty sentence.")
else:
    # Split the sentence into a list of words
    words = sentence.split()

    print(f"\nOriginal: {sentence}")

    # Count characters including spaces
    print(f"Characters (with spaces): {len(sentence)}")

    # Count characters excluding spaces
    print(f"Characters (without spaces): {len(sentence.replace(' ', ''))}")

    # Count words
    print(f"Words: {len(words)}")

    # Convert to uppercase
    print(f"UPPERCASE: {sentence.upper()}")

    # Convert to lowercase
    print(f"lowercase: {sentence.lower()}")

    # Convert to title case
    print(f"Title Case: {sentence.title()}")

    # Get the first word
    print(f"First word: {words[0]}")

    # Get the last word
    print(f"Last word: {words[-1]}")

    # Reverse the entire sentence
    print(f"Reversed: {sentence[::-1]}")


# OUTPUT:
# PS C:\Users\...\Documents\Genai\Assignment2> python q03_string_manipulator.py
# Enter a sentence: Hello World Python

# Original: Hello World Python
# Characters (with spaces): 18
# Characters (without spaces): 16
# Words: 3
# UPPERCASE: HELLO WORLD PYTHON
# lowercase: hello world python
# Title Case: Hello World Python
# First word: Hello
# Last word: Python
# Reversed: nohtyP dlroW olleH
