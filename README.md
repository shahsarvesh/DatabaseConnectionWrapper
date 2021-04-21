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

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
