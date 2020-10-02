import random

random_number = random.randint(0,101)
#print(random_number)

guess = ""
while guess != random_number:
    guess = int(input("Guess a number between 0 and 100: "))
    if guess == random_number:
        print(f"You got it! The number was {random_number}!")
        exit
    elif guess > random_number:
        print("Guess Lower!")
    elif guess < random_number:
        print("Guess Higher!")

