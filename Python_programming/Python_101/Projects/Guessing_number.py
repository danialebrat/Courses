import random
import math

def play_game():
    print("Welcome to the Guessing Number Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"You have a maximum of {int(math.log(100, 2))+1} attempts.")

    secret_number = random.randint(1, 100)
    attempts = 0
    max_attempts = int(math.log(100, 2))+1

    while attempts < max_attempts:
        guess = input("Take a guess: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input! Please enter a valid number.")
            continue

        attempts += 1

        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts!")
            break

    if attempts == max_attempts:
        print(f"Oops! You reached the maximum number of attempts. The secret number was {secret_number}.")

    print("Thanks for playing!")

# Start the game
play_game()
