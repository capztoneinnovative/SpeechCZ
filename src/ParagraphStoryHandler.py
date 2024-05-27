from DataBase import DataBase
import os
from paragraph_module import ParagraphStory
from Paragraph import Paragraph

class ParagraphStoryHandler:
    def __init__(self, server, database, username, password):
        self.db_connector = DataBase(server, database, username, password)
        self.highword_instance = ParagraphStory(self.db_connector)
        
    def paragraph_retrieve(self):
        return self.highword_instance.paragraph_retrieve()

    def recognize_and_write_output(self, printed_sentence):
        if printed_sentence:
            read_paragraph = Paragraph(printed_sentence)
            read_paragraph.speech_to_text()
            return read_paragraph.run()
        else:
            print("Failed to retrieve word list.")
            return []

