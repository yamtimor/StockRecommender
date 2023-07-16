from StockLoader import StockLoader
import yaml

def main():
    """
    Main function
    """

    # Load the configuration file
    with open('config.yml', 'r') as f:
        config = yaml.safe_load(f)

    symbols = config['symbols']
    start_date = config['start_date']
    end_date = config['end_date']
    db_config = config['db_config']
    db_uri = f"mysql://{db_config['username']}:{db_config['password']}@{db_config['host']}:{db_config['port']}/{db_config['database']}"

    loader = StockLoader(symbols, start_date, end_date, db_uri)
    loader.load_data_to_mysql()

if __name__ == "__main__":
    main()