
[![CI](https://github.com/nogibjj/DEmini6/actions/workflows/cicd.yml/badge.svg?branch=main)](https://github.com/nogibjj/DEmini6/actions/workflows/cicd.yml)

## IDS706_Week6
### File Structure
```
DEmini6/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
├── .gitignore
├── data/
│   ├── instagram_Data.csv
│   └── instagram_global_top_1000.csv
├── Dockerfile
├── LICENSE
├── main.py
├── Makefile
├── mylib/
│   ├── __init__.py
│   ├── __pycache__/
│   ├── extract.py
│   ├── query.py
│   └── transform_load.py
├── query_log.md
├── README.md
├── requirements.txt
├── setup.sh
└── test_main.py
```
## Purpose of project
The goal of this project is to create an ETL-Query pipeline utilizing a cloud service like Databricks. This pipeline will involve tasks such as extracting data from Kaggle public datasets, cleaning and transforming the data, then loading it into Databricks SQL Warehouse. Once the data is in place, we'll be able to run complex queries that may involve tasks like joining tables, aggregating data, and sorting results. This will be accomplished by establishing a database connection to Databricks. 
## Preparation
1. open codespaces 
2. wait for container to be built and virtual environment to be activated with requirements.txt installed 
3. make your own .env file to store your Databricks' secrets as it requires a conncection to be established to Databricks
3. extract: run `make extract`
4. transform and load: run `make transform_load`
4. query: run `make query` or alternatively write your own query using `python main.py general_query <insert query>`

## Complex Query
Explanations of query:
```sql
    SELECT t1.country, t1.category, t1.category,
                AVG(t1.Followers) as avg_followers,
                COUNT(*) as total_Account
            FROM default.InstagramData t1
            JOIN default.InstagramTop1000 t2 ON t1.Account = t2.Account
            GROUP BY t1.country, t1.category
            ORDER BY avg_followers DESC
            LIMIT 10
```
- SELECT Clause:

- t1.country: Retrieves the country from the InstagramData table. t1.category, t1.category: Appears to have a duplicate column. This might be a typo, as you likely meant to select only one t1.category.
AVG(t1.Followers) AS avg_followers: Calculates the average number of followers for each group of country and category. COUNT(*) AS total_Account: Counts the total number of accounts in each group.

- Groups the data by country and category to calculate aggregate values (like AVG and COUNT).
- Sorts the results in descending order by the average number of followers.
- Limits the output to the top 10 results with the highest average followers.
   <img width="1176" alt="image" src="https://github.com/user-attachments/assets/9737d736-aaa0-4b8e-a4d0-ab55c6ec47e8">


## Check format and test errors 
1. Format code `make format`
2. Lint code `make lint`
3. Test coce `make test`


## References 
1. https://github.com/databricks/databricks-sql-python
2. https://github.com/nogibjj/cloud-database-LAB
3. https://learn.microsoft.com/en-us/azure/databricks/sql/admin/create-sql-warehouse
