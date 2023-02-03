import sys
import requests
if len(sys.argv) < 2:
    sys.exit("Missing command-line argument")
else:
    try:
        btc = float(sys.argv[1])
    except:
        sys.exit("Command-line argument is not a number")

response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
r = response.json()
btc_usd = r["bpi"]["USD"]["rate_float"]
usd = btc_usd * btc
print("${:,.4f}".format(usd))