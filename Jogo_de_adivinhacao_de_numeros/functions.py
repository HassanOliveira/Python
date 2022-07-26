from random import randint
from math import log2

def number_compiler():
    inferior_limit = int(input('Enter a number for the lower limit: '))
    upper_limit = int(input('Enter a number for the upper limit: '))
    drawn_number = randint(inferior_limit, upper_limit)
    minimum_number_of_guessing = int(log2(upper_limit - inferior_limit) + 1)
    return(drawn_number, minimum_number_of_guessing)


def verification(drawn_number, minimum_number_of_guessing):
    i = 1
    number = int(input(f'{i}° guess - Enter a number: '))
    while (number != drawn_number and i != minimum_number_of_guessing):
        i = i + 1
        if (number > drawn_number):
            print('Try again! You guessed it too high')
            number = int(input(f'{i}° guess - Enter a number: '))
        elif (number < drawn_number):
            print('Try again! You guessed it too small')
            number = int(input(f'{i}° guess - Enter a number: '))
    if (number == drawn_number and i <= minimum_number_of_guessing):
            print('\nCongratulations!\n')
    elif (number != drawn_number and i >= minimum_number_of_guessing):
            print('\nBetter luck next time!\n')