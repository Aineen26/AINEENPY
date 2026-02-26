
import random
secret_number = random.randint(1,100)
tries = 0
max_attempts = 3
guess = 0
print(f"I'm thinking of a number between (1-100).You have {max_attempts} attempts!")
while tries < max_attempts:
    guess = int(input("Guess the correct number: "))
    tries += 1
    if guess == secret_number:
        print("Correct!")
        break
    elif guess < secret_number:
        print("Too Low...Try again!")
    else:
        print("Too High...Try again!")
if guess != secret_number:
    print("=="*40)
    print(f"You are guessing wrong and you have failed 3 attempts.")
    print(f"The number I picked was: {secret_number}")
