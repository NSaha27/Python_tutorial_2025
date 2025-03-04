# Guess a number between 1 and 10
import random
import math

print("-: Number Guessing Game :-")

rand_number = math.floor(random.random() * 10)
NUM_OF_CHANCES = 3

counter = 1

status = "Alash! you didn't guess the number!"

print("(you have only 3 chances to guess the correct number)")
while counter <= NUM_OF_CHANCES:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess < 1 or guess > 10:
        guess = int(input("Select a valid number between 1 and 10: "))
    if guess < 1 or guess > 10:
        guess = int(
            input("This is the last chance, select a valid number between 1 and 10: "))
    if guess < 1 or guess > 10:
        status = "you crossed the maximum limit of valid chances!"
        break
    if guess == rand_number:
        status = "Hurray! you guessed the number accurately"
        break
    else:
        print(
            f"{"too large" if guess > rand_number else "too small"}, guess correctly!")
        print(f"you have only {NUM_OF_CHANCES - counter} chances left!")
        print()
    counter += 1

print(status)
