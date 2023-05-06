from Stock import Stock
from sqlalchemy import create_engine
import pandas as pd

class StockLoader:
    def __init__(self, symbols, start_date, end_date, db_uri):
        self.symbols = symbols
        self.start_date = start_date
        self.end_date = end_date
        self.db_uri = db_uri

    def load_data_to_mysql(self):
        # Load data from Yahoo Finance API
        stocks = Stock.create_stocks(self.symbols)
        history_metadata_data = []
        for stock in stocks:
            history_metadata_data.append(stock.get_history_metadata(self.start_date, self.end_date))

        # Combine data into a single DataFrame
        history_metadata_df = pd.concat(history_metadata_data)

        # Load data into MySQL database using SQLAlchemy
        engine = create_engine(self.db_uri)
        history_metadata_df.to_sql('history_metadata', con=engine, if_exists='replace')