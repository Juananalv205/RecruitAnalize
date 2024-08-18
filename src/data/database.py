import mysql.connector
import os
from dotenv import load_dotenv

load_dotenv("../.env")

class MysqlConnection():
        
    def __init__(self):
        self.mydb = None
        self.mycursor = None
        print("Utilizando Conexión a MySQL")
        try:
                self.mydb = mysql.connector.connect(
                    host=os.getenv('DatabaseHost'),
                    port=os.getenv('DatabasePort'),
                    user=os.getenv('DatabaseUser'),
                    password=os.getenv('DatabasePassword'),
                    database=os.getenv('DatabaseName')
                )
                self.mycursor = self.mydb.cursor()
        except mysql.connector.Error as e:
            print("Error al conectar a la base de datos:", e)
    
    def close_connection(self):
        if self.mycursor:
            self.mycursor.close()
        if self.mydb:
            self.mydb.close()
        print("Conexión cerrada")
        
    def get_table(self, table):
            
            try:
                self.mycursor.execute(f"SELECT * FROM {table}")
                myresult = self.mycursor.fetchall()
                return myresult
            except mysql.connector.Error as e:
                return f"Error al obtener los datos de la tabla {table}: {e}"
            finally:
                self.close_connection()
