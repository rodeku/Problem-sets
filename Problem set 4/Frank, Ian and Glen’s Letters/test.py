from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

def main():

    try:
        figlet_function('ñlkdsajf')
    except:
        print('not working')


def figlet_function(x):
    s = input()
    figlet.setFont(font=x)
    print(figlet.renderText(s))


main()