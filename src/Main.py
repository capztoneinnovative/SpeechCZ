

#import sys
from DataBase import DataBase

from highword_module import HighWord
from paragraph_module import ParagraphStory
from speechcz import SpeechCZ
from error_handling import CustomException
from logger import logging

def get_database_connection():
    server = 'LAPTOP-S1QDCEQ9\SQLEXPRESS'
    database = 'Speech'
    username = 'karan'
    password = '123456789'
    return DataBase(server, database, username, password)

def main():
    try:
        connect = get_database_connection()
        print("connected")
        #logging.info("Connection established.")
        my_instance = SpeechCZ(connect)

        option_functions = {
            1: my_instance.highword,
            2: my_instance.paragraph_story
        }

        option = int(input("Enter the option 1 or 2: "))
        if option in option_functions:
            if option == 1:
                input_letter = input("Enter the starting letter: ")
                highword_instance = HighWord(connect)
                option_functions[option](highword_instance, input_letter)
            else:
                paragraph_instance = ParagraphStory(connect)
                option_functions[option](paragraph_instance)
        else:
            logging.error("Invalid option")
    except Exception as e:
        logging.error("An error occurred:", exc_info=True)
        #raise CustomException(e, sys)

if __name__ == "__main__":
    main()
