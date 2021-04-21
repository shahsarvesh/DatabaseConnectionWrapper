# DatabaseConnectionWrapper

This wrapper allows a Python application to work with a Database without having to manage a database connection.

## Creating a Database connection
Start with creating a database connection object. The DataBaseConnection accepts a database file in the directory  
```python
# Set up Database connection
database_name = 'sample.db'
path = 'path/to/db/file' + database_name
data_conn = DataBaseConnection(path)
``` 
If a database exists then it will connect to the database, but if database does not exist then a new database file will be created.

## Add a file into the database
Populate database with a dataframe using `create_table_from_data()`. The function creates a log with a `sql_traceback` and all queries that were executed.
```python
# Read a dataframe into memory
# Sample Data
data = {
    'foo':[1,2,3],
    'bar':['a','b','c']
}

df = pd.DataFrame.from_dict(data)
table_name = 'table name'

data_conn.create_table_drom_data(df, table_name)
```
#### Output
```
2021-04-21 17:11:33 data_connection.py: create_table_from_data: 122 INFO: Successfully created a table in sample.db
```
