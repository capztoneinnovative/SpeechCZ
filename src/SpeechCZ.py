

from Split_syllable import Split_syllable
from Paragraph import Paragraph
from highword_module import HighWord
from paragraph_module import ParagraphStory
from logger import logging

class SpeechCZ:
    def __init__(self, connection):
        self.connection = connection
        

    def highword_instance(self, input_letter):
        highword_instance = HighWord(self.connection, input_letter)
        word_list = highword_instance.word_retrieve()
        logging.info("List of word based on you seareched letter:")
        
        speech_to_audio = Split_syllable(word_list)
        speech_to_audio.recognize_speech()

    def paragraph_instance(self):
        paragraph_instance = ParagraphStory(self.connection)
        printed_sentence = paragraph_instance.paragraph_retrieve()
        logging.info("This is a story you should read:")
        
        read_paragraph = Paragraph(printed_sentence)
        read_paragraph.speech_to_text()
        read_paragraph.run()


