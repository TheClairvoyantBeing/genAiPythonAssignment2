# Question 16: Number Guessing Game
# Difficulty: Hard | Points: 7 | Time: 35 min
# Create a number guessing game where the computer picks a random number between 1-100
# and the user gets 7 attempts.
# Rules:
# 1. After each guess, show if guess is too high or too low and attempts remaining
# 2. If correct: congratulate and show attempts used
# 3. If failed: reveal the number
# 4. Ask to play again
# Bonus (+3 points): Track best score (minimum attempts) and give hints when close (within 5).

# --- Write your solution below this line ---

print("\n\n\n=== Q16: Number Guessing Game ===\n\n\n")

attempts     = 7
best_score   = None
games_played = 0
games_won    = 0

while True:
    # Generating random number using memory address of a temp object
    secret = id(object()) % 100 + 1
    games_played += 1

    print(f"\n=== GAME #{games_played} ===")
    print(f"Got a number 1-100, u got {attempts} tries!")
    if best_score:
        print(f"Best score so far: {best_score} attempts")

    won = False
    for i in range(1, attempts+1):
        try:
            guess = int(input(f"\nAttempt {i}/{attempts}: "))

            if guess == secret:
                print(f"Correct!! got it in {i} tries 🎉")
                won = True
                games_won += 1

                # update best score if this is better (bonus)
                if best_score is None or i < best_score:
                    best_score = i
                    print(f"New best score: {best_score} attempts! 🏆")
                break
            else:
                # close hint within 5 (bonus)
                if abs(guess - secret) <= 5:
                    print("So close omg!!")

                if guess < secret:
                    print(f"Too low! ({attempts-i} tries left)")
                else:
                    print(f"Too high! ({attempts-i} tries left)")

        except ValueError:
            print("enter a number ffs")

    if not won:
        print(f"\nBetter luck next time.. it was {secret}")

    # show stats and ask to play again
    print(f"\nStats: {games_won} wins / {games_played} games played")
    if best_score:
        print(f"Best score: {best_score} attempts")

    again = input("\nPlay again? (y/n): ").strip().lower()
    if again != "y":
        print("thanks for playing!")
        break


# OUTPUT:
# PS C:\Users\...\Documents\Genai\Assignment2> python q16_number_guessing_game.py

# === GAME #1 ===
# Got a number 1-100, u got 7 tries!

# Attempt 1/7: 50
# Too high! (6 tries left)

# Attempt 2/7: 20
# Too low! (5 tries left)

# Attempt 3/7: 28
# Too low! (4 tries left)

# Attempt 4/7: 40
# So close omg!!
# Too high! (3 tries left)

# Attempt 5/7: 35
# So close omg!!
# Too low! (2 tries left)

# Attempt 6/7: 37
# Correct!! got it in 6 tries 🎉
# New best score: 6 attempts! 🏆

# Stats: 1 wins / 1 games played
# Best score: 6 attempts

# Play again? (y/n): y

# === GAME #2 ===
# Got a number 1-100, u got 7 tries!
# Best score so far: 6 attempts

# Attempt 1/7: 25
# Too low! (6 tries left)

# Attempt 2/7: 75
# Too high! (5 tries left)

# Attempt 3/7: 50
# Too high! (4 tries left)

# Attempt 4/7: 40
# So close omg!!
# Too high! (3 tries left)

# Attempt 5/7: 38
# So close omg!!
# Too high! (2 tries left)

# Attempt 6/7: 34
# So close omg!!
# Too low! (1 tries left)

# Attempt 7/7: 35
# So close omg!!
# Too low! (0 tries left)

# Better luck next time.. it was 37

# Stats: 1 wins / 2 games played
# Best score: 6 attempts

# Play again? (y/n): y

# === GAME #3 ===
# Got a number 1-100, u got 7 tries!
# Best score so far: 6 attempts

# Attempt 1/7: 50
# Too high! (6 tries left)

# Attempt 2/7: 30
# Too low! (5 tries left)

# Attempt 3/7: 40
# So close omg!!
# Too high! (4 tries left)

# Attempt 4/7: 35
# So close omg!!
# Too low! (3 tries left)

# Attempt 5/7: 37
# Correct!! got it in 5 tries 🎉
# New best score: 5 attempts! 🏆

# Stats: 2 wins / 3 games played
# Best score: 5 attempts

# Play again? (y/n): n
# thanks for playing!