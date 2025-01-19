import random

def guessing_game():
    levels = {"easy": 10, "medium": 7, "hard": 5}
    print("Choose difficulty level: easy, medium, or hard")
    level = input("Enter level: ").lower()
    attempts = levels.get(level, 7)
    number_to_guess = random.randint(1, 100)

    print(f"You have {attempts} attempts to guess the number between 1 and 100.")

    while attempts > 0:
        try:
            guess = int(input("Enter your guess: "))
            if guess < 1 or guess > 100:
                print("Please guess a number between 1 and 100.")
            elif guess < number_to_guess:
                attempts -= 1
                if number_to_guess - guess <= 10:
                    print(f"Too low! You're very close. You have {attempts} attempts left.")
                else:
                    print(f"Too low! You have {attempts} attempts left.")
            elif guess > number_to_guess:
                attempts -= 1
                if guess - number_to_guess <= 10:
                    print(f"Too high! You're very close. You have {attempts} attempts left.")
                else:
                    print(f"Too high! You have {attempts} attempts left.")
            else:
                print("Congratulations! You guessed it right.")
                break

            if attempts == 0:
                print(f"Game over! The correct number was {number_to_guess}.")
        except ValueError:
            print("Invalid input. Please enter an integer.")

guessing_game()
