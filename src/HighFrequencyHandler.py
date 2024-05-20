import os
from DataBase import DataBase
from Split_syllable import Split_syllable
from highword_module import HighWord

class HighFrequency:
    def __init__(self, server, database, username, password):
        self.db_connector = DataBase(server, database, username, password)
        self.highword_instance = HighWord(self.db_connector)

    def word_retrieve(self, input_letter):
        return self.highword_instance.word_retrieve(input_letter)

    def recognize_and_write_output(self, word_list):
        if word_list:
            speech_to_audio = Split_syllable(word_list)
            return speech_to_audio.run()
        else:
            print("Failed to retrieve word list.")
            return []
