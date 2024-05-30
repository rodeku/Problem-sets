def main():
    expression = input('Expression: ').split()
    print(math(expression))


def math(x):
    num1 = float(x[0])
    num2 = float(x[2])
    
    match x[1]:
        case '/':
            return num1/num2
        case '*':
            return num1*num2
        case '+':
            return num1+num2
        case '-':
            return num1-num2
        
main()