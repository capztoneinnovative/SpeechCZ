import os

from DataBase import DataBase
from Split_syllable import Split_syllable
from Paragraph import Paragraph
from logger import logging


def log_info_save():
    username = None
    password = None

    # Get the current working directory
    current_directory = os.getcwd()

    # Specify the file name 
    # Info.Txt file is store DataBase USERNAME and PASSWORD
    file_path = os.path.join(current_directory, "Info.txt")

    # Check if the login file exists
    if os.path.exists(file_path):
        with open(file_path, "r") as file:
            lines = file.readlines()
            if len(lines) == 2:
                username = lines[0].strip()
                password = lines[1].strip()

    if username is None or password is None:
        # login info not found, prompt user
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        # Save the login info to a file
        with open(file_path, "w") as file:
            file.write(username + "\n")
            file.write(password)

    return username, password

## connect into DataBase Table

def SpeechCZ():
    # connect the db
    server = 'LAPTOP-S1QDCEQ9\SQLEXPRESS'
    database = 'Speech'
    username, password = log_info_save()

    db_connector = DataBase(server, database, username, password)
    connect = db_connector.connect()
 
 ##  module 1 High Frequency word retrieve from DB table     
    """
    if connect:  
        cursor = connect.cursor()
        High_frequency_word = f"SELECT TOP 3 * FROM highword WHERE WordName LIKE '{input_letter}%';"
        cursor.execute(High_frequency_word)
        rows = cursor.fetchall()
        word_list = [item[1] for item in rows]
        logging.info("Retrieved word list: %s", word_list)
        print(word_list)  
    else:
        logging.error("Failed to connect to the database.")
        print("Failed to connect to the database.")
        
    
    speech_to_audio = Split_syllable(word_list)
    speech_to_audio.recognize_speech()
"""
    
## Module 2 Paragraph Read from DB Table
    if connect:
        cursor = connect.cursor()
        sql_query_paragraph= f"select top 1 TextData from imgtxt order by newID()"
        cursor.execute(sql_query_paragraph)
        printed_sentence = cursor.fetchall()
        print(printed_sentence)
        print(type(printed_sentence))
        logging.info("Retrieved Paragraph from table: %s", printed_sentence)
    else:
        logging.error("Failed to connect to the database.")
    
    
    read_paragraph= Paragraph(printed_sentence)
    read_paragraph.speech_to_text()
    read_paragraph.run()

## SpeechCZ function Execute part:

if __name__ == "__main__":
    #input_letter = input("Enter the letter to search for: ")
    SpeechCZ()

