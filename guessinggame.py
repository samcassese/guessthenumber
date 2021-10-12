import random

num = random.randint(1,1000)

checker = 0

while checker == 0:
    guess = float(input("Guess a number from 1-1000: "))
    if guess > num:
            print("Lower!")
    elif guess < num:
            print("Higher!")
    else:
                print("Correct!")
                checker += 1 