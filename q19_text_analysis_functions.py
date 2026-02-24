# Question 19: Text Analysis Functions
# Difficulty: Hard | Points: 9 | Time: 40 min
# Create the following text analysis functions:
# 1. count_words(text) - return number of words
# 2. count_vowels(text) - return number of vowels
# 3. count_consonants(text) - return number of consonants
# 4. reverse_text(text) - return reversed text
# 5. is_palindrome(text) - return True/False
# 6. remove_vowels(text) - return text without vowels
# 7. word_frequency(text) - return dictionary of word counts
# 8. longest_word(text) - return longest word
# 9. analyze_text(text) - calls all above functions and displays results
# Sample Output:
# Enter text: Hello World Hello
# === TEXT ANALYSIS ===
# Words: 3
# Vowels: 4
# Consonants: 8
# Reversed: olleH dlroW olleH
# Palindrome: No
# Without vowels: Hll Wrld Hll
# Longest word: Hello (5 letters)
# Word Frequency: hello: 2, world: 1

# --- Write your solution below this line ---

print("\n\n\n=== Q19: Text Analysis Functions ===\n\n\n")

def count_words(t):      return len(t.split())
def count_vowels(t):
    count = 0
    for c in t:
        if c in "aeiouAEIOU":
            count += 1
    return count

def count_consonants(t):
    count = 0
    for c in t:
        if c.isalpha() and c not in "aeiouAEIOU":
            count += 1
    return count

def reverse_text(t):     return t[::-1]

def is_palindrome(t):
    c = t.replace(" ", "").lower()
    return c == c[::-1]

def remove_vowels(t):
    result = ""
    for c in t:
        if c not in "aeiouAEIOU":
            result += c
    return result

def longest_word(t):     return max(t.split(), key=len)

def word_frequency(t):
    counts = {}
    for word in t.lower().split():
        counts[word] = counts.get(word, 0) + 1
    return counts

def format_frequency(freq):
    freq_str = ""
    for k, v in freq.items():
        freq_str += f"{k}: {v}, "
    return freq_str.rstrip(", ")

def analyze_text(t):
    lw       = longest_word(t)
    freq     = word_frequency(t)
    freq_str = format_frequency(freq)   # uses our new function

    print(f"\n=== TEXT ANALYSIS ===")
    print(f"Words: {count_words(t)}")
    print(f"Vowels: {count_vowels(t)}")
    print(f"Consonants: {count_consonants(t)}")
    print(f"Reversed: {reverse_text(t)}")
    print(f"Palindrome: {'Yes' if is_palindrome(t) else 'No'}")
    print(f"Without vowels: {remove_vowels(t)}")
    print(f"Longest word: {lw} ({len(lw)} letters)")
    print(f"Word Frequency: {freq_str}")

text = input("Enter text: ")
if text.strip() == "":
    print("empty input bruh")
else:
    analyze_text(text)


# OUTPUT:

# PS C:\Users\...\Documents\Genai\Assignment2> python q19_text_analysis_functions.py  

# Enter text: She drove a racecar and a kayak

# === TEXT ANALYSIS ===
# Words: 7
# Vowels: 11
# Consonants: 14
# Reversed: kayak a dna racecar a evord ehS
# Palindrome: No
# Without vowels: Sh drv  rccr nd  kyk
# Longest word: racecar (7 letters)
# Word Frequency: she: 1, drove: 1, a: 2, racecar: 1, and: 1, kayak: 1