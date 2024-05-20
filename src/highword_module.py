
import sys
from DataBase import DataBase
from error_handling import CustomException
from logger import logging
import pyodbc # type: ignore



class HighWord:
    def __init__(self, connection):
        self.connection = connection

    def word_retrieve(self, input_letter):
        if not self.connection:
            logging.error("Failed to connect to the database.")
            print("Failed to connect to the database.")
            return None
        try:
            cursor = self.connection.get_cursor()
            query = "SELECT TOP 3 * FROM highword WHERE WordName LIKE ?;"
            cursor.execute(query, (input_letter + "%",))
            rows = cursor.fetchall()
            word_list = [item[1] for item in rows]
            logging.info("Retrieved word list: %s", word_list)
            return word_list
        except pyodbc.Error as e:
            logging.error(f"Error executing SQL query: {e}")
            return None
