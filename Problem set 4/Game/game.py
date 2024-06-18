# https://cs50.harvard.edu/python/2022/psets/4/game/

import random
import sys

def main():
    guess()


def guess():

    prompt = positive_input('Input: ')
    number_to_guess = random.randint(1,prompt)

    while True:
        guess = positive_input('Guess: ')

        if guess < number_to_guess:
            print('Too small!')
            continue
        elif number_to_guess < guess:
            print('Too large!')
            continue
        else:
            sys.exit('Just right!')


def positive_input(x):
    while True:
        prompt = input(f'{x}')
        if prompt.isdigit():
            prompt = int(prompt)
            if 0 < prompt:
                return prompt
            else:
                continue
        else:
            continue
main()