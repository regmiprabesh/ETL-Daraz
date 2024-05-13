""" This module contains string constants which contain SQL scripts for
creating/dropping tables and inserting data into those tables.

These constants are imported by other python scripts in order to perform
the ETL work.
"""

# DROP TABLES
products_table_drop = "DROP TABLE IF EXISTS products"


# CREATE TABLES
products_table_create = """
CREATE TABLE IF NOT EXISTS products (
                id SERIAL PRIMARY KEY,
                product_name text,
                product_price DECIMAL(10, 5),
                product_price_usd DECIMAL(10, 5),
                product_price_eur DECIMAL(10, 5),
                product_price_gbp DECIMAL(10, 5),
                product_price_inr DECIMAL(10, 5),
                product_rating DECIMAL(10, 5),
                sold_quantity INTEGER,
                scraped_date text
);
"""

# INSERT RECORDS
products_table_insert = """
INSERT INTO products (product_name, product_price, product_rating, sold_quantity, scraped_date,  product_price_usd, product_price_eur, product_price_gbp, product_price_inr)
     VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s);"""

# LOAD RECORDS
products_table_load = """
SELECT * FROM products;"""

# QUERY LISTS
create_table_queries = [products_table_create]
drop_table_queries = [products_table_drop]