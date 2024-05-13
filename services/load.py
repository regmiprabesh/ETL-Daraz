#import libraries
from services.log_service import log_progress
from helper.sql_queries import products_table_insert, products_table_load

#Load data to CSV
def load_to_csv(df, output_path):
    """ This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing."""
    df.to_csv(output_path)
    log_progress('Data Stored To CSV File')

#Load Data to database
def load_to_db(df, conn):
    """ This function saves the final data frame to a database
    table with the provided name. Function returns nothing."""
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    """Iterate over the rows in DataFrame and insert
    into the table"""
    for _, row in df.iterrows():
        cur.execute(products_table_insert, tuple(row))
    run_query(products_table_load,conn)
    log_progress('Data Stored To PostgreSQL database')

#Get Data
def run_query(query_statement, conn):
    """ This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. """
    cursor = conn.cursor()
    cursor.execute(query_statement)
    result = cursor.fetchall()
    log_progress('Data Fetch Complete')
    return result