
import pyodbc               # type: ignore          
import sys
from error_handling import CustomException
from logger import logging


class DataBase:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = self.connect()

    def connect(self):
        try:
            conn = pyodbc.connect(f"DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}")
            return conn
        except pyodbc.Error as e:
            #logging.error("Error inserting data:", exc_info=True)
            print(f"Error connecting to database: {e}")
            return None

    def get_cursor(self):
        if self.connection:
            return self.connection.cursor()
        else:
            raise CustomException("No connection available.")





    