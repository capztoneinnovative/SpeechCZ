import re
import speech_recognition as sr  # type: ignore
from datetime import datetime, timedelta
import logging

class Paragraph:
    def __init__(self, printed_sentence_row):
        # Access the actual sentence from the pyodbc.Row object by index
        self.printed_sentence = printed_sentence_row[0]  # Assuming the sentence is the first column
        self.logger = logging.getLogger(__name__)
        self.unknown_error_count = 0
        
    def remove_special_characters(self, text):
        return re.sub(r'[^a-zA-Z0-9]', '', text)

    def compare_sentences(self, spoken_sentence):
        printed_words = self.printed_sentence.lower().split()
        spoken_words = spoken_sentence.lower().split()
        printed_words = [self.remove_special_characters(word) for word in printed_words]
        spoken_words = [self.remove_special_characters(word) for word in spoken_words]
        wrong_words = [(printed_word, spoken_word) for printed_word, spoken_word in zip(printed_words, spoken_words) if printed_word != spoken_word]
        return wrong_words

    def speech_to_text(self, max_duration=60):
        recognizer = sr.Recognizer()
        start_time = datetime.now()
        while (datetime.now() - start_time).total_seconds() <= max_duration:
            with sr.Microphone() as source:
                self.logger.info("Please read the paragraph")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)
            try:
                text = recognizer.recognize_google(audio)
                self.logger.info("You said: %s", text)
                return text
            except sr.UnknownValueError:
                self.unknown_error_count += 1
                if self.unknown_error_count >= 2:
                    self.logger.error("UnknownValueError occurred 2 times. Exiting...")
                    exit()
                self.logger.info("Sorry, Your voice is too low. Please speak loudly and try again.")
            except sr.RequestError as e:
                self.logger.error("Could not request results from Google Speech Recognition service; %s", e)

        self.logger.info("Maximum reading time exceeded. Exiting...")
        exit()

    def run(self):
        results = []
        while True:
            spoken_sentence = self.speech_to_text()
            if spoken_sentence:
                wrong_words = self.compare_sentences(spoken_sentence)
                result = {
                    'incorrect_word_list': [word[0] for word in wrong_words]
                    
                }
                results.append(result)
                
                if wrong_words:
                    self.logger.info("Incorrect pronunciation detected.")
                    for printed_word, spoken_word in wrong_words:
                        self.logger.info("Sentence Word: %s, Spoken Word: %s", printed_word, spoken_word)
                else:
                    self.logger.info("You pronounced all words correctly!")
            break     
        return results

