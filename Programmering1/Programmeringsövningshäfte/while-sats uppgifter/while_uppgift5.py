import random
import sympy
random_number = random.randint(0,101)
print(random_number)

guess = ""
while guess != random_number:
    guess = int(input("Guess a number between 0 and 100: "))
    if guess == random_number:
        print(f"You got it! The number was {random_number}!")
        break
    elif guess > random_number:
        print("Guess Lower!")
    elif guess < random_number:
        print("Guess Higher!")
    if sympy.isprime(random_number):
        print("It's a prime number!")
    elif random_number % 2 == 0:
        print("It's a even number!")
    else:
        print("It's a odd number!")

