
import os
import sys
from DataBase import DataBase
from Split_syllable import Split_syllable
from highword_module import HighWord
from paragraph_module import ParagraphStory
from Paragraph import Paragraph
from OutputHandler import OutputHandler
from HighFrequencyHandler import HighFrequency
from ParagraphStoryHandler import ParagraphStoryHandler


def main():
    if len(sys.argv) != 2:
        #print("Usage: python script.py <function_name>")
        return

    server = 'LAPTOP-S1QDCEQ9\SQLEXPRESS'
    database = 'Speech'
    username = 'karan'
    password = '123456789'
    output_dir = 'output'

    output_handler = OutputHandler(output_dir)

    function_name = sys.argv[1]

    if function_name == "highfrequency":
        high_frequency = HighFrequency(server, database, username, password, output_handler)
        input_letter = input("Enter the starting letter: ")
        word_list = high_frequency.word_retrieve(input_letter)
        high_frequency.recognize_and_write_output(word_list)
    elif function_name == "paragraphstory":
        paragraph_story_handler = ParagraphStoryHandler(server, database, username, password, output_handler)
        printed_sentence = paragraph_story_handler.paragraph_retrieve()
        paragraph_story_handler.recognize_and_write_output(printed_sentence)
    else:
        print("Invalid function name.")

if __name__ == "__main__":
    main()








"""
def create_output_directory(directory_name):
    if not os.path.exists(directory_name):
        os.makedirs(directory_name,exist_ok=True)

def highfrequncy(server, database, username, password, output_dir):
    try:
        db_connector = DataBase(server, database, username, password)
        highword_instance = HighWord(db_connector)

        input_letter = input("Enter the starting letter: ")
        word_list = highword_instance.word_retrieve(input_letter)
        if word_list:
            speech_to_audio = Split_syllable(word_list)
            speech_to_audio.recognize_speech()

            # Generate unique output file name
            output_file = os.path.join(output_dir, 'highfrequncy_output.txt')

            # Create output directory if it doesn't exist
            create_output_directory(output_dir)

            # Write output to file
            with open(output_file, 'w') as f:
                f.write(speech_to_audio.output)
        else:
            print("Failed to retrieve word list.")
    except Exception as e:
        print(f"An error occurred: {e}")

def paragraphstory(server, database, username, password, output_dir):
    try:
        db_connector = DataBase(server, database, username, password)
        Paragraph_instance = ParagraphStory(db_connector)
        printed_sentence = Paragraph_instance.paragraph_retrieve()
        if printed_sentence:
            read_paragraph = Paragraph(printed_sentence)
            read_paragraph.speech_to_text()
            read_paragraph.run()

            # Generate unique output file name
            output_file = os.path.join(output_dir, 'paragraphstory_output.txt')

            # Create output directory if it doesn't exist
            create_output_directory(output_dir)

            # Write output to file
            with open(output_file, 'w') as f:
                f.write(read_paragraph.output)
        else:
            print("Failed to retrieve word list.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main(server, database, username, password, output_dir):
    if len(sys.argv) != 2:
        print("Usage: python script.py <function_name>")
        return

    function_name = sys.argv[1]

    if function_name == "highfrequncy":
        highfrequncy(server, database, username, password, output_dir)
    elif function_name == "paragraphstory":
        paragraphstory(server, database, username, password, output_dir)
    else:
        print("Invalid function name.")

if __name__ == "__main__":
    server = 'LAPTOP-S1QDCEQ9\SQLEXPRESS'
    database = 'Speech'
    username = 'karan'
    password = '123456789'
    output_dir = 'output'  # Specify the output directory name here
    create_output_directory(output_dir)  # Ensure output directory exists
    main(server, database, username, password, output_dir)



"""



