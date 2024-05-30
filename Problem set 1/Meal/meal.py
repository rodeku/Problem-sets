def main():
    hour = input('What time is it? ')
    if hour.endswith('a.m.') or hour.endswith ('p.m.'):
        # 12 hour format
        if hour.endswith('a.m.'):
            hour_conv = convert(hour.strip('a.m.'))
        else:
            hour_conv = convert(hour.strip('p.m.')) + 12
    else:
        #24 hour format
        hour_conv = convert(hour)
    
    
    if 7 <= hour_conv <= 8:
        print('breakfast time')
    elif 12 <= hour_conv <= 13:
        print('lunch time')
    elif 18 <= hour_conv <= 19:
        print('dinner time')
    



def convert(time):
    partition = time.partition(':')
    h1 = float(partition[0])
    h2 = float(partition[2])/60
    return h1 + h2


if __name__ == "__main__":
    main()