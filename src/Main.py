import sys
from userinfo import UserHandler
from highword_speech_results import DatabaseHandler
from HighFrequencyHandler import HighFrequency

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
                    result['total_attempts'], result['accuracy_rate'],username
                )
            
            db_handler.close()
        else:
            print(f"Function '{function_name}' not recognized.")
    else:
        print("Login failed. Please check your username and password.")
    user_handler.close()

if __name__ == "__main__":
    main()
