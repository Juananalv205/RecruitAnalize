import mysql.connector
import os
from dotenv import load_dotenv
import pandas as pd

load_dotenv("../.env")

class MysqlConnection():
    
    def __init__(self):
        self.host = os.getenv('DatabaseHost')
        self.port = os.getenv('DatabasePort')
        self.user = os.getenv('DatabaseUser')
        self.password = os.getenv('DatabasePassword')
        self.database = os.getenv('DatabaseName')
        self.mydb = None
        self.mycursor = None
        
    def open_connection(self):
        print("Utilizando Conexión a MySQL")
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
                return "Conexión Exitosa"
        except mysql.connector.Error as e:
            return f"Error al conectar a la base de datos: {e}"
    
    def close_connection(self):
        if self.mycursor:
            try:
                # Asegurarse de consumir todos los resultados no leídos
                self.mycursor.fetchall()
            except mysql.connector.Error:
                pass  # Ignorar errores si no hay resultados por consumir
            self.mycursor.close()
        if self.mydb:
            self.mydb.close()
        return "Conexión cerrada"
        
    def run_query(self, query, params=None):
        try:
            self.mycursor.execute(query, params)  # Usar los parámetros aquí
            # Consumir resultados si hay filas disponibles
            if self.mycursor.with_rows:
                results = self.mycursor.fetchall()
                print(f"Resultados: {results}")
            self.mydb.commit()
            return "Consulta ejecutada con éxito"
        except mysql.connector.Error as e:
            return f"Error al ejecutar la consulta: {e}"
        
    def run_select_query(self, query, params=None):
        try:
            self.mycursor.execute(query, params)
            results = self.mycursor.fetchall()
            return results
        except mysql.connector.Error as e:
            return f"Error al ejecutar la consulta SELECT: {e}"

    def open_query(self, query_path, table_name):
        with open(query_path, 'r') as file:
            select_sql_script = file.read()
        query = select_sql_script.replace('{{table_name}}', table_name)
        return query

    def create_dataframe(self, query_path, table_name):
        try:
            self.open_connection()
            select_sql_script = self.open_query(query_path, table_name)
            rows =  self.run_select_query(select_sql_script)# Obtener los resultados después de ejecutar la consulta
            colnames = [desc[0] for desc in self.mycursor.description]
            df = pd.DataFrame(rows, columns=colnames)
            return df
        except mysql.connector.Error as e:
            return f"Error al crear el DataFrame: {e}"
        finally:
            self.close_connection()
