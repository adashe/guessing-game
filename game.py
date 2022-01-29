"""A number-guessing game."""

# Put your code here

import random



user_name = input("What's your name?")
print(f'Hello {user_name}, welcome to our guessing game')

random_number = random.randint(1, 101)

print('Do not tell anyone, but the number is ' + str(random_number))

user_guess = (input("Guess a number between 1 and 100."))

print('Your guess is ' + str(user_guess))

