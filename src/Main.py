"""
import sys
import os
from DatabaseManager import DatabaseManager
from TextToSpeech import TextToSpeech
from prefix import PrefixApplication
from suffix import SuffixApplication
from error_handling import CustomException
from logger import logging
from userinfo import UserHandler
from highword_speech_results import DatabaseHandler
from HighFrequencyHandler import HighFrequency
from ParagraphStoryHandler import ParagraphStoryHandler
from paragraph_read_result import ReadingResults

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <function_name>")
        return

    server = 'LAPTOP-S1QDCEQ9\\SQLEXPRESS'
    database = 'Speech'
    username = 'karan'
    password = '123456789'

    function_name = sys.argv[1]

    try:
        # Create a UserHandler instance and attempt to login
        user_handler = UserHandler(server, database, username, password)
        
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        
        if user_handler.login_user(username_input, password_input):
            print("Login successful")

            if function_name == 'prefix':
                db_manager = DatabaseManager(server, database, username, password)
                tts = TextToSpeech()
                app = PrefixApplication(db_manager, tts)
                app.run()
            
            elif function_name == 'suffix':
                db_manager = DatabaseManager(server, database, username, password)
                tts = TextToSpeech()
                app = SuffixApplication(db_manager, tts)
                app.run()
            
            elif function_name == "highfrequency":
                high_frequency = HighFrequency(server, database, username, password)
                input_letter = input("Enter the starting letter: ")
                word_list = high_frequency.word_retrieve(input_letter)
                results = high_frequency.recognize_and_write_output(word_list)

                # Insert results into database
                db_handler = DatabaseHandler(server, database, username, password)
                for result in results:
                    db_handler.insert_result(
                        result['high_freq_word'], result['correct_count'], result['incorrect_count'],
                        result['total_attempts'], result['accuracy_rate'], username
                    )
                db_handler.close()
            
            elif function_name == "paragraphread":
                paragraph_handler = ParagraphStoryHandler(server, database, username, password)
                paragraph_retrieves = paragraph_handler.paragraph_retrieve()
                results = paragraph_handler.recognize_and_write_output(paragraph_retrieves)

                db_handler = ReadingResults(server, database, username, password)
                for result in results:
                    # Assuming 'incorrect_word_list' is a string or a type that can be converted to a valid SQL data type
                    incorrect_word_list_str = ','.join(result['incorrect_word_list'])  # Convert list to string if necessary
                    db_handler.insert_data(
                        username, incorrect_word_list_str
                    )
                db_handler.close_connection()

            else:
                print(f"Function '{function_name}' not recognized.")
        else:
            print("Login failed. Please check your username and password.")
        
        user_handler.close()
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()

"""


"""
import sys
from DatabaseManager import DatabaseManager
from TextToSpeech import TextToSpeech
from prefix import PrefixApplication
from suffix import SuffixApplication
from error_handling import CustomException
from logger import logging

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <prefix|suffix>")
        return

    server = 'LAPTOP-S1QDCEQ9\\SQLEXPRESS'
    database = 'Speech'
    username = 'karan'
    password = '123456789'

    function_name = sys.argv[1]

    db_manager = DatabaseManager(server, database, username, password)
    tts = TextToSpeech()

    if function_name == 'prefix':
        app = PrefixApplication(db_manager, tts)
    elif function_name == 'suffix':
        app = SuffixApplication(db_manager, tts)
    else:
        print("Invalid function name. Please choose 'prefix' or 'suffix'.")
        return

    app.run()

if __name__ == "__main__":
    main()


"""



"""
import sys
import os

sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from userinfo import UserHandler
from highword_speech_results import DatabaseHandler
from HighFrequencyHandler import HighFrequency
from ParagraphStoryHandler import ParagraphStoryHandler
from paragraph_read_result import ReadingResults

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <function_name>")
        return

    server = 'LAPTOP-S1QDCEQ9\\SQLEXPRESS'
    database = 'Speech'
    username = 'karan'
    password = '123456789'

    function_name = sys.argv[1]

    try:
        # Create a UserHandler instance and attempt to login
        user_handler = UserHandler(server, database, username, password)
        
        username_input = input("Enter your username: ")
        password_input = input("Enter your password: ")
        
        if user_handler.login_user(username_input, password_input):
            print("Login successful")

            if function_name == "highfrequency":
                high_frequency = HighFrequency(server, database, username, password)
                input_letter = input("Enter the starting letter: ")
                word_list = high_frequency.word_retrieve(input_letter)
                results = high_frequency.recognize_and_write_output(word_list)

                # Insert results into database
                db_handler = DatabaseHandler(server, database, username, password)
                for result in results:
                    db_handler.insert_result(
                        result['high_freq_word'], result['correct_count'], result['incorrect_count'],
                        result['total_attempts'], result['accuracy_rate'], username
                    )
                db_handler.close()
            
            elif function_name == "paragraphread":
                paragraph_handler = ParagraphStoryHandler(server, database, username, password)
                paragraph_retrieves = paragraph_handler.paragraph_retrieve()
                results = paragraph_handler.recognize_and_write_output(paragraph_retrieves)

                db_handler = ReadingResults(server, database, username, password)
                for result in results:
                    # Assuming 'incorrect_word_list' is a string or a type that can be converted to a valid SQL data type
                    incorrect_word_list_str = ','.join(result['incorrect_word_list'])  # Convert list to string if necessary
                    db_handler.insert_data(
                        username, incorrect_word_list_str
                    )
                db_handler.close_connection()

            else:
                print(f"Function '{function_name}' not recognized.")
        else:
            print("Login failed. Please check your username and password.")
        
        user_handler.close()
    
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()


"""


















import sys
from userinfo import UserHandler
from highword_speech_results import DatabaseHandler
from HighFrequencyHandler import HighFrequency
from ParagraphStoryHandler import ParagraphStoryHandler

from paragraph_read_result import ReadingResults

def main():
    if len(sys.argv) != 2:
        print("Usage: python main.py <function_name>")
        return

    server = 'LAPTOP-S1QDCEQ9\\SQLEXPRESS'
    database = 'Speech'
    username = 'karan'
    password = '123456789'

    function_name = sys.argv[1]

    # Create a UserHandler instance and attempt to login
    user_handler = UserHandler(server, database, username, password)
    
    username = input("Enter your username: ")
    password_input = input("Enter your password: ")
    if user_handler.login_user(username, password_input):
        
        if function_name == "highfrequency":
            high_frequency = HighFrequency(server, database, username, password)
            input_letter = input("Enter the starting letter: ")
            word_list = high_frequency.word_retrieve(input_letter)
            results = high_frequency.recognize_and_write_output(word_list)

            # Insert results into database
            db_handler = DatabaseHandler(server, database, username, password)
            for result in results:
                db_handler.insert_result(
                    result['high_freq_word'], result['correct_count'], result['incorrect_count'],
                    result['total_attempts'], result['accuracy_rate'], username
                )
            db_handler.close()
        
        elif function_name == "paragraphread":
            paragraph_handler = ParagraphStoryHandler(server, database, username, password)
            paragraph_retrieves = paragraph_handler.paragraph_retrieve()
            results = paragraph_handler.recognize_and_write_output(paragraph_retrieves)

            db_handler = ReadingResults(server, database, username, password)
            for result in results:
                # Assuming 'incorrect_word_list' is a string or a type that can be converted to a valid SQL data type
                incorrect_word_list_str = ','.join(result['incorrect_word_list'])  # Convert list to string if necessary
                db_handler.insert_data(
                    username, incorrect_word_list_str
                )
            db_handler.close_connection()

        else:
            print(f"Function '{function_name}' not recognized.")
    else:
        print("Login failed. Please check your username and password.")
    user_handler.close()

if __name__ == "__main__":
    main()








