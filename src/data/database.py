import mysql.connector
import os
from dotenv import load_dotenv

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
                print("Conexión Exitosa")
        except mysql.connector.Error as e:
            print(f"Error al conectar a la base de datos: {e}")
    
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
        print("Conexión cerrada")
        
    def run_query(self, query, params=None):
        try:
            self.open_connection()
            self.mycursor.execute(query)
            
            # Consumir resultados si hay filas disponibles
            if self.mycursor.with_rows:
                results = self.mycursor.fetchall()
                print(f"Resultados: {results}")
            self.mydb.commit()
            return "Consulta ejecutada con éxito"
        except mysql.connector.Error as e:
            return f"Error al ejecutar la consulta: {e}"
        finally:
            self.close_connection()
