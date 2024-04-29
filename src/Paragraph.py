import sys
import pyttsx3  # type: ignore
import speech_recognition as sr  # type: ignore
import re
import logging

from error_handling import CustomException
from logger import logging

class Paragraph:
    def __init__(self, printed_sentence):
        self.printed_sentence = printed_sentence
        self.logger = logging.getLogger(__name__)

    def remove_special_characters(self, text):
        return re.sub(r'[^a-zA-Z0-9]', '', text)

    def compare_sentences(self, spoken_sentence):
        printed_words = self.printed_sentence.lower().split()
        spoken_words = spoken_sentence.lower().split()
        
        printed_words = [self.remove_special_characters(word) for word in printed_words]

        wrong_words = []

        for printed_word, spoken_word in zip(printed_words, spoken_words):
            if printed_word != spoken_word:
                wrong_words.append((printed_word, spoken_word))
        return wrong_words

    def speech_to_text(self):
        recognizer = sr.Recognizer()

        while True:
            with sr.Microphone() as source:
                self.logger.info("Please read the paragraph")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                self.logger.info("You said: %s", text)
                return text
            except sr.UnknownValueError:
                self.logger.info("Sorry, Your voice is too low. Please speak loudly and try again.")
            except sr.RequestError as e:
                self.logger.error("Could not request results from Google Speech Recognition service; %s", e)

    def run(self):
        while True:
            spoken_sentence = self.speech_to_text()
            if spoken_sentence:
                wrong_words = self.compare_sentences(spoken_sentence)
                if wrong_words:
                    self.logger.info("Incorrect pronunciation detected.")
                    for printed_word, spoken_word in wrong_words:
                        self.logger.info("Sentence Word: %s, Spoken Word: %s", printed_word, spoken_word)
                    wrong_words_list = [word[0] for word in wrong_words]
                    return wrong_words_list
                else:
                    self.logger.info("You pronounced all words correctly!")
                    return []
