import yfinance as yf

class Stock(yf.Ticker):
    """
    Stock class
        Attributes:
            symbol (str): stock symbol
    """

    def __init__(self, symbol):
        super().__init__(symbol)
        self.symbol = symbol

    def get_history_metadata(self, start_date, end_date):
        history_metadata = super().history(start=start_date, end=end_date, interval='1d', actions=False)
        return history_metadata

    @staticmethod
    def create_stocks(symbols):
        stocks = []
        for symbol in symbols:
            stock = Stock(symbol)
            stocks.append(stock)
        return stocks
