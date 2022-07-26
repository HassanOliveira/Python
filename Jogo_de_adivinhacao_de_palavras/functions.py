import random

name = input('What is your name?')

print('Good Luck', name, '!')

words = ['carro', 'livro', 'cachorro', 'teclado', 'predio', 'copo', 'agua']

print('Guess the word')

def draw(words):
    guesses = ''
    word = random.choice(words)
    i = 0
    chance = 8
    while i < 8:
        cont = 0
        for letter in word:
            if letter in guesses:
                print(letter)
            else:
                print('_')
                cont = cont + 1

        if cont == 0:
            print('You WIN!')
            print('The word is: ', word)
            break

        guess = input('Enter a letter: ')

        guesses += guess

        chance = chance - 1

        if chance == 0:
            print('You lose')
            break
        else:
            print(f'You have more {chance} chances')
        
        i = i + 1

draw(words)