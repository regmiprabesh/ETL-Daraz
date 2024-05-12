#import libraries
from services.log_service import log_progress
from services.extract import extract
from services.transform import transform
from services.load import load_to_csv,load_to_db
import sqlite3

#Main Function
def main():
    url = 'https://raw.githubusercontent.com/regmiprabesh/daraz-scraper/main/data/product.jsonl'
    output_csv_path = 'output/products.csv'
    database_name = 'output/products.db'
    table_name = 'products'
    log_progress('Initiating ETL process')
    #Extract Data
    df = extract(url=url)
    #Transform Data
    df = transform(df, 'data/exchange_rate.csv')
    #Load Data
    load_to_csv(df, output_csv_path)
    with sqlite3.connect(database_name) as conn:
        load_to_db(df, conn, table_name)

if __name__ == "__main__":
    main()