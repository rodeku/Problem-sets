def main():
    answer = input('What is the Answer to the Great Question of Life, the Universe, and Everything? ').lower().strip()
    if universe(answer):
        print('Yes')
    else:
        print('No')

def universe(i):
    if i == '42':
        return True
    elif i == 'forty-two':
        return True
    elif i == 'forty two':
        return True
    else:
        return False

main()