def main():
    user_input = input('Input: ')
    output = vocal_strip(user_input)
    print(f'Output: {output}')

def vocal_strip (s):
    vocals = ['A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u']
    string_copy = []

    for i, c in enumerate(s):
        if c in vocals:
            continue
        elif c == ' ':
            string_copy.append(' ')
        else:
            string_copy.append(c)
    
    sep = ''
    return sep.join(string_copy)
    

main()