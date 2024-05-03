

from Split_syllable import Split_syllable
from Paragraph import Paragraph
from logger import logging
#from error_handling import CustomException

from highword_module import HighWord
from paragraph_module import ParagraphStory

class SpeechCZ:
    def __init__(self, connect):
        self.connect = connect

    def highword(self, input_letter):
        highword_instance = HighWord(self.connect, input_letter)
        word_list = highword_instance.word_retrieve()
        logging.info("List of word based on you seareched letter:")
        
        speech_to_audio = Split_syllable(word_list)
        speech_to_audio.recognize_speech()

    def paragraph_story(self):
        paragraph_instance = ParagraphStory(self.connect)
        printed_sentence = paragraph_instance.retrieve()
        logging.info("This is a story you should read:")
        
        read_paragraph= Paragraph(printed_sentence)
        read_paragraph.speech_to_text()
        read_paragraph.run()
    
