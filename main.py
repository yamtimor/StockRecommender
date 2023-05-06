from StockLoader import StockLoader

symbols = ['AAPL', 'GOOG', 'MSFT']
start_date = '2023-01-01'
end_date = '2023-05-01'
db_uri = 'mysql://root:Yam232323@localhost:3306/stock_data'

loader = StockLoader(symbols, start_date, end_date, db_uri)
loader.load_data_to_mysql()