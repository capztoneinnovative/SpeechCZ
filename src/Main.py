

import sys
from DataBase import DataBase
from speechcz import SpeechCZ
from error_handling import CustomException
from logger import logging


def main():
    server = 'LAPTOP-S1QDCEQ9\SQLEXPRESS'
    database = 'Speech'
    username = 'karan'
    password = '123456789'
    
    try:
        connection = DataBase(server, database, username, password)
        option = int(input("Choose an option:\n1. High Words\n2. Paragraph\n"))
        
        if option == 1:
            input_letter = input("Enter the starting letter: ")
            speech = SpeechCZ(connection)
            speech.highword_instance(input_letter)
        elif option == 2:
            speech = SpeechCZ(connection)
            speech.paragraph_instance()
        else:
            logging.error("Invalid option.")
            
    except Exception as e:
        #print(f"An error occurred: {e}")
        raise CustomException(e,sys)
        
if __name__ == "__main__":
    main()


