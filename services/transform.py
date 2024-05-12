#import libraries
from services.log_service import log_progress
import pandas as pd

#Transform Data
def transform(df, csv_path):
    log_progress('Data Transformation Started.')
    """ Remove the duplicate entries and keep the last scraped product entry for each product with reindexing"""
    df = df.drop_duplicates(subset='product_name', keep='last')
    df.reset_index(drop=True, inplace=True)
    """ Remove unnecessary columns product_url and total_reviews """
    df = df.drop(['product_url', 'total_reviews'], axis=1)
    """ Access the CSV file for exchange rate
    information, and adds four columns to the data frame, each
    containing the transformed version of Market Cap column to
    respective currencies"""
    exchange_rate = pd.read_csv(csv_path, index_col=0).to_dict()['Rate']
    df['Product Price(USD)'] = round(df['product_price'] / exchange_rate['USD'], 2)
    df['Product Price(GBP)'] = round(df['product_price'] / exchange_rate['GBP'], 2)
    df['Product Price(EUR)'] = round(df['product_price'] / exchange_rate['EUR'], 2)
    df['Product Price(INR)'] = round(df['product_price'] / exchange_rate['INR'], 2)
    """ Fill zero if rating is not available"""
    df['product_rating'] = df['product_rating'].fillna(0)
    """ Fill zero if sold quantity is not available"""
    df['sold_quantity'] = df['sold_quantity'].fillna(0)
    """ Convert scraped date format to DD/MM/YYYY"""
    df['scraped_date'] = pd.to_datetime(df['scraped_date']).dt.strftime('%d/%m/%Y')
    log_progress('Data Transformation Completed.')
    return df