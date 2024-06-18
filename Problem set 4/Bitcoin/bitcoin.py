import requests
import sys

def main():
    if len(sys.argv) <= 1:
        sys.exit('Missing command-line argument')
    else:
        try:
            amount_of_bitcoin = float(sys.argv[1])
        except ValueError:
            sys.exit('Command-line argument is not a number')

    price = get_price_btc()
    amount = price*amount_of_bitcoin
    print(f"${amount:,.4f}")


def get_price_btc():
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        return r.json()['bpi']['USD']['rate_float']
    except requests.RequestException:
        pass

main()