#print("\U0001F642") #Slightly smiling face 🙂
#print("\U0001F641") #Slightly frowning face 🙁

def convert(string):
    return string.replace(':)','\U0001F642').replace(':(','\U0001F641')

def main():
    x = input('Please write your phrase: ')
    variable = convert(x)
    print(variable)

main()
