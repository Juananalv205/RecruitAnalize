#Importing library
import sys
import os
from .database import MysqlConnection
import pandas as pd


#Class to load data
class LoadData:
    
    def __init__(self):
        self.connection = MysqlConnection()

    def insert_data_from_dataframe(self, insert_sql_file_path, select_sql_file_path, table_name, dataframe):
        try:
            # Read the insert SQL file
            with open(insert_sql_file_path, 'r') as file:
                insert_sql_script = file.read()
            insert_sql_script = insert_sql_script.replace('{{table_name}}', table_name)

            # Read the selection SQL file
            with open(select_sql_file_path, 'r') as file:
                select_sql_script = file.read()
            select_sql_script = select_sql_script.replace('{{table_name}}', table_name)

            # Connect to the database
            self.connection.open_connection()

            def insert_and_verify(start, end, expected_count):
                #Auxiliary function for inserting a data block and verifying insertion
                for index, row in dataframe.iloc[start:end].iterrows():
                    data_tuple = tuple(row)
                    try:
                        self.connection.run_query(insert_sql_script, data_tuple)
                    except Exception as e:
                        print(f"Error during row insertion {start} a {end}: {e}")
                        return False
                
                # Automatic verification
                try:
                    result = self.connection.run_select_query(select_sql_script)
                    if len(result) >= expected_count:
                        print(f"Successful verification: {expected_count} rows found.")
                        return True
                    else:
                        print(f"Failed verification. The following were expected {expected_count} but they found themselves in {len(result)}.")
                        return False
                except Exception as e:
                    print(f"Error during row verification {start} a {end}: {e}")
                    return False

            # Test Phase: Upload and verify first 10 rows
            if not insert_and_verify(0, 10, 10):
                return "Failed verification in the first 10 rows. Process aborted."

            # Final Phase: Upload and verify data in blocks of 1000
            total_rows = len(dataframe)
            for start in range(10, total_rows, 1000):
                end = min(start + 1000, total_rows)
                expected_count = end  # The expected amount is the final rate
                if not insert_and_verify(start, end, expected_count):
                    return f"Failed verification in row block {start} a {end}. Process aborted."
            return "All data successfully inserted"
        except FileNotFoundError:
            return f"The file {insert_sql_file_path} or {select_sql_file_path} was not found."
        finally:
            self.connection.close_connection()
