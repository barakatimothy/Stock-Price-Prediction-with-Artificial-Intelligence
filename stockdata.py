import yfinance as yf

# Specify the tickers
tickers = ['AAPL']

# Fetch data
data = yf.download(tickers, start="2022-01-01", end="2022-12-31")

# Save to CSV
data.to_csv('stock_data.csv')

print("Data saved to stock_data.csv")
