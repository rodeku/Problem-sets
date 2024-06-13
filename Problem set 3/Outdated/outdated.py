# outdated.py

def main():
    x = outdated()
    print(f"{x[2]}-{x[0]:02}-{x[1]:02}")



def outdated():
    while True:
        try:
            date = input('Date: ')
            if '/' in date and int(date.split('/')[0]) <= 12 and int(date.split('/')[1]) <= 31:
                date = date.split('/')
                list = []
                for i in range(len(date)):
                    list.append(int(date[i]))
                date = list
                return date
            elif ',' in date and int(date.split(' ')[1].rstrip(',')) <= 12:
                date = date.split(' ')
                month_number = months.index(date[0]) + 1
                day = int(date[1].rstrip(','))
                date = [month_number, day, date[2]]
                return date
        
        except (ValueError):
            pass
    


months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]


main()