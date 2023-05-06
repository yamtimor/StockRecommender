import yfinance as yf

class Stock(yf.Ticker):
    def __init__(self, symbol):
        super().__init__(symbol)

    @staticmethod
    def create_stocks(symbols):
        stocks = []
        for symbol in symbols:
            stock = Stock(symbol)
            stocks.append(stock)
        return stocks