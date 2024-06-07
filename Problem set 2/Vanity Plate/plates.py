def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if s.isalnum() == True and verify_length(s) == True:
        if s[0].isdigit() == True:
            return False
        elif s[-2].isdigit() == True and s[-1].isalpha() == True:
            return False            
        elif if_first_zero(s) == True:
            return False
        else:
            return True
        
    else:
        return False

def verify_length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False


    

def if_first_zero(s):
    list = []
    for i, c in enumerate(s):
        list.append(c)
        if c.isdigit() == True and c == '0':
            break
        else:
            continue
    
    if len(list) < len(s):
        return True
    else:
        return False
    
    
main()