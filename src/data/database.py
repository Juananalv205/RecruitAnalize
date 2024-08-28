#Importing library
import mysql.connector
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv("../.env")

class MysqlConnection():
    #import credentials from .env file
    def __init__(self):
        self.host = os.getenv('DatabaseHost')
        self.port = os.getenv('DatabasePort')
        self.user = os.getenv('DatabaseUser')
        self.password = os.getenv('DatabasePassword')
        self.database = os.getenv('DatabaseName')
        self.mydb = None
        self.mycursor = None
    
    #Open connection to the database
    def open_connection(self):
        try:
            self.mydb = mysql.connector.connect(
                host=self.host,
                port=self.port,
                user=self.user,
                password=self.password,
                database=self.database
            )
            self.mycursor = self.mydb.cursor()
            if self.mydb is not None:
                return "Successful Connection"
        except mysql.connector.Error as e:
            return f"Error connecting to the database: {e}"
    
    #Close connection to the database
    def close_connection(self):
        if self.mycursor:
            try:
                # Make sure to consume all unread results.
                self.mycursor.fetchall()
            except mysql.connector.Error:
                pass  # Ignore errors if no results to consume
            self.mycursor.close()
        if self.mydb:
            self.mydb.close()
        return "Closed connection"
    #Run query with commit
    def run_query(self, query, params=None):
        try:
            self.mycursor.execute(query, params)  # Use the parameters here
            # Consume results if rows are available
            if self.mycursor.with_rows:
                results = self.mycursor.fetchall()
            self.mydb.commit()
            return "Consultation successfully executed"
        except mysql.connector.Error as e:
            return f"Error executing query: {e}"
    
    #Run select query without commit
    def run_select_query(self, query, params=None):
        try:
            self.mycursor.execute(query, params)
            results = self.mycursor.fetchall()
            return results
        except mysql.connector.Error as e:
            return f"Error when executing the SELECT query:: {e}"

    #Open and create dinamic query
    def open_query(self, query_path, table_name):
        with open(query_path, 'r') as file:
            select_sql_script = file.read()
        query = select_sql_script.replace('{{table_name}}', table_name)
        return query

    #Create dataframe from query
    def create_dataframe(self, query_path, table_name):
        try:
            self.open_connection()
            select_sql_script = self.open_query(query_path, table_name)
            rows =  self.run_select_query(select_sql_script)# Get the results after executing the query
            colnames = [desc[0] for desc in self.mycursor.description]
            df = pd.DataFrame(rows, columns=colnames)
            return df
        except mysql.connector.Error as e:
            return f"Error creating DataFrame: {e}"
        finally:
            self.close_connection()
