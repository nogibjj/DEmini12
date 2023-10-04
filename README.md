[![CI](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week5/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week5/actions/workflows/cicd.yml)
## Jeremy_Tan_IDS706_Week5
### File Structure
```
Jeremy_Tan_IDS706_Week5/
├── .devcontainer/
│   ├── devcontainer.json
│   └── Dockerfile
├── .github/
│   └── workflows/cicd.yml
├── .gitignore
├── AD_flow.svg
├── data/
│   └── serve_times.csv
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
├── ServeTimesDB.db
├── setup.sh
└── test_main.py
```
## Purpose of project
The purpose of this project is to build an ETL-Query pipeline. I use FiveThirtyEight's public dataset to extract it into a local csv file, tranfrom the csv file by cleaning it, loading it into a .db file, and querying it with SQLlite. 

## Preparation
1. open codespaces 
2. wait for container to be built and virtual environment to be activated with requirements.txt installed 
3. extract: run `make extract`
4. transform and load: run `make transform_load`
4. query: run `make query` or alternatively write your own query using `python main.py general_query <insert query>`

## Sample CRUD Operations 
Explanations of functions can be found [here](https://github.com/nogibjj/Jeremy_Tan_IDS706_Week5/blob/main/mylib/query.py)
1. Create: `python main.py create_record 'John Doe' 40 '2023-09-05' 'Jane Doe' '30-40' 1 '0-0'`
2. Read: `python main.py read_data`
3. Update: `python main.py update_record 1 'John Doe' 40 '2023-09-05' 'Jane Doe' '30-40' 1 '0-0'`
4. Delete: `python main.py delete_record 1`

## Check format and test errors 
1. Format code `make format`
2. Lint code `make lint`
3. Test coce `make test`

## Simple Vizualization of Process
![ETLQ](adflow.svg)

## References 
https://github.com/nogibjj/sqlite-lab