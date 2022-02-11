import art
import random

answer = random.randint(1, 100)
attempts = 0
is_Playing = True

print(art.logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")

if difficulty == "easy":
    attempts = 10
elif difficulty == "hard":
    attempts = 5

while is_Playing:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess > answer:
        print("Too High.")
        print("Guess again.")
        attempts -= 1
    elif guess < answer:
        print("Too Low.")
        print("Guess again.")
        attempts -= 1
    elif guess == answer:
        print(f"You got it! The answer was {answer}.")
        is_Playing = False

    if attempts == 0:
        is_Playing = False
        print("You've run out of guesses, you lose.")
