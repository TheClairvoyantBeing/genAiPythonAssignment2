# Question 1: Personal Bio Card
# Difficulty: Easy | Points: 2 | Time: 10 min
# Write a program that displays your information in a formatted card:
# ╔════════════════════════════════╗
# ║ STUDENT BIO CARD               ║
# ╔════════════════════════════════╗
# ║ Name : John Doe                ║
# ║ Age : 20 years                 ║
# ║ Course : Python Programming    ║
# ║ College : ABC University       ║
# ║ Email : john@example.com       ║
# ╚════════════════════════════════╝
# Requirements:
# - Use variables for each field
# - Display in a nicely formatted box
# - Must be visually appealing

# --- Write your solution below this line ---

# Take input from the user
name    = input("Enter your name: ")
age     = input("Enter your age: ")
course  = input("Enter your course: ")
college = input("Enter your college: ")
email   = input("Enter your email: ")

# Print the bio card using box-drawing characters
# Note to me : the :<30 inside f-strings left-aligns the value in a 30-character wide space
print("╔═════════════════════════════════════════╗")
print("║           STUDENT BIO CARD              ║")
print("╠═════════════════════════════════════════╣")
print(f"║ Name    : {name:<30}║")
print(f"║ Age     : {age:<30}║")
print(f"║ Course  : {course:<30}║")
print(f"║ College : {college:<30}║")
print(f"║ Email   : {email:<30}║")
print("╚═════════════════════════════════════════╝")


# OUTPUT:

# PS C:\Users\...\Documents\Genai\Assignment2> python q01_personal_bio_card.py
# Enter your name: Jhon Doe
# Enter your age: 31
# Enter your course: Python Programming
# Enter your college: ABC University
# Enter your email: jhondoe@example.com
# ╔═════════════════════════════════════════╗
# ║           STUDENT BIO CARD              ║
# ╠═════════════════════════════════════════╣
# ║ Name    : Jhon Doe                      ║
# ║ Age     : 31                            ║
# ║ Course  : Python Programming            ║
# ║ College : ABC University                ║
# ║ Email   : jhondoe@example.com           ║
# ╚═════════════════════════════════════════╝
