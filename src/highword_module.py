import sys
from DataBase import DataBase
from error_handling import CustomException
from logger import logging


class HighWord:
    def __init__(self, connect):
        self.connect = connect

    def word_retrieve(self, input_letter):
        try:
            if self.connect:
                cursor = self.connect.cursor()
                high_frequency_word_query = f"SELECT TOP 3 * FROM highword WHERE WordName LIKE '{input_letter}%';"
                cursor.execute(high_frequency_word_query)
                rows = cursor.fetchall()
                word_list = [item[1] for item in rows]
                logging.info("Retrieved word list: %s", word_list)
            else:
                logging.error("Failed to connect to the database.")
        except Exception as e:
            logging.error("Error occurred while executing SQL query:", exc_info=True)
            raise CustomException(e, sys)

