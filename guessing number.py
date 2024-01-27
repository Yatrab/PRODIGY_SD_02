import random

def guess_number_game():
    number_to_guess = random.randint(1, 100)
    attempts = 0
    guess = None

    while guess != number_to_guess:
        try:
            guess = int(input("Guess the number between 1 and 100: "))
            attempts += 1
        except ValueError:
            print("Invalid input. Please enter a number.")

        if guess < number_to_guess:
            print("Too low. Try again.")
        elif guess > number_to_guess:
            print("Too high. Try again.")
        else:
            print(f"Congratulations! You guessed the number in {attempts} attempts.")

if __name__ == "__main__":
    guess_number_game()