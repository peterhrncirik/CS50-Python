import requests
import sys

# Check arguments validity
if len(sys.argv) == 1:
    sys.exit('Missing command-line argument')
elif sys.argv[1].isalpha():
    sys.exit('Command-line argument is not a number')
elif not float(sys.argv[1]):
    sys.exit()

# Numbers of bitcoins from user
bitcoins = float(sys.argv[1])

# Let's get request
try:
    r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    data = r.json()

    # Current BITCOIN/USD rate
    current_rate = data['bpi']['USD']['rate_float']

    # Calculate price
    price = current_rate * bitcoins

    print(f"${price:,.4f}")


except requests.RequestException:
    print('Something went wrong')
