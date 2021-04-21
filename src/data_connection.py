import sqlite3
import pandas as pd

import os
cur_dir = os.path.dirname(os.path.abspath(__file__))

import logger
logging = logger.get_logger('logger', 'log.log')

class DataBaseConnection():
    """
    @class
    Establishes a Database connection to a database. If the database does not exist a new database will be created. 

    Attributes:
    -----------
    database_name: str
        Name of the database that needs to be created or connected to
    
    conn: sqlite connect object
        Internal variable auto initialized 

    cursor: sqlite cursor object
        Internal variable auto initialized 

    Methods:
    --------
    execute_raw_query(query)
        Executes a query and returns list of tuples 

    execute_query(query)
        Executes a query and returns list of tuples

    create_table_from_data(data, table_name)
        Create a database table from DataFrame

    get_tables_from_data()
        Returns a list of tables from SQL DB
    """

    # Initialize contructor 
    def __init__(self, database_name):
        self.database_name = database_name
        self.conn = sqlite3.connect(self.database_name)
        self.cursor = self.conn.cursor()

    def execute_raw_query(self, query):
        """
        Executes a query and returns list of tuples 

        Parameters:
        -----------
        query: str
            A SQL query 
        
        Returns:
        --------
        data: list of tuple
            List of tuples with headers as first tuple and first element of each tuple as the index
        """
        try:
            # Execute query and fetch all the rows 
            self.cursor.execute(query)
            data = self.cursor.fetchall()
            # Extract column names from cursor attributes
            column_names = tuple(map(lambda x: x[0], self.cursor.description))
            data.insert(0, column_names)
            # Create a log traceback for query information
            self.conn.set_trace_callback(logging.info)
            logging.info("Queried Data from {}. Rows = {}".format(self.database_name,len(data)))
            return data
        except:
            logging.exception('Something went wrong')
            return None

    def execute_query(self, query):
        """
        Executes a query and returns list of tuples 

        Parameters:
        -----------
        query: str
            A SQL query 
        
        Returns:
        --------
        data: DataFrame
            Output of SQL query as a DataFrame
        """
        try:
            # Read SQL Queries
            df = pd.read_sql_query(query, self.conn, index_col='index')
            self.conn.set_trace_callback(logging.info)
            logging.info("Queried Data from {}. Shape = {}".format(self.database_name,df.shape))
            return df
        except:
            logging.exception('Something went wrong')
            return None

    def create_table_from_data(self, data, table_name):
        """
        Create a database table from DataFrame

        Parameters:
        -----------
        data: DataFrame
            DataFrame that needs to be converted to SQL
        
        table_name: str
            Name of the table for the database
        
        Returns:
        --------
        status_code: int
            Status code, 0 for success and -1 for failure
        """
        try:
            # Send the data to SQL
            data.to_sql(table_name, con = self.conn, if_exists = 'append')
            self.conn.set_trace_callback(logging.info)
            return 0
        except:
            logging.exception('Something went wrong')
            return -1

    def get_tables_from_data(self):
        """
        Returns a list of tables from SQL DB

        Parameters:
        -----------
        None 
        
        Returns:
        --------
        table_names: list
            List of table names
        """
        try:
            # Execute query
            self.cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
            self.conn.set_trace_callback(logging.info)
            return self.cursor.fetchall()
        except:
            logging.exception('Something went wrong')
            return None

    def close_sql_connection(self):
        """
        Close connection object 
        """
        logging.info('Connection closed')
        self.conn.close()

    def __repr__(self):
        return "DataBaseConnection: %s"%(self.database_name)

def main():

    # Create a new database connection
    database_name = cur_dir+'/../data/test_db.db'
    data_conn = DataBaseConnection(database_name)

    # # Get list of exisiting data in database
    print(data_conn.get_tables_from_data())

    # Add a new table to database from csv/xlsx using Pandas
    df = pd.read_csv(cur_dir+'/../data/sample.csv') # Read the dataframe
    print(df)

    # Use the function and assign it a table name
    data_conn.create_table_from_data(df, table_name = 'sample_data')

    # Pass a query to function
    query = "select * from sample_data where A=1"

    # Run a custom query against the database
    data = data_conn.execute_raw_query(query)
    # print(data) # print the data 

    # Run a custom query and get output as dataframe
    dataframe = data_conn.execute_query(query)
    # print(dataframe)

    data_conn.close_sql_connection()

if __name__ == '__main__':
    main()