import random

def guessing_game():
    secret_number = random . randint(1, 10)

    attempts = 0
    print("welcome to the Guessing Game!")
    print("I've picked a number betwwen 1 and 100.can you guess it?")

    while True:
        try:
            guess = int(input("enter your guess:"))
            attempts += 1

            if guess<secret_number:
                print("too low! try again.")
            elif guess > secret_number:
                print("Too high! try again")
            else:
                print(f"congratulations!You guessed the number {secret_number} in {attempts} attempts.")
            break
        except  ValueError :
                print("please enter a valid number")

guessing_game()