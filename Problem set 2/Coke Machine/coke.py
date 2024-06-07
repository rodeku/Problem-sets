def main():
    amount_due = 50

    while 0 < amount_due:
        print(f'Amount Due: {amount_due}')
        amount_in = int(input('Insert Coin: '))

        if verify_denomination(amount_in) == True:
            amount_due = amount_due - amount_in
        else:
            continue
        
    if amount_due == 0:
        print('Change Owed: 0')
    else:
        print(f'Change Owed: {-amount_due}')

def verify_denomination(n):
    if n == 25 or n == 10 or n == 5:
        return True
    else:
        return False

main()