#import libraries
from services.log_service import log_progress


def load_to_csv(df, output_path):
    """ This function saves the final data frame as a CSV file in
    the provided path. Function returns nothing."""

    df.to_csv(output_path)

    log_progress('Data saved to CSV file')


def load_to_db(df, sql_connection, table_name):
    """ This function saves the final data frame to a database
    table with the provided name. Function returns nothing."""

    df.to_sql(table_name, sql_connection, if_exists='replace', index=False)

    log_progress('Data loaded to Database as a table, Executing queries')


def run_query(query_statement, sql_connection):
    """ This function runs the query on the database table and
    prints the output on the terminal. Function returns nothing. """

    cursor = sql_connection.cursor()
    cursor.execute(query_statement)
    result = cursor.fetchall()
    # for row in result:
    #     ic(row)

    log_progress('Process Complete')

    return result