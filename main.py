#import libraries
from services.log_service import log_progress
from services.extract import extract
from services.transform import transform
from services.validate import validation
from services.load import load_to_csv,load_to_db
import psycopg2
from dotenv import load_dotenv
import os

#Main Function
def main():
    #Path for daraz scraped data and output csv file
    url = 'https://raw.githubusercontent.com/regmiprabesh/daraz-scraper/main/data/product.jsonl'
    output_csv_path = 'output/products.csv'
    log_progress('Initiating ETL process')
    #Extract Data
    df = extract(url=url)
    #Transform Data
    df = transform(df, 'data/exchange_rate.csv')
    #Validate Data
    if validation(df):
        #Load Data To CSV
        load_to_csv(df, output_csv_path)
        #Load to PostgreSQL if environment is not github and also check if .env file is present
        if load_dotenv() and os.getenv("Environment") != "Github":
            #Connect and load data to PostgreSQL
            conn = psycopg2.connect(
                dbname=os.getenv("DB_NAME"),
                user=os.getenv("DB_USER"),
                password=os.getenv("DB_PASSWORD"),
                host=os.getenv("DB_HOST"),
                port=os.getenv("DB_PORT"),
            )
            load_to_db(df,conn)
        log_progress('ETL Completed')
if __name__ == "__main__":
    main()