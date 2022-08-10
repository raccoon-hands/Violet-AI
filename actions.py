#!/usr/bin/env python3
import re
from dictionaries import *
from random import *

def flashcard(subject):
    """
    Show the user a random key and ask them
    to define it. Show the definition
    when the user presses return.    
    """
    print("Let's look at some flashcards! Let me know when you want to stop.")
    a_dict = subject
    exit = False

    while not exit:
        random_key = choice(list(a_dict))
        print('\nDefine: ', random_key)
        exit = input('\nPress return to see the definition:')
        print('\nThe definition is: ' + a_dict[random_key])
        exit = input('\nPress return for a new flashcard:')

    print("\nAlright, I've put the flashcards away.")


def lookup(subject):
    """
    Ask the user for a term, then look
    it up as a key in the chosen dictionary, and return
    its value.
    """
    a_dict = subject
    new_dict = {}

    for key in a_dict:
        newkey = re.sub('[^A-Za-z0-9]+', '', key).lower()
        new_dict[newkey] = a_dict[key]
                        
    print("Type 'end' at any time to stop looking in the dictionary.")
    
    exit = False
    
    while not exit:
        a_key = input('\nPlease type the term that you would like me to look up:').lower()
        a_key = re.sub('[^A-Za-z0-9]+', '', a_key)

        if a_key in new_dict:
            print(new_dict.get(a_key))

        elif a_key == 'end':
            print("\nOkay, I've put away the dictionary.")
            exit = True

        else:
            print("I don't seem to know that term. Please check your spelling and try again.")
        
    
    


