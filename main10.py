#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                                     #says greetings
colors = ['red','orange','yellow','green','blue','violet','purple']     #array of options
play_again = ''                                         #play again set to empty 
best_count = sys.maxsize                                # the biggest number
while (play_again != 'n' and play_again != 'no'):       #while statement for if you want to play the game
    match_color = random.choice(colors)                 #makes a random color choice
    count = 0                                           #count set to zero
    color = ''                                          # player guess set to empty
    while (color != match_color):                       # while statement to see if you matched the color
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()                   #makes your guess all lower case
        count += 1                                      #plus one to the count everytime
        if (color == match_color):                      #checks if color matches
            print('Correct!')                           #says correct
        else:                                           #if its not correct
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count))      #try again and give the number of guesses
    print('\nYou guessed it in {0} tries!'.format(count))       #when you guess it correctly tells you how many times it took
    if (count < best_count):                                    #tells what you lowest number of quesses is
        print('This was your best guess so far!')               # tells you when it was your best
    best_count = count                                          #best guess nnumber is set to count 
    play_again = input("\nWould you like to play again? ").lower().strip()      #asks if you want to play the game again
print('Thanks for playing!')                                    #if you say no it thanks you for playing and closes the program