# Question 9: Ticket Pricing System
# Difficulty: Medium | Points: 4 | Time: 25 min
# Create a movie ticket pricing system.
# Age-based Pricing:
# Below 3: Free
# 3-12: ₹150 (Child)
# 13-59: ₹300 (Adult)
# 60+: ₹200 (Senior)
# Day-based Discount:
# Monday-Thursday: No discount
# Friday-Sunday: 20% discount
# Inputs: Age, Day of week, Number of tickets
# Display base price, discount (if any), price after discount, and total amount.

# --- Write your solution below this line ---

print("\n\n\n=== Q09: Ticket Pricing System ===\n\n\n")

valid_days   = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
weekend_days = ["friday", "saturday", "sunday"]

try:
    age = int(input("Enter age: "))

    # Edge case: negative age
    if age < 0:
        print("Error: Age cannot be negative.")
    else:
        # Keep asking until a valid day is entered (handles typos)
        while True:
            day = input("Enter day of week: ").strip().lower()
            if day in valid_days:
                break
            else:
                print("Invalid day. Please enter a valid day (e.g. Monday, Friday).")

        tickets = int(input("Enter number of tickets: "))

        # Edge case: zero or negative tickets
        if tickets <= 0:
            print("Error: Number of tickets must be at least 1.")
        else:
            # Determine age category and base price
            if age < 3:
                base_price = 0
                category   = "Infant"
            elif age <= 12:
                base_price = 150
                category   = "Child"
            elif age <= 59:
                base_price = 300
                category   = "Adult"
            else:
                base_price = 200
                category   = "Senior"

            # Checking to see whether to apply 20% discount on weekends (Friday-Sunday)
            if day in weekend_days:
                discount = base_price * 0.20
                day_info = f"{day.capitalize()} (Weekend Rate)"
            else:
                discount = 0
                day_info = f"{day.capitalize()} (Weekday - No Discount)"

            price_per_ticket = base_price - discount
            total_amount     = price_per_ticket * tickets

            print("\n=== TICKET DETAILS ===")
            print(f"Category      : {category}")
            print(f"Base Price    : \u20b9{base_price:.2f} per ticket")
            print(f"Day           : {day_info}")

            if discount > 0:
                print(f"Discount (20%): \u20b9{discount:.2f}")
            else:
                print(f"Discount      : None")

            print(f"Price/Ticket  : \u20b9{price_per_ticket:.2f}")
            print(f"Tickets       : {tickets}")
            print(f"Total Amount  : \u20b9{total_amount:.2f}")

except ValueError:
    print("Error: Please enter valid numbers.")


# OUTPUT:
# PS C:\Users\...\Documents\Genai\Assignment2> python q09_ticket_pricing_system.py
# Enter age: 25
# Enter day of week: friday
# Enter number of tickets: 2

# === TICKET DETAILS ===
# Category      : Adult
# Base Price    : ₹300.00 per ticket
# Day           : Friday (Weekend Rate)
# Discount (20%): ₹60.00
# Price/Ticket  : ₹240.00
# Tickets       : 2
# Total Amount  : ₹480.00