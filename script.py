import alpaca_trade_api as tradeapi
import time

# Replace these with your Alpaca API credentials
API_KEY = 'PKBGDBT7O9R29NVQEXX5'
SECRET_KEY = '51mqZFZPIy4nhwguJn4sG2ZPLkJseJ2KdnWKfBaB'
BASE_URL = 'https://paper-api.alpaca.markets'   # For paper trading

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')
def buy(symbol, qty):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='buy',
        type='market',
        time_in_force='gtc'
    )

def sell(symbol, qty):
    api.submit_order(
        symbol=symbol,
        qty=qty,
        side='sell',
        type='market',
        time_in_force='gtc'
    )

def get_current_price(symbol):
    last_trade = api.get_latest_trade(symbol)
    return float(last_trade.price)

def main(symbol, qty):
    while True:
        current_price = get_current_price(symbol)
        open_price = api.get_latest_trade(symbol).price
        
        if current_price > open_price:
            buy(symbol, qty)
            print(f"Bought {qty} shares of {symbol} at {current_price}")

        elif current_price < open_price - 30:  # Place stop loss 30 points below opening price
            sell(symbol, qty)
            print(f"Sold {qty} shares of {symbol} at {current_price}")

        time.sleep(60)  # Check every minute

if __name__ == "__main__":
    symbol = input("Enter the stock symbol: ")
    qty = int(input("Enter the quantity to trade: "))
    main(symbol, qty)
