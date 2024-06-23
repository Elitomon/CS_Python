# High/low guessing game
# Eli Monroe
# Nov 13 2021

import random

game = ('y')

while game != ('n' or 'N'):
    maxValue = int(input('What should the maximum number for this game be? '))
    myNumber =  int(random.randint(1, maxValue))
    print (' ')
    guess = int(input('Guess my number: '))

    while guess != myNumber:

        if guess > myNumber:
            print ('Your guess is too high.')
            print (' ')
            guess = int(input('Guess my number: '))

        else:
            print ('Your guess is too low. ')
            print (' ')
            guess = int(input('Guess my number: '))
        

    print ('You guessed my number!')
    print (' ')
    game = input('Do you wish to play again? (Y/N): ')
    print (' ')

print ('Thank you for playing!')
    
    
