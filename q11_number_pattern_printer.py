# Question 11: Number Pattern Printer
# Difficulty: Medium | Points: 4 | Time: 25 min
# Create a program that prints the following patterns. User should choose which pattern and
# height.
# Pattern 1:
# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# Pattern 2:
# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# Pattern 3:
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1
# Pattern 4:
# 1
# 121
# 12321
# 1234321
# 123454321

# --- Write your solution below this line ---

print("\n\n\n=== Q11: Number Pattern Printer ===\n\n\n")

while True:
    print("\n=== NUMBER PATTERN PRINTER ===")
    print("1. Incremental Triangle   (1 / 1 2 / 1 2 3)")
    print("2. Same Number Triangle   (1 / 2 2 / 3 3 3)")
    print("3. Reverse Countdown      (5 4 3 / 4 3 2 ...)")
    print("4. Number Pyramid         (1 / 121 / 12321)")
    print("5. Right-Aligned Triangle")
    print("6. Diamond")
    print("7. Exit")

    try:
        ch = int(input("\nChoice: "))

        if ch == 7:
            print("bye!")
            break

        if ch not in range(1, 7):
            print("pick 1-7")
            continue

        n = int(input("Enter height: "))
        if n < 1:
            print("enter valid height bruh")
            continue

        print()

        if ch == 1:
            # 1 / 1 2 / 1 2 3 ...
            for i in range(1, n+1):
                for j in range(1, i+1):
                    print(j, end=" ")
                print()

        elif ch == 2:
            # 1 / 2 2 / 3 3 3 ...
            for i in range(1, n+1):
                for j in range(i):
                    print(i, end=" ")
                print()

        elif ch == 3:
            # reverse countdown per row
            for i in range(n, 0, -1):
                for j in range(i, 0, -1):
                    print(j, end=" ")
                print()

        elif ch == 4:
            # pyramid: 1 / 121 / 12321 ...
            for i in range(1, n+1):
                row = list(range(1, i+1)) + list(range(i-1, 0, -1))
                print(*row)

        elif ch == 5:
            # right-aligned triangle
            for i in range(1, n+1):
                print(" " * (n-i), end="")
                for j in range(1, i+1):
                    print(j, end=" ")
                print()

        elif ch == 6:
            # diamond - goes up then comes back down
            for i in range(1, n+1):
                row = list(range(1, i+1)) + list(range(i-1, 0, -1))
                print(" " * (n-i) + " ".join(str(x) for x in row))
            for i in range(n-1, 0, -1):
                row = list(range(1, i+1)) + list(range(i-1, 0, -1))
                print(" " * (n-i) + " ".join(str(x) for x in row))

    except ValueError:
        print("numbers only pls")


# OUTPUT 

# PS C:\Users\...\Documents\Genai\Assignment2> python q11_number_pattern_printer.py

# === NUMBER PATTERN PRINTER ===
# 1. Incremental Triangle   (1 / 1 2 / 1 2 3)
# 2. Same Number Triangle   (1 / 2 2 / 3 3 3)
# 3. Reverse Countdown      (5 4 3 / 4 3 2 ...)
# 4. Number Pyramid         (1 / 121 / 12321)
# 5. Right-Aligned Triangle
# 6. Diamond
# 7. Exit

# Choice: 1
# Enter height: 9

# 1
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5
# 1 2 3 4 5 6
# 1 2 3 4 5 6 7
# 1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9

# === NUMBER PATTERN PRINTER ===
# 1. Incremental Triangle   (1 / 1 2 / 1 2 3)
# 2. Same Number Triangle   (1 / 2 2 / 3 3 3)
# 3. Reverse Countdown      (5 4 3 / 4 3 2 ...)
# 4. Number Pyramid         (1 / 121 / 12321)
# 5. Right-Aligned Triangle
# 6. Diamond
# 7. Exit

# Choice: 2
# Enter height: 9

# 1
# 2 2
# 3 3 3
# 4 4 4 4
# 5 5 5 5 5
# 6 6 6 6 6 6
# 7 7 7 7 7 7 7
# 8 8 8 8 8 8 8 8
# 9 9 9 9 9 9 9 9 9

# === NUMBER PATTERN PRINTER ===
# 1. Incremental Triangle   (1 / 1 2 / 1 2 3)
# 2. Same Number Triangle   (1 / 2 2 / 3 3 3)
# 3. Reverse Countdown      (5 4 3 / 4 3 2 ...)
# 4. Number Pyramid         (1 / 121 / 12321)
# 5. Right-Aligned Triangle
# 6. Diamond
# 7. Exit

# Choice: 3
# Enter height: 9

# 9 8 7 6 5 4 3 2 1
# 8 7 6 5 4 3 2 1
# 7 6 5 4 3 2 1
# 6 5 4 3 2 1
# 5 4 3 2 1
# 4 3 2 1
# 3 2 1
# 2 1
# 1

# === NUMBER PATTERN PRINTER ===
# 1. Incremental Triangle   (1 / 1 2 / 1 2 3)
# 2. Same Number Triangle   (1 / 2 2 / 3 3 3)
# 3. Reverse Countdown      (5 4 3 / 4 3 2 ...)
# 4. Number Pyramid         (1 / 121 / 12321)
# 5. Right-Aligned Triangle
# 6. Diamond
# 7. Exit

# Choice: 4
# Enter height: 9

# 1
# 1 2 1
# 1 2 3 2 1
# 1 2 3 4 3 2 1
# 1 2 3 4 5 4 3 2 1
# 1 2 3 4 5 6 5 4 3 2 1
# 1 2 3 4 5 6 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1

# === NUMBER PATTERN PRINTER ===
# 1. Incremental Triangle   (1 / 1 2 / 1 2 3)
# 2. Same Number Triangle   (1 / 2 2 / 3 3 3)
# 3. Reverse Countdown      (5 4 3 / 4 3 2 ...)
# 4. Number Pyramid         (1 / 121 / 12321)
# 5. Right-Aligned Triangle
# 6. Diamond
# 7. Exit

# Choice: 5
# Enter height: 9

#         1
#        1 2
#       1 2 3
#      1 2 3 4
#     1 2 3 4 5
#    1 2 3 4 5 6
#   1 2 3 4 5 6 7
#  1 2 3 4 5 6 7 8
# 1 2 3 4 5 6 7 8 9

# === NUMBER PATTERN PRINTER ===
# 1. Incremental Triangle   (1 / 1 2 / 1 2 3)
# 2. Same Number Triangle   (1 / 2 2 / 3 3 3)
# 3. Reverse Countdown      (5 4 3 / 4 3 2 ...)
# 4. Number Pyramid         (1 / 121 / 12321)
# 5. Right-Aligned Triangle
# 6. Diamond
# 7. Exit

# Choice: 6
# Enter height: 9

#         1
#        1 2 1
#       1 2 3 2 1
#      1 2 3 4 3 2 1
#     1 2 3 4 5 4 3 2 1
#    1 2 3 4 5 6 5 4 3 2 1
#   1 2 3 4 5 6 7 6 5 4 3 2 1
#  1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
# 1 2 3 4 5 6 7 8 9 8 7 6 5 4 3 2 1
#  1 2 3 4 5 6 7 8 7 6 5 4 3 2 1
#   1 2 3 4 5 6 7 6 5 4 3 2 1
#    1 2 3 4 5 6 5 4 3 2 1
#     1 2 3 4 5 4 3 2 1
#      1 2 3 4 3 2 1
#       1 2 3 2 1
#        1 2 1
#         1

# === NUMBER PATTERN PRINTER ===
# 1. Incremental Triangle   (1 / 1 2 / 1 2 3)
# 2. Same Number Triangle   (1 / 2 2 / 3 3 3)
# 3. Reverse Countdown      (5 4 3 / 4 3 2 ...)
# 4. Number Pyramid         (1 / 121 / 12321)
# 5. Right-Aligned Triangle
# 6. Diamond
# 7. Exit

# Choice: 7
# bye!