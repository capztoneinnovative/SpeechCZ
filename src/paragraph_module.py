import sys
from DataBase import DataBase
from error_handling import CustomException
from logger import logging

import pyodbc # type: ignore


class ParagraphStory:
    def __init__(self, connection):
        self.connection = connection

    def paragraph_retrieve(self):
        if not self.connection:
            logging.error("Failed to connect to the database.")
            print("Failed to connect to the database.")
            return None
        try:
            cursor = self.connection.get_cursor()
            sql_query_paragraph = "SELECT TOP 1 TextData FROM imgtxt ORDER BY NEWID();"
            cursor.execute(sql_query_paragraph)
            printed_sentence = cursor.fetchone()
            print(printed_sentence)
            logging.info("Retrieved paragraph from table: %s", printed_sentence)
            return printed_sentence
        except pyodbc.Error as e:
            logging.error(f"Error executing SQL query: {e}")
            return None


