# Question 13: Sum and Average Calculator
# Difficulty: Easy | Points: 4 | Time: 20 min
# Ask the user how many numbers they want to add. Then take that many numbers as input using a loop.
# Calculate: 1. Sum 2. Average 3. Maximum number 4. Minimum number
# Sample Output:
# How many numbers? 5
# Enter number 1: 10
# Enter number 2: 20
# ...
# Sum: 100
# Average: 20.0
# Maximum: 30
# Minimum: 10
# Bonus (+3 points): Add statistical analysis: Median and Mode calculations.

# --- Write your solution below this line ---

print("\n\n\n=== Q13: Sum and Average Calculator ===\n\n\n")

try:
    count = int(input("How many numbers? "))

    if count <= 0:
        print("enter at least 1")
    else:
        numbers = []
        for i in range(1, count+1):
            n = float(input(f"Enter number {i}: "))
            numbers.append(n)

        total = sum(numbers)
        avg   = total / count

        print(f"\nSum: {total}")
        print(f"Average: {avg}")
        print(f"Maximum: {max(numbers)}")   # built-in max
        print(f"Minimum: {min(numbers)}")   # built-in min

        # BONUS: Median + Mode
        sorted_nums = sorted(numbers)
        mid = count // 2

        # median: middle val if odd, avg of 2 middles if even
        if count % 2 == 1:
            median = sorted_nums[mid]
        else:
            median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

        # mode: most freq number using a dictionary
        freq = {}
        for n in numbers:
            freq[n] = freq.get(n, 0) + 1
        max_freq = max(freq.values())
        modes = [k for k, v in freq.items() if v == max_freq]

        print(f"\n--- BONUS ---")
        print(f"Median: {median}")
        if len(modes) == len(numbers):
            print("Mode: No mode (all values unique)")
        else:
            print(f"Mode: {', '.join(str(m) for m in modes)}")

except ValueError:
    print("numbers only pls")




# USING INBUILT FUNCTIONS (BONUS)
# import statistics

# print(f"Mean   : {statistics.mean(numbers)}")
# print(f"Median : {statistics.median(numbers)}")
# print(f"Mode   : {statistics.mode(numbers)}")



# OUTPUT:
# PS C:\Users\...\Documents\Genai\Assignment2> python q13_sum_and_average_calculator.py
# How many numbers? 5
# Enter number 1: 10
# Enter number 2: 20
# Enter number 3: 30
# Enter number 4: 25
# Enter number 5: 10

# Sum: 95.0
# Average: 19.0
# Maximum: 30.0
# Minimum: 10.0

# --- BONUS ---
# Median: 20.0
# Mode: 10.0
