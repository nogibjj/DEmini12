"""
Transforms and Loads data into Azure Databricks
"""

import os
import pandas as pd
from databricks import sql
from dotenv import load_dotenv

def load(
    dataset="data/instagram-Data.csv", 
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

    # Connect to Databricks
    with sql.connect(
        server_hostname=server_h,
        http_path=http_path,
        access_token=access_token,
    ) as connection:
        cursor = connection.cursor()

        # Check if the InstagramData table exists and create if not
        cursor.execute("SHOW TABLES LIKE 'InstagramData'")
        result = cursor.fetchall()

        if not result:
            print("Creating InstagramData table...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS InstagramData (
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
            insert_data(cursor, df, "InstagramData")

        # Check if the InstagramTop1000 table exists and create if not
        cursor.execute("SHOW TABLES LIKE 'InstagramTop1000'")
        result = cursor.fetchall()

        if not result:
            print("Creating InstagramTop1000 table...")
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS InstagramTop1000 (
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
            # Insert data into InstagramTop1000
            # insert_data(cursor, df2, "InstagramTop1000")

        cursor.close()

    return "Success"

def insert_data(cursor, df, table_name):
    """Inserts data from a DataFrame into a specified table."""
    print(f"Inserting data into {table_name}...")
    for _, row in df.iterrows():
        # Use parameterized queries to prevent SQL injection
        cursor.execute(
            f"INSERT INTO {table_name} VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)", 
            tuple(row)
        )
    print(f"Data inserted into {table_name} successfully.")

# Example usage
if __name__ == "__main__":
    result = load()
    print(result)


load()