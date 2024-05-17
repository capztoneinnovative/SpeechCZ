from DataBase import DataBase
import os
from paragraph_module import ParagraphStory
from Paragraph import Paragraph

class ParagraphStoryHandler:
    def __init__(self, server, database, username, password, output_handler):
        self.server = server
        self.database = database
        self.username = username
        self.password = password
        self.output_handler = output_handler

    def paragraph_retrieve(self):
        db_connector = DataBase(self.server, self.database, self.username, self.password)
        Paragraph_instance = ParagraphStory(db_connector)
        return Paragraph_instance.paragraph_retrieve()

    def recognize_and_write_output(self, printed_sentence):
        if printed_sentence:
            read_paragraph = Paragraph(printed_sentence,self.output_handler)
            read_paragraph.speech_to_text()
            read_paragraph.run()
            output_file = os.path.join(self.output_handler.output_dir, 'paragraphstory_output.txt')
            self.output_handler.write_to_file(output_file, read_paragraph.output)
        else:
            print("Failed to retrieve word list.")
