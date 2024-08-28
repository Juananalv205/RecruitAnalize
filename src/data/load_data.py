from .database import MysqlConnection
import pandas as pd
import os

class LoadData:
    
    def __init__(self):
        self.connection = MysqlConnection()

    def insert_data_from_dataframe(self, insert_sql_file_path, select_sql_file_path, table_name, dataframe):
        try:
            # Leer el archivo SQL de inserción
            with open(insert_sql_file_path, 'r') as file:
                insert_sql_script = file.read()
            insert_sql_script = insert_sql_script.replace('{{table_name}}', table_name)

            # Leer el archivo SQL de selección
            with open(select_sql_file_path, 'r') as file:
                select_sql_script = file.read()
            select_sql_script = select_sql_script.replace('{{table_name}}', table_name)

            # Conectar a la base de datos
            self.connection.open_connection()

            def insert_and_verify(start, end, expected_count):
                """Función auxiliar para insertar un bloque de datos y verificar la inserción"""
                for index, row in dataframe.iloc[start:end].iterrows():
                    data_tuple = tuple(row)
                    try:
                        self.connection.run_query(insert_sql_script, data_tuple)
                    except Exception as e:
                        print(f"Error durante la inserción de las filas {start} a {end}: {e}")
                        return False
                
                # Verificación automática
                try:
                    result = self.connection.run_select_query(select_sql_script)
                    if len(result) >= expected_count:
                        print(f"Verificación exitosa: {expected_count} filas encontradas.")
                        return True
                    else:
                        print(f"Verificación fallida. Se esperaban {expected_count} filas, pero se encontraron {len(result)}.")
                        return False
                except Exception as e:
                    print(f"Error durante la verificación de las filas {start} a {end}: {e}")
                    return False

            # **Fase de Prueba:** Subir y verificar las primeras 10 filas
            if not insert_and_verify(0, 10, 10):
                return "Verificación fallida en las primeras 10 filas. Proceso abortado."

            # **Fase Final:** Subir y verificar los datos en bloques de 1000
            total_rows = len(dataframe)
            for start in range(10, total_rows, 1000):
                end = min(start + 1000, total_rows)
                expected_count = end  # La cantidad esperada es el índice final
                if not insert_and_verify(start, end, expected_count):
                    return f"Verificación fallida en el bloque de filas {start} a {end}. Proceso abortado."
            return "Todos los datos insertados con éxito"
        except FileNotFoundError:
            return f"El archivo {insert_sql_file_path} o {select_sql_file_path} no se encontró."
        finally:
            self.connection.close_connection()
