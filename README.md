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

## Create or Add a table in the database from a pandas dataframe
Populate database with a dataframe using `create_table_from_data()`. The function creates a log with a `sql_traceback` and all queries that were executed. Since we're adding a dataframe to the databse, using Python's `read_*` we can add any data with any intermediate clean operations to the database. If the table exists, the new data will be appended to the exisiting table otherwise a new table will be created. 
```python
# Set up Database connection
database_name = 'sample.db'
path = 'path/to/db/file' + database_name
data_conn = DataBaseConnection(path)

# Read a dataframe into memory
# Sample Data
data = {
    'foo':[1,2,3],
    'bar':['a','b','c']
}

df = pd.DataFrame.from_dict(data)
table_name = 'table name'

data_conn.create_table_from_data(df, table_name)
```
#### Output
```
2021-04-21 17:11:33 data_connection.py: create_table_from_data: 122 INFO: Successfully created a table in sample.db
```
This function is great for on the go database and querying, however it is recommended to use SQL `CREATE_TABLE` to create tables first so that you can define primary key, foreign keys and datatypes for tuples. And then use `create_table_from_data()` to add data.

## Querying data from Database
In order to handle large datasets, it is easier to do bulk of aggregations within the database and import the results back in Python.

#### Sample SQL query
```SQL
SELECT * FROM TABLE WHERE COLUMN = VALUE
```
**Steps:**
1. Run the SQL query in a SQL environment
2. Store the result as a file in local harddrive
3. Import the results as a dataframe with appropriate dtypes
4. Carry out further operations   

With `execute_query_to_dataframe()` we can directly store SQL results in memory for futher operations.

#### Sample Python
```python
# Set up Database connection
database_name = 'sample.db'
path = 'path/to/db/file' + database_name
data_conn = DataBaseConnection(path)

query = """
    SELECT * FROM table_name WHERE column1 = value1
"""
# Execute the query and store the results in the dataframe
df = data_conn.execute_query_to_dataframe(query)

# Carry on with your pipeline
---
# YOUR ETL CODE

```
## Querying data into Database
We can run a comprehensive ETL operation in Python and store the output back into SQL database using out `DatabaseConnection` using `create_table_from_data()`

```python
query = """YOUR SQL QUERY TO GET SOME DATA"""
# Execute the query and store the results in the dataframe
df = data_conn.execute_query_to_dataframe(query)

---
# YOUR ETL CODE
---
table_name = 'POST ETL NEW TABLE'
data_conn.create_table_from_data(df, table_name)
```

Similarly you can also write custom SQL statements and use `execute_query` to update database
```python
query = """
    UPDATE table_name
    SET column1 = value1, column2 = value2, ...
    WHERE condition;
"""

data_conn.execute_query(query)
```
-------
# License: 
MIT License

Copyright (c) 2021 Sarvesh Shah

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.
