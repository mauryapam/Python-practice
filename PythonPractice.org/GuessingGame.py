"""Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether 
they guessed too low, too high, or exactly right. (Hint: remember to use the user input lessons from the very first exercise)

Extras:

Keep the game going until the user types “exit”
Keep track of how many guesses the user has taken, and when the game ends, print this out."""

import random

num=random.randint(1,9)
guesses=0
userInput=0
# userInput= int(input("Guess a number between 1 and 9 :"))

while userInput!=num and userInput!='exit':
    userInput= int(input("Pick a number:"))
    if userInput==num:
        print("You guessed it right! ")
        guesses+=1
        print('Total guesses : ',guesses)

    elif userInput>num:
        print("Your guess is too high! ")
        guesses+=1

    else:
        print("Your guess is too low! ")
        guesses+=1

