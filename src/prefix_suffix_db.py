# db_loader.py
import pyodbc # type: ignore

class prefix_suffix_db_loader:
    def __init__(self, server, database, username, password, driver='ODBC Driver 17 for SQL Server'):
        self.connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

    def get_connection(self):
        return pyodbc.connect(self.connection_string)

    def get_list_from_db(self, table_name):
        conn = self.get_connection()
        cursor = conn.cursor()
        cursor.execute(f"SELECT {table_name[:-1]} FROM {table_name}")
        result = cursor.fetchall()
        conn.close()
        return [row[0] for row in result]

    def get_prefixes(self):
        return self.get_list_from_db('Prefixes')

    def get_suffixes(self):
        return self.get_list_from_db('Suffixes')

    def get_roots(self):
        return self.get_list_from_db('Roots')

