# Question 10: Simple ATM Simulator
# Difficulty: Medium-Hard | Points: 7 | Time: 30 min
# Create an ATM simulation with initial balance = ₹10,000.
# Menu: 1. Check Balance 2. Deposit Money 3. Withdraw Money 4. Exit
# Rules:
# - Check sufficient balance before withdrawal
# - Minimum balance of ₹500 must remain at all times
# - Display transaction messages and updated balance after each transaction
# Sample Run:
# ATM SIMULATOR
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Exit
# Enter choice: 3
# Enter amount to withdraw: 2000
# Withdrawal successful!
# New balance: ₹8000
# Bonus (+3 points): Add transaction history

# --- Write your solution below this line ---

print("\n\n\n=== Q10: Simple ATM Simulator ===\n\n\n")

balance     = 10000.0
history     = []   # bonus: transaction log
MIN_BALANCE = 500.0

while True:
    print("\n=== ATM SIMULATOR ===")
    print("1. Check Balance")
    print("2. Deposit")
    print("3. Withdraw")
    print("4. Transaction History (BONUS)")
    print("5. Exit")

    try:
        choice = int(input("\nEnter choice: "))

        if choice == 1:
            print(f"Current Balance: ₹{balance:.2f}")

        elif choice == 2:
            amount = float(input("Enter deposit amount: ₹"))
            if amount <= 0:
                print("Amount must be greater than 0.")
            else:
                balance += amount
                history.append(f"Deposited  ₹{amount:.2f} | Balance: ₹{balance:.2f}")
                print(f"Deposit successful!")
                print(f"New balance: ₹{balance:.2f}")

        elif choice == 3:
            amount = float(input("Enter amount to withdraw: ₹"))
            if amount <= 0:
                print("Amount must be greater than 0.")
            elif amount > balance:
                print("Insufficient balance!")
            elif (balance - amount) < MIN_BALANCE:
                print(f"Cannot withdraw! Minimum balance of ₹{MIN_BALANCE:.2f} must remain.")
            else:
                balance -= amount
                history.append(f"Withdrawn  ₹{amount:.2f} | Balance: ₹{balance:.2f}")
                print(f"Withdrawal successful!")
                print(f"New balance: ₹{balance:.2f}")

        elif choice == 4:
            # BONUS: show transaction history
            if not history:
                print("No transactions yet.")
            else:
                print("\n=== TRANSACTION HISTORY ===")
                for i, entry in enumerate(history, 1):
                    print(f"  {i}. {entry}")

        elif choice == 5:
            print("Thank you for using the ATM. Goodbye!")
            break

        else:
            print("Invalid choice. Pick 1-5.")

    except ValueError:
        print("Please enter valid numbers only.")


# OUTPUT:

# PS C:\Users\...\Documents\Genai\Assignment2> python q10_simple_atm_simulator.py

# === ATM SIMULATOR ===
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Transaction History (BONUS)
# 5. Exit

# Enter choice: 1
# Current Balance: ₹10000.00

# === ATM SIMULATOR ===
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Transaction History (BONUS)
# 5. Exit

# Enter choice: 2
# Enter deposit amount: ₹5000
# Deposit successful!
# New balance: ₹15000.00

# === ATM SIMULATOR ===
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Transaction History (BONUS)
# 5. Exit

# Enter choice: 3
# Enter amount to withdraw: ₹20000
# Insufficient balance!

# === ATM SIMULATOR ===
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Transaction History (BONUS)
# 5. Exit

# Enter choice: 3
# Enter amount to withdraw: ₹8000
# Withdrawal successful!
# New balance: ₹7000.00

# === ATM SIMULATOR ===
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Transaction History (BONUS)
# 5. Exit

# Enter choice: 4

# === TRANSACTION HISTORY ===
#   1. Deposited  ₹5000.00 | Balance: ₹15000.00
#   2. Withdrawn  ₹8000.00 | Balance: ₹7000.00

# === ATM SIMULATOR ===
# 1. Check Balance
# 2. Deposit
# 3. Withdraw
# 4. Transaction History (BONUS)
# 5. Exit

# Enter choice: 5
# Thank you for using the ATM. Goodbye!
