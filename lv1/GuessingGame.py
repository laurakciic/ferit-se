# https://www.practicepython.org/exercise/2014/04/02/09-guessing-game-one.html

# Generate a random number between 1 and 9 (including 1 and 9). 
# Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right.

import random
randomNum =  random.randint(1,9)
guess = (int(input("Try to guess the generated number in range [1,9]: ")))

while (guess != randomNum):
    if guess == randomNum:
        print("You guessed right!")
        break
    elif guess > randomNum:
        print("Your guess is higher than the generated number")
        guess = (int(input("Try to guess the generated number in range [1,9]: ")))
    else:
         print("Your guess is lower than the generated number")
         guess = (int(input("Try to guess the generated number in range [1,9]: ")))
print("You guessed right!")
