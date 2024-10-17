"""
Transforms and Loads data into Azure Databricks
"""

import os
import pandas as pd
from databricks import sql
from dotenv import load_dotenv

            # print("Creating InstagramData table...")
            # cursor.execute("""
            #     CREATE TABLE IF NOT EXISTS InstagramData (
            #         Country STRING,
            #         Rank INT,
            #         Account STRING,
            #         Title STRING,
            #         Link STRING,
            #         Category STRING,
            #         Followers INT,
            #         AudienceCountry STRING,
            #         AuthenticEngagement INT,
            #         EngagementAvg INT,
            #         Scraped STRING
            #     )

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
            # insert_data(cursor, df, "InstagramData")

        for _, row in df.iterrows():
                convert = (_,) + tuple(row)
                cursor.execute(f"INSERT INTO InstagramData VALUES {convert}")
        cursor.execute("SHOW TABLES FROM default LIKE 'Instagram*'")
        result = cursor.fetchall()
        # c.execute("DROP TABLE IF EXISTS InstagramData")
        if not result:
            cursor.execute(
                """
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
                """
            )
            for _, row in df2.iterrows():
                convert = (_,) + tuple(row)
                cursor.execute(f"INSERT INTO InstagramData VALUES {convert}")
        cursor.close()

    return "success"