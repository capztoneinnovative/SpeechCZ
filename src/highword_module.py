
from DataBase import DataBase
from error_handling import CustomException
from logger import logging

class HighWord:
    def __init__(self, connect, input_letter):
        self.connect = connect
        self.input_letter = input_letter

    def retrieve(self):
        if self.connect:
            cursor = self.connect.cursor()
            high_frequency_word_query = f"SELECT TOP 3 * FROM highword WHERE WordName LIKE '{self.input_letter}%';"
            cursor.execute(high_frequency_word_query)
            rows = cursor.fetchall()
            word_list = [item[1] for item in rows]
            logging.info("Retrieved word list: %s", word_list)
            #print(word_list)
        else:
            logging.error("Failed to connect to the database.")
            #print("Failed to connect to the database.")
        #return None
