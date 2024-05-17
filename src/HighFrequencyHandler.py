import os
from DataBase import DataBase
from Split_syllable import Split_syllable
from highword_module import HighWord


class HighFrequency:
    def __init__(self, server, database, username, password):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        #self.output_handler = output_handler

    def word_retrieve(self, input_letter):
        db_connector = DataBase(self.server, self.database, self.username, self.password)
        highword_instance = HighWord(db_connector)
        return highword_instance.word_retrieve(input_letter)

    def recognize_and_write_output(self, word_list):
        if word_list:
            speech_to_audio = Split_syllable(word_list)
            speech_to_audio.recognize_speech()
            
            #output_file = os.path.join(self.output_handler.output_dir, 'highfrequency_output.txt')
            #elf.output_handler.write_to_file(output_file, speech_to_audio.output)
        else:
            print("Failed to retrieve word list.")
