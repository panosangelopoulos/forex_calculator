import json, urllib2

url = 'http://api.fixer.io/latest'
currencies_values = urllib2.urlopen(url)
read_values = currencies_values.read()

JsonValues= json.loads(read_values)


usd = JsonValues['rates']['USD']

def find_latest_price(base, rate):
    url = 'http://api.fixer.io/latest?base='+ base +'&symbols=' + rate
    get_data_price = urllib2.urlopen(url)
    read_data_prices = get_data_price.read()
    json_data_prices = json.loads(read_data_prices)
    rate = json_data_prices['rates'][rate]

    print rate
    return rate

# base = 'GBP'
# rate = 'JPY'
# find_latest_price(base, rate)