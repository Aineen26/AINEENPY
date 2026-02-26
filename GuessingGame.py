

import random
print("=="*25)
print("Welcome to the Guessing Game!")
print("=="*25)
print("I'm thinking of a Number(1-100).")

hidden = random.randint(1, 100)
guess = 0
while guess != hidden:
    guess = int(input("Make a guess: "))
    if guess < hidden:
        print("Your guess is too low.")
    elif guess > hidden:
        print("Your guess is too high.")
print("you got it!!..Right guess")
