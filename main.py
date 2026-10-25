
import random


def get_random_number():
    """Generate a secret number between 1 and 99."""
    return random.randrange(1, 100)


def give_hint(number, guess):
    """Return a hint based on the difference between the guess and number."""
    if guess == number:
        return "Right"
    elif abs(number - guess) <= 10:
        return "Hot"
    else:
        return "Cold"


def run_guess():
    """Run the number guessing game until the user wins."""
    secret_number = get_random_number()

    print("Welcome to the Number Guessing Game!")
    print("Guess a number between 1 and 99.")

    while True:
        try:
            guess = int(input("Enter your guess: "))

            if not 1 <= guess <= 99:
                print("Please enter a number between 1 and 99.")
                continue

        except ValueError:
            print("Invalid input. Please enter a whole number.")
            continue

        hint = give_hint(secret_number, guess)

        if hint == "Right":
            print("You guessed it right!!")
            break
        else:
            print(hint)


if __name__ == "__main__":
    run_guess()
