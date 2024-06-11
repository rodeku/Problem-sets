def main():
    x = grocery()    
    for i,c in enumerate(x):
        print(f'{x[c]} {c}')


def grocery():
    grocery_list = {}
    counts = 0

    while True:
        try:
            prompt = input().upper()
            if prompt in grocery_list.keys():
                counts = grocery_list.get(prompt) + 1
                grocery_list.update({prompt:counts})
            else:
                grocery_list[prompt] = 1
        
        except EOFError:
            sorted_dict = {key: grocery_list[key] for key in sorted(grocery_list)}
            return sorted_dict
        except KeyError:
            pass





main()