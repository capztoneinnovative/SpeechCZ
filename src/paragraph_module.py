
from DataBase import DataBase
from error_handling import CustomException
from logger import logging


class ParagraphStory:
    def __init__(self, connect):
        self.connect = connect

    def retrieve(self):
        if self.connect:
            cursor = self.connect.cursor()
            sql_query_paragraph = "SELECT TOP 1 TextData FROM imgtxt ORDER BY NEWID();"
            cursor.execute(sql_query_paragraph)
            printed_sentence = cursor.fetchone()
            print(printed_sentence)
            logging.info("Retrieved paragraph from table: %s", printed_sentence)
        else:
            logging.error("Failed to connect to the database.")

        #return printed_sentence
