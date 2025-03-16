#	Implement a number guessing game where the user has limited attempts.

import random

def number_guessing_game():
    # User-defined range
    try:
        lower_bound = int(input("Enter the lower bound: "))
        upper_bound = int(input("Enter the upper bound: "))
        if lower_bound >= upper_bound:
            print(" Upper bound should be greater than the lower bound.")
            return

        # Random number within the user-defined range
        secret_number = random.randint(lower_bound, upper_bound)

        # User-defined number of attempts
        attempts = int(input("Enter the number of attempts you want: "))

        print(f"\n Welcome to the Number Guessing Game!")
        print(f"Guess the number between {lower_bound} and {upper_bound}. You have {attempts} attempts.\n")

        # Game loop
        while attempts > 0:
            try:
                guess = int(input("Enter your guess: "))

                if guess < lower_bound or guess > upper_bound:
                    print(f" Please guess a number between {lower_bound} and {upper_bound}.")
                    continue

                if guess == secret_number:
                    print(f" Congratulations! You guessed the correct number: {secret_number}")
                    break
                elif guess < secret_number:
                    print(" Too low! Try again.")
                else:
                    print(" Too high! Try again.")

                attempts -= 1
                print(f"Attempts remaining: {attempts}")

            except ValueError:
                print(" Invalid input! Please enter a valid number.")

        # Out of attempts
        if attempts == 0:
            print(f" Out of attempts! The correct number was {secret_number}.")

    except ValueError:
        print(" Invalid input! Please enter valid numbers.")

# Start the game
number_guessing_game()
