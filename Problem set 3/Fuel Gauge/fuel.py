def main():
    y = fuel_gauge()
    print(f'{y}')


def fuel_gauge():
    while True:
        try:
            prompt = input('Fraction: ').partition('/')
            num = int(prompt[0])/int(prompt[2])
            if 0.01 < num < 0.99:
                return f'{int((round(num,2))*100)}%'
            elif num <= 0.01:
                return 'E'
            elif 0.99 <= num <= 1:
                return 'F'
        except (ValueError, ZeroDivisionError):
            pass
        
            
        
main()