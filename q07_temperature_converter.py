# Question 7: Temperature Converter
# Difficulty: Medium | Points: 4 | Time: 25 min
# Create a temperature converter with a menu-based system supporting:
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Celsius to Kelvin
# 4. Kelvin to Celsius
# 5. Fahrenheit to Kelvin
# 6. Kelvin to Fahrenheit
# 7. Exit
# Formulas:
# - C to F: (C × 9/5) + 32
# - F to C: (F - 32) × 5/9
# - C to K: C + 273.15
# - K to C: K - 273.15
# - F to K: (F - 32) × 5/9 + 273.15
# - K to F: (K - 273.15) × 9/5 + 32

# --- Write your solution below this line ---

print("\n\n\n=== Q07: Temperature Converter ===\n\n\n")

# Conversion functions
def celsius_to_fahrenheit(c):
    return (c * 9/5) + 32

def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_kelvin(c):
    return c + 273.15

def kelvin_to_celsius(k):
    return k - 273.15

def fahrenheit_to_kelvin(f):
    return (f - 32) * 5/9 + 273.15

def kelvin_to_fahrenheit(k):
    return (k - 273.15) * 9/5 + 32

# Keep showing the menu until user exits
while True:
    print("\n=== TEMPERATURE CONVERTER ===")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Kelvin")
    print("6. Kelvin to Fahrenheit")
    print("7. Exit")

    try:
        choice = int(input("Enter choice: "))

        if choice == 7:
            print("Goodbye!")
            break

        elif choice in [1, 2, 3, 4, 5, 6]:
            temp = float(input("Enter temperature: "))

            # Edge case: Kelvin cannot be negative
            if choice in [4, 6] and temp < 0:
                print("Error: Kelvin temperature cannot be negative.")
                continue

            if choice == 1:
                print(f"{temp}°C = {celsius_to_fahrenheit(temp):.2f}°F")
            elif choice == 2:
                print(f"{temp}°F = {fahrenheit_to_celsius(temp):.2f}°C")
            elif choice == 3:
                print(f"{temp}°C = {celsius_to_kelvin(temp):.2f}K")
            elif choice == 4:
                print(f"{temp}K = {kelvin_to_celsius(temp):.2f}°C")
            elif choice == 5:
                print(f"{temp}°F = {fahrenheit_to_kelvin(temp):.2f}K")
            elif choice == 6:
                print(f"{temp}K = {kelvin_to_fahrenheit(temp):.2f}°F")

        else:
            print("Invalid choice. Please enter a number between 1 and 7.")

    except ValueError:
        print("Error: Please enter valid numbers.")


# OUTPUT:

# PS C:\Users\...\Documents\Genai\Assignment2> python q07_temperature_converter.py

# === TEMPERATURE CONVERTER ===
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Celsius to Kelvin
# 4. Kelvin to Celsius
# 5. Fahrenheit to Kelvin
# 6. Kelvin to Fahrenheit
# 7. Exit
# Enter choice: 1
# Enter temperature: 32
# 32.0°C = 89.60°F

# === TEMPERATURE CONVERTER ===
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Celsius to Kelvin
# 4. Kelvin to Celsius
# 5. Fahrenheit to Kelvin
# 6. Kelvin to Fahrenheit
# 7. Exit
# Enter choice: 2
# Enter temperature: 32
# 32.0°F = 0.00°C

# === TEMPERATURE CONVERTER ===
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Celsius to Kelvin
# 4. Kelvin to Celsius
# 5. Fahrenheit to Kelvin
# 6. Kelvin to Fahrenheit
# 7. Exit
# Enter choice: 3
# Enter temperature: 32
# 32.0°C = 305.15K

# === TEMPERATURE CONVERTER ===
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Celsius to Kelvin
# 4. Kelvin to Celsius
# 5. Fahrenheit to Kelvin
# 6. Kelvin to Fahrenheit
# 7. Exit
# Enter choice: 4
# Enter temperature: 32
# 32.0K = -241.15°C

# === TEMPERATURE CONVERTER ===
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Celsius to Kelvin
# 4. Kelvin to Celsius
# 5. Fahrenheit to Kelvin
# 6. Kelvin to Fahrenheit
# 7. Exit
# Enter choice: 5
# Enter temperature: 32
# 32.0°F = 273.15K

# === TEMPERATURE CONVERTER ===
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Celsius to Kelvin
# 4. Kelvin to Celsius
# 5. Fahrenheit to Kelvin
# 6. Kelvin to Fahrenheit
# 7. Exit
# Enter choice: 6
# Enter temperature: 32
# 32.0K = -402.07°F

# === TEMPERATURE CONVERTER ===
# 1. Celsius to Fahrenheit
# 2. Fahrenheit to Celsius
# 3. Celsius to Kelvin
# 4. Kelvin to Celsius
# 5. Fahrenheit to Kelvin
# 6. Kelvin to Fahrenheit
# 7. Exit
# Enter choice: 7
# Goodbye!
