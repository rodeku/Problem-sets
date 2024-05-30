def main():
    filename = input('File name: ').lower().strip()
    print(filetype(filename))



def filetype(x):
    if x.endswith('.jpg') or x.endswith('.jpeg'):
        return 'image/jpeg'
    elif x.endswith('.gif'):
        return 'image/gif'
    elif x.endswith('.png'):
        return 'image/png'
    elif x.endswith('.pdf'):
        return 'application/pdf'
    elif x.endswith('.txt'):
        return 'text/plain'
    elif x.endswith('.zip'):
        return 'application/zip'
    else:
        return 'application/octet-stream'


main()
