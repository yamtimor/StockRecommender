import yfinance as yf

class Stock(yf.Ticker):
    def __init__(self, symbol):
        super().__init__(symbol)

stock = Stock("MSFT")
actions = stock.actions