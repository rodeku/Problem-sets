
s = input("Plate: ")



def if_first_zero(s):
    list = []
    for i, c in enumerate(s):
        list.append(c)
        if c.isdigit() == True and c == '0':
            break
        else:
            continue
    
    print(list)

    if len(list) < len(s):
        return True
    else:
        return False

print(if_first_zero(s))