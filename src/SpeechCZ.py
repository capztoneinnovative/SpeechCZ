import os

from DataBase import DataBase
from Split_syllable import Split_syllable
from Paragraph import Paragraph
from logger import logging

from highword_module import HighWord
from paragraph_module import ParagraphStory

class SpeechCZ:
    def __init__(self, connect):
        self.connect = connect

    def highword(self, input_letter):
        highword_instance = HighWord(self.connect, input_letter)
        word_list = highword_instance.retrieve()
        
        speech_to_audio = Split_syllable(word_list)
        speech_to_audio.recognize_speech()

    def paragraph_story(self):
        paragraph_instance = ParagraphStory(self.connect)
        printed_sentence = paragraph_instance.retrieve()
        
        read_paragraph= Paragraph(printed_sentence)
        read_paragraph.speech_to_text()
        read_paragraph.run()
             
def main():
    server = 'LAPTOP-S1QDCEQ9\SQLEXPRESS'
    database = 'Speech'
    username = 'karan'
    password = '123456789'
  
    try:
        db_connector = DataBase(server, database, username, password)
        my_instance = SpeechCZ(db_connector)

        option_functions = {
            1: my_instance.highword,
            2: my_instance.paragraph_story
        }

        option = int(input("Enter the option 1 or 2: "))
        if option in option_functions:
            if option == 1:
                input_letter = input("Enter the starting letter: ")
                option_functions[option](input_letter)
            else:
                option_functions[option]()
        else:
            print("Invalid option")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
