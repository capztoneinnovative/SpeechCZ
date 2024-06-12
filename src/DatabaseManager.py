import pyodbc
import random
from error_handling import CustomException
from logger import logging

class DatabaseManager:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.connection = self.connect()

    def connect(self):
        try:
            conn = pyodbc.connect(
                f"DRIVER={{SQL Server}};SERVER={self.server};DATABASE={self.database};UID={self.username};PWD={self.password}"
            )
            logging.info("Database connection established successfully.")
            return conn
        except pyodbc.Error as e:
            logging.error(f"Error connecting to database: {e}")
            raise CustomException(f"Database connection error: {e}")

    def get_cursor(self):
        if self.connection:
            return self.connection.cursor()
        else:
            logging.error("Attempted to get cursor with no connection.")
            raise CustomException("No connection available.")

    def retrieve_random_prefix(self, num_prefix=1):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT prefix, examples FROM prefix')
            prefixes = cursor.fetchall()
            return random.choices(prefixes, k=num_prefix)  # Fetching all prefixes and selecting random ones
        except pyodbc.Error as e:
            logging.error(f"Error retrieving prefixes: {e}")
            raise CustomException(f"Error retrieving prefixes: {e}")

    def retrieve_random_suffixes(self, num_suffixes=1):
        try:
            cursor = self.get_cursor()
            cursor.execute('SELECT suffix, examples FROM suffixes')
            suffixes = cursor.fetchall()
            return random.choices(suffixes, k=num_suffixes)  # Fetching all suffixes and selecting random ones
        except pyodbc.Error as e:
            logging.error(f"Error retrieving suffixes: {e}")
            raise CustomException(f"Error retrieving suffixes: {e}")

    def close(self):
        if self.connection:
            self.connection.close()
            logging.info("Database connection closed.")
