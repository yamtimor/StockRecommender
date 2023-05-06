import yfinance

class Stock(yf.Ticker):
    def __init__(self, symbol):
        super().__init__(symbol)

