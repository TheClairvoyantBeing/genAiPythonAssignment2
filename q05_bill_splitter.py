# Question 5: Bill Splitter
# Difficulty: Medium | Points: 4 | Time: 25 min
# Create a restaurant bill splitting program.
# Inputs: Total bill amount, Number of people, Tax percentage, Tip percentage
# Calculate and Display: Subtotal, Tax amount, Bill after tax, Tip amount, Total bill, Amount per person
# Sample Output:
# Enter total bill: 1000
# Number of people: 4
# Tax percentage: 10
# Tip percentage: 15
# === BILL BREAKDOWN ===
# Subtotal: ₹1000.00
# Tax (10%): ₹100.00
# After tax: ₹1100.00
# Tip (15%): ₹165.00
# Total: ₹1265.00
# Per person: ₹316.25

# --- Write your solution below this line ---

print("\n\n\n=== Q05: Bill Splitter ===\n\n\n")

try:
    # Get inputs from the user
    total_bill  = float(input("Enter total bill: "))
    people      = int(input("Number of people: "))
    tax_percent = float(input("Tax percentage: "))
    tip_percent = float(input("Tip percentage: "))

    # Edge case: zero or negative people
    if people <= 0:
        print("Error: Number of people must be at least 1.")
    else:
        # Calculates tax
        tax_amount = total_bill * (tax_percent / 100)

        # Bill after tax
        after_tax = total_bill + tax_amount

        # Tip is calculated on the original (not after-tax)
        tip_amount = total_bill * (tip_percent / 100)

        # Final total and split
        total     = after_tax + tip_amount
        per_person = total / people

        #\u20b9 used for ₹
        print("\n=== BILL BREAKDOWN ===")
        print(f"Subtotal:       \u20b9{total_bill:.2f}")
        print(f"Tax ({tax_percent}%):       \u20b9{tax_amount:.2f}")
        print(f"After tax:      \u20b9{after_tax:.2f}")
        print(f"Tip ({tip_percent}%):       \u20b9{tip_amount:.2f}")
        print(f"Total:          \u20b9{total:.2f}")
        print(f"Per person:     \u20b9{per_person:.2f}")

except ValueError:
    print("Error: Please enter valid numbers.")


# OUTPUT:
# PS C:\Users\...\Documents\Genai\Assignment2> python q05_bill_splitter.py
# Enter total bill: 1000
# Number of people: 4
# Tax percentage: 10
# Tip percentage: 15

# === BILL BREAKDOWN ===
# Subtotal:       ₹1000.00
# Tax (10.0%):       ₹100.00
# After tax:      ₹1100.00
# Tip (15.0%):       ₹150.00
# Total:          ₹1250.00
# Per person:     ₹312.50
