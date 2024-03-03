# Starter file for TM112 2023J TMA03 Q2


"""
This flashcard program allows the user to ask for a word_list entry.
In response, the program randomly picks an entry from all word_list
entries. It shows the entry. After the user presses return, the
program shows the definition of that particular entry.
The user can repeatedly ask for an entry and also
has the option to quit the program instead of seeing
another entry.
"""

from random import *

# IMPORTANT
# Q2 (a)(iii) Make changes only to
# -- the docstring for the program as a whole;
# -- the docstring of the show_flashcard() function;
# -- the body of the show_flashcard() function.


def show_flashcard():
    """ Show the user a random key and ask them
        to define it. Show the definition
        when the user presses return.    
    """
    random_key = choice(list(proverbs_dictionary))
    print('Define: ', random_key)
    input('Press return to see the definition')
    print(proverbs_dictionary[random_key])

## Set up the proverbs_dictionary
proverbs_dictionary = {"A rolling stone gathers no":"moss",
               "More haste less":"speed",
               "Curiosity killed the":"cat",
               "Rome wasn't built in a":"day",
               "It’s no use crying over spilt":"milk",
               "Many hands make light":"work",
               "A stitch in time saves":"nine",
               "The early bird catches the ":"worm",
               "Look before you ":"leap",
               "Where there's a will there's a":"way",
               "Least said soonest":"mended",
               "A fool and his money are soon":"parted",
               "Too many cooks spoil the":"broth",
               "Fools rush in where angels fear to":"tread"
              }

# The interactive loop

exit = False
while not exit:
    user_input = input('Enter s to show a flashcard and q to quit: ')
    if user_input == 'q':
        exit = True
    elif user_input == 's':
        show_flashcard()
    else:
        print('You need to enter either q or s.')              
