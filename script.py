import alpaca_trade_api as tradeapi

API_KEY = 'PKBGDBT7O9R29NVQEXX5'
SECRET_KEY = '51mqZFZPIy4nhwguJn4sG2ZPLkJseJ2KdnWKfBaB'
BASE_URL = 'https://paper-api.alpaca.markets'

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

account = api.get_account()

# Corrected code
aapl_bars = api.get_barset('AAPL', 'day', limit=5)
aapl = aapl_bars['AAPL']

# Printing the barset
for bar in aapl:
    print(bar.t, bar.o, bar.h, bar.l, bar.c, bar.v)
