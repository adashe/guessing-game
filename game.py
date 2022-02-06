"""A number-guessing game."""

# Put your code here

import random

user_name = input("What's your name? ")

print(f'Hello {user_name}, welcome to our guessing game.')

random_number = random.randint(1, 101)

print('Shhh, do not tell anyone, but the number is ' + str(random_number) + '.')

user_guess = int((input("Guess a number between 1 and 100: ")))

print('Your guess is ' + str(user_guess))

while True:
    if user_guess == random_number:
        print('Yey! You guessed correct!')
        break
    elif user_guess > random_number:
        print("You were above the number!")
        user_guess = int((input("Please guess again: ")))
    elif user_guess < random_number:
        print("You were below the number!")
        user_guess = int((input("Please guess again: ")))
    else:
        print("Invalid input")
