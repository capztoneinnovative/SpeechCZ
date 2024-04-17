import os

from DataBase import DataBase
from Split_syllable import Split_syllable



def log_info_save():
    username = None
    password = None

    # Check if the login file exists
    if os.path.exists(r"C:\Projects\Info.txt"):
        with open(r"C:\Projects\Info.txt", "r") as file:
            lines = file.readlines()
            if len(lines) == 2:
                username = lines[0].strip()
                password = lines[1].strip()

    if username is None or password is None:
        # login info not found, prompt user
        username = input("Enter the username: ")
        password = input("Enter the password: ")

        # Save the login info to a file
        with open(r"C:\Projects\Info.txt", "w") as file:
            file.write(username + "\n")
            file.write(password)

    return username, password

def SpeechCZ():
    server = 'LAPTOP-S1QDCEQ9\SQLEXPRESS'
    database = 'Speech'
    username, password = log_info_save()

    db_connector = DataBase(server, database, username, password)
    connection = db_connector.connect()
    if connection:
        #cursor = connection.cursor()
        #input_letter = input("Enter the letter to search for: ")
        #sql_query = f"SELECT * FROM highword WHERE WordName LIKE '{input_letter}%';"
        
        cursor = connection.cursor()
        input_letter = input("Enter the letter to search for: ")
        sql_query = f"SELECT TOP 3 * FROM highword WHERE WordName LIKE '{input_letter}%';"
        cursor.execute(sql_query)
        rows = cursor.fetchall()
        print(rows)
        word_list = [item[1] for item in rows]
        print(word_list)  
    else:
        print("Failed to connect to the database.")
    
    speech_to_audio = Split_syllable(word_list)
    speech_to_audio.recognize_speech()

if __name__ == "__main__":
    SpeechCZ()
