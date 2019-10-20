'''
starter code
'''

import random

random_number = random.randint(1,10) # numbers 1-10

# handle user guesses
# if the guess correct, tell them they won
# otherwise tell them if they are too high or too low

# BONUS - let them play again if they want!

'''
my code
'''

while True:
    guess = input("Choose a number between 1 and 10: ")
    guess = int(guess)
    if guess > random_number:
        print("Too high!")
    elif guess < random_number:
        print("Too low!")
    else:
        print("You guessed correctly!")
        play_again = input("Do you want to play again? (y/n) ")
        if play_again == 'y':
            random_number = random.randint(1,10)
            guess = None
        else:
            print("Thank you for playing!")
            break