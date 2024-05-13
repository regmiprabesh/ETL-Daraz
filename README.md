# ETL (Extract Transform Load)

This script extracts the data from another repositiory that scrapes the liquors from Daraz, and performs ETL pipeline, and stores it in PostgreSQL and CSV file.

## Table of Contents
1. [Introduction](#introduction)
2. [System Design](#system-design)
3. [Tools & Libraries](#tools)
4. [Installation](#installation)
5. [Project Structure](#project-structure)
6. [Usage](#usage)
7. [Data Schema](#data-schema)
8. [Workflow](#workflow)
9. [Future Work](#future-work)
10. [Conclusion](#conclusion)
11. [Contribution](#contribution)

## Introduction
ETL stands for “Extract, Transform, and Load” and describes the set of processes to extract data from one or multiple system, transform it, and load it into a target repository. An ETL is a data pipeline for cleaning, enriching, and transforming data from a variety of sources before integrating it for use in data analytics, business intelligence, and data science.The goal of ETL is to make it easier to analyse and report on data from multiple sources by creating a single, unified view of the data.

The Three Stages of ETL:

Extract: It involves pulling data from various sources. These sources can be databases, CRM systems, files, or any other data storage systems. The goal is to gather all the necessary data for further processing.

Transform: This step involves cleaning, validating, and formatting the data. The aim is to ensure that the data is accurate, consistent, and usable.

Load: Here, the transformed data is loaded into a data warehouse or another system where it can be analysed and used to make business decisions.

## System Design
![System Design](images/pipeline.png?raw=true "Title")

This system follows the traditional Extract, Load, Transformation pattern. The data is loaded from the jsonl file from the daraz-scraping github repository, which contains all the liquors with different categories, and the currency rate is loaded from the exchange_csv file inside the data folder in this repository. The data is then transformed, validated, and stored in PostgreSQL and a csv file inside the output folder. PostgreSQL is chosen as a better option because it is open-source and provides advantages such as scalability, ACID compliance, Extensibility etc. The data is even loaded into products.csv file inside the output folder for quickview during test phase.

## Tools
- Programming Language : Python
- Database : PostgreSQL

## Libraries
- Pandas : Used data manipulation and analysis 
- Requests : Used for loading product data from Github repository
- psycopg2 : Used for using PostgreSQL 
- python-dotenv: Used for environment variables

## Installation

  1. Clone this repository to your local machine:
        ```bash
        git clone https://github.com/regmiprabesh/ETL-Daraz
        ```
2. Open your terminal and navigate to the project directory:

    ```bash
    cd ETL-Daraz
    ```
3. Create a virtual environment for the project using venv:

    ```bash
    python -m venv venv_etl
    ```
4. Activate the virtual environment.

- For Mac/Linux 
  
  ```bash
  source venv_etl/bin/activate
  ```
- For Windows 
  
  ```bash
  .\venv_etl\Scripts\activate.bat
  ```

5. Install the required Python packages. 
    ```bash
    pip install -r requirements.txt
    ```

## Project Structure

The project has the following structure:
```
ETL-Daraz/
│
├── data/
│   └── exchange_rate.csv
│
├── images/
│   └── *
│
├── log/
│   └── log.txt
│
├── output/
│   └── products.csv
│  
├── services/
│   ├── __init__.py
│   ├── extract.py
│   ├── load.py
│   ├── log_service.py
│   ├── transform.py
│   └── validate.py
│
├── .env.example
│
├── main.py
│
├── README.md
│
└── requirements.txt


```
-   `data/`: This directory is where csv file of exchange rate is kept.
-   `exchange_rate.csv`: This csv file contains information of currency exchange rates which is used in transformation process.
-   `helper/`: This directory is database related files are kept
-   `db_helper.py`: This python script helps to create a database and add necessary tables to it.
-   `sql_queries.py`: This file contains different SQL queries for PostgreSQL for inserting, reading data.
-   `images/`: This directory contains different screenshot images of the system.
-   `logs/`: This directory contains log file.
-   `log.txt`: This file contains system log information which can be helpful during tests.
-   `output/`: This directory contains the output csv file after transformation.
-   `products.csv`: This file contains the product information after transformation.
-   `services/`: This directory is where code related to extract, transform, validation and load is kept.
-   `extract.py`: This file contains script to extract the product from jsonl file from daraz-scraper github repository and exchange_rate csv file from data folder in this repository.
-   `load.py`: This file contains the script used to load data into PostgreSQL and CSV file after transformation.
-   `log_service.py`: This file contains script related to writing into log file inside log folder.
-   `transform.py`: This file contains the script used for data transformation.
-   `validate.py`: This file contains the script used to validate data before storing into PostgreSQL and CSV file after transformation.
-   `.env.example`: This file contains example environment variables for PostgreSQL connection.
-   `main.py`: This is the main python script which initiates the ETL.
-   `README.md`: This file contains the documentation of the scraper.
-   `requirements.txt`: This file lists the Python dependencies for this project.


## Usage

Rename .env.example file to .env and update your PostgreSQL credentials there

To create required database schema and and tables navigate to the project directory and run the following command:
```bash
python helper/db_helper.py
```
To start etl, navigate to the project directory and run the following command:
```bash
python main.py
```
This will start the ETL and begin storing data in the PostgreSQL database and products.csv file inside output.

## Data Schema

The data after transformation in this project is organised into single product table: `products`.

- `products`: This table stores information about each product after transformation. It has the following fields:
    - `id`: An auto-incrementing integer that serves as the primary key.
    - `product_name`: The name of the product.
    - `product_price`: The price of the product in NPR.
    - `product_price_usd`: The price of the product in USD.
    - `product_price_eur`: The price of the product in EUR.
    - `product_price_gbp`: The price of the product in GBP.
    - `product_price_inr`: The price of the product in INR.
    - `product_rating`: The rating of the product, 0 if there are no ratings.
    - `sold_quantity`: The total quantity sold,0 if null.
    - `scraped_date`: Scraping date in DD/MM/YYYY format.

## WorkFlow
### 1. Extract
Data are loaded from JSONl file from daraz-scraper repository and CSV file from inside data directory and then read into dataframe for further manipulation and analysis.
![Product Json](images/product_jsonl.png?raw=true "Title")
![Category CSV](images/currency_csv.png?raw=true "Title")

### 2. Transform
Data are transformed at this stage.Duplicate data are removed here performing data cleaning. The different additional currency was added to the the table for better insight of the data. The null field in rating column and sold_quantity column didn't look so good so 0 is added for the empty data. One of the major problem was human readability in case of scraped date, the date was formatted into more readable format.The products with price less than 500 and not belonging to the category other than Spirits were filtered out to get the better view of the Spirits in the scraped data for better analysis.

![Raw Data](images/raw_data.png?raw=true "Title")

### 3. Validation
Data are validated at this stage. The transformed data are checked if they have any null value or if there is no data. Duplicate data are also checked here if found data are not loaded and log file is written that duplicate entry is found. If all validation test are passed then they are moved into further step to be loaded into database.

### 4. Load
Finally after the transformation, the data is loaded in PostgreSQL and CSV file inside the output folder. For quick access and easy testing during the development the data is also loaded in CSV file other than PostgreSQL
![Transformed Data](images/transformed_data1.png?raw=true "Title")

![Transformed Data](images/transformed_data2.png?raw=true "Title")

![Transformed Data](images/transformed_csv.png?raw=true "Title")

## Future Work
- Currently this ETL pipeline extracts data from a daraz e-commerce website only. We can expand this to include more sources, which would provide a more comprehensive view of the market.
- Data versioning can be implemented to keep track of changes to your data over time.
-   Data quality improvement with more sophisticated data cleaning and preprocessing techniques.
-   Currently ETL jobs need to be run manually or can be run in batches with cron jobs, in future real time ETL processes can be implemented.
-   As the data size can increase in huge number in future we can optimize the process my moving towards distributed framework like Apache Spark.
-   With this cleaned and processed data, we can implement more advanced analytics, such as predictive modelling in the near future.
-   We can use more security measures and ensure data protection,as data handling is a crucial step
-   Infuture alert system for any failures or significant deviations of data can be developed.
- Dashboard can be developed for better visualisation.
## Conclusion
In conclusion, this ETL project has successfully demonstrated the power of data extraction, transformation, and loading in providing valuable insights from e-commerce data. The project’s design, which leverages Python and PostgreSQL, ensures efficient data processing and storage. The use of Pandas for data manipulation and psycopg2 for PostgreSQL interaction further enhances the project’s effectiveness.

The project’s future work, which includes data source expansion, data quality checks, error handling, performance optimisation, data analysis, and visualisation, promises to elevate the project to new heights. The implementation of automated testing, data governance, data versioning, pipeline monitoring, user interface improvements, and thorough documentation will undoubtedly contribute to the project’s robustness and user-friendliness.

## Contribution

Contributions to this project are welcome. Please open an issue to discuss your proposed changes before making a pull request.