import psycopg2
from sql_queries import create_table_queries, drop_table_queries
from dotenv import load_dotenv
import os

#Create Database
def create_database():
    #Load env variables
    load_dotenv()
    """
    - Creates and connects to the darazdb
    - Returns the connection and cursor to darazdb
    """
    # connect to default database
    conn = psycopg2.connect(
            dbname="postgres",
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT"),
        )
    conn.set_session(autocommit=True)
    cur = conn.cursor()
    
    # create daraz database with UTF8 encoding
    cur.execute("DROP DATABASE IF EXISTS darazdb")
    cur.execute("CREATE DATABASE darazdb WITH ENCODING 'utf8' TEMPLATE template0")

    # close connection to default database
    conn.close()    
    
    # connect to daraz database
    conn = psycopg2.connect(
        dbname=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
    )
    
    cur = conn.cursor()
    
    return cur, conn

#Drop Table
def drop_tables(cur, conn):
    """
    Drops each table using the queries in `drop_table_queries` list.
    """
    for query in drop_table_queries:
        cur.execute(query)
        conn.commit()

#Create Tables
def create_tables(cur, conn):
    """
    Creates each table using the queries in `create_table_queries` list. 
    """
    for query in create_table_queries:
        cur.execute(query)
        conn.commit()

#Main Function
def main():
    """
    - Drops (if exists) and Creates the daraz database. 
    
    - Establishes connection with the daraz database and gets
    cursor to it.  
    
    - Drops all the tables.  
    
    - Creates all tables needed. 
    
    - Finally, closes the connection. 
    """
    cur, conn = create_database()
    
    drop_tables(cur, conn)
    create_tables(cur, conn)

    conn.close()


if __name__ == "__main__":
    main()