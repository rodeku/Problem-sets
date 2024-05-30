def main():
    greeting = input('Greeting: ').lower().strip()
    y = bonus(greeting)
    print(y)


def bonus(x):
    if x.startswith('hello'):
        return '$0'
    elif x.startswith('h'):
        return '$20'
    else:
        return '$100'

main()
