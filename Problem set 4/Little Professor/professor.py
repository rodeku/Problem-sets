import random


def main():
    level = get_level()

    count = 0
    mistakes = 0

    while count < 10:
        strikes = 0
        count = count + 1
        int1 = generate_integer(level)
        int2 = generate_integer(level)
        sum = int1+int2
        
        

        while strikes < 3:
            try:
                print(f'{int1} + {int2} = ', end='')
                prompt = int(input())
                if prompt == sum:
                    break
                else:
                    strikes = strikes + 1
                    print('EEE',strikes)
                    continue

            except ValueError:
                strikes = strikes + 1
                print('EEE',strikes)
                continue
        else:
            print(f'{int1} + {int2} = {sum}')
            mistakes = mistakes + 1
            print(f'Current mistakes: {mistakes}')
    
        score = 10 - mistakes
    print(f'Score: {score}')

        


def get_level():
    while True:
        prompt = input('Level: ')
        if prompt.isdigit():
            prompt = int(prompt)
            if prompt == 1 or prompt == 2 or prompt == 3:
                return prompt
            else:
                continue
        else:
            continue


def generate_integer(level):
    if level == 1:
        integer = random.randint(0,9)
    elif level == 2:
        integer = random.randint(10,99)
    elif level == 3:
        integer = random.randint(100,999)
    else:
        raise ValueError
    return integer


if __name__ == "__main__":
    main()