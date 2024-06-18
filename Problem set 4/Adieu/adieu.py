import inflect
p = inflect.engine()

def main():
    
    print(f'\nAdieu, adieu, to {adieu()}')

def adieu():
    mylist = []
    while True:
        try:
            prompt = input('Name: ')
            mylist.append(prompt)
        except EOFError:
            name_list = p.join(mylist)
            return name_list
        

    
main()