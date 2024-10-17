"""
Transforms and Loads data into Azure Databricks
"""
import sys
import os
import pandas as pd
from databricks import sql
import numpy as np
from dotenv import load_dotenv
sys.path.append('/Library/Frameworks/Python.framework/Versions/3.12/lib/python3.12/site-packages')

def load(
    dataset="data/instagram_Data.csv", 
    dataset2="data/instagram_global_top_1000.csv"
):
    """Loads data into Databricks from CSV files."""

    # Load environment variables
    load_dotenv()
    server_h = os.getenv("SERVER_HOSTNAME")
    access_token = os.getenv("ACCESS_TOKEN")
    http_path = os.getenv("HTTP_PATH")

    # Load the CSV files into DataFrames
    df = pd.read_csv(dataset, delimiter=",", skiprows=1)
    df2 = pd.read_csv(dataset2, delimiter=",", skiprows=1)
    df = df.replace({np.nan: None})
    df2 = df2.replace({np.nan: None})
    # Connect to Databricks
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        cursor = connection.cursor()

        # Check if the InstagramData table exists and create if not
        cursor.execute("SHOW TABLES LIKE 'instagramtop1000'")
        result = cursor.fetchall()

        if not result:
            print("Creating instagramtop1000 table...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS instagramtop1000 (
                    Country STRING,
                    Rank INT,
                    Account STRING,
                    Title STRING,
                    Link STRING,
                    Category STRING,
                    Followers INT,
                    AudienceCountry STRING,
                    AuthenticEngagement INT,
                    EngagementAvg INT,
                    Scraped STRING
                )
            """)
            # Insert data into InstagramData
            # insert_data(cursor, df, "InstagramData")
        # for _, row in df2.iterrows():
        #     # Replace None with 'NULL' during value preparation
        #     converted_row = [f"NULL" if x is None else f"'{x}'" if isinstance(x, str) else x for x in row]
            
        #     # Join the values properly into the SQL query
        #     values = ', '.join(map(str, converted_row))
        #     sqlc = f"INSERT INTO instagramtop1000 VALUES ({values})"
            
        #     # Execute the query
        #     cursor.execute(sqlc)

        # result = cursor.fetchall()
        # c.execute("DROP TABLE IF EXISTS InstagramData")
        if not result:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS instagramtop1000 (
                    Country STRING,
                    Rank INT,
                    Account STRING,
                    Title STRING,
                    Link STRING,
                    Category STRING,
                    Followers INT,
                    AudienceCountry STRING,
                    AuthenticEngagement INT,
                    EngagementAvg INT,
                    Scraped STRINGmake
                )
                """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                cursor.execute(f"INSERT INTO instagramtop1000 VALUES {convert}")
        cursor.close()

    return "success"