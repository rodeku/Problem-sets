def main():
    camel_case = input('camelCase: ')
    
    is_upper = False

    for c in camel_case:
        if c.isupper():
            is_upper = True
    
    if is_upper == True:
        snake_case = convert_to_snake(camel_case)
        print(f'snake_case: {snake_case}')
    else:
        print(f'snake_case: {camel_case}')


def lower_case(s):
    return s.lower()
 

def convert_to_snake(s):
    list = []
    position = []
    letters = []
    list_of_words = []
    for i, c in enumerate(s):
        letters.append(c)
        if c.isupper() == True:
            list.append(c)
            position.append(i)
        else:
            continue

    
   # print(new_word1)
    new_list = []
    n = 0
    for i in range(len(position)):
            new_word = s[n:position[i]]
            new_list.append(new_word)
            n = position[i]
                
    new_word = s[position[i]:]
    new_list.append(new_word)
    new_list = new_list

    sep = '_'
    return lower_case(sep.join(new_list))

main()