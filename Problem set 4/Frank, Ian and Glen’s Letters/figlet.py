from pyfiglet import Figlet
import sys
import random

figlet = Figlet()
def main():
    

    if len(sys.argv) == 1: # print text in random font
        font_list = figlet.getFonts()
        f = random.choice(font_list)
        figlet_function(f)
    elif sys.argv[2] not in figlet.getFonts():
        sys.exit('Invalid usage')

    elif len(sys.argv) == 3 and sys.argv[1] == '-f': # print text in provided font
        f = sys.argv[2]
        figlet_function(f)
    elif len(sys.argv) == 3 and sys.argv[1] == '--font':
        f = sys.argv[2]
        figlet_function(f)
    else:
        sys.exit('Invalid usage')


def figlet_function(x):
    s = input()
    figlet.setFont(font=x)
    print(figlet.renderText(s))


main()