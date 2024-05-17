import speech_recognition as sr         # type: ignore  
from error_handling import CustomException
from hyphen import Hyphenator           # type: ignore  
from eng_to_ipa import ipa_list         # type: ignore  
from highword_speech_results import DatabaseHandler

class SplitSyllableApp:
    def __init__(self, word_list, highword_speech_results):
        self.word_list = word_list
        self.db_handler = highword_speech_results
        self.recognizer = sr.Recognizer()
        self.hyphenator = Hyphenator('en_US')

    def recognize_speech(self, word):
        with sr.Microphone() as source:
            self.recognizer.adjust_for_ambient_noise(source)
            print("Please say the word:", word)
            audio = self.recognizer.listen(source)
            try:
                voice = self.recognizer.recognize_google(audio)
                print("You said:", voice)
                return voice.lower()
            except Exception as e:
                raise CustomException(e)

    def print_syllables(self, word):
        syllables = self.hyphenator.syllables(word)
        pronunciation = ipa_list(word)[0]
        return syllables, pronunciation

    def run(self):
        for word in self.word_list:
            correct_count = 0
            incorrect_count = 0
            total_attempts = 0

            while total_attempts < 5:
                try:
                    voice = self.recognize_speech(word)
                    if voice == word.lower():
                        correct_count += 1
                        print("Correct word pronunciation!")
                        break
                    else:
                        incorrect_count += 1
                        syllables, pronunciation = self.print_syllables(word)
                        print(f"Syllables: {syllables}")
                        print(f"Pronunciation: {pronunciation}")
                except CustomException as e:
                    print("Your voice is too low, speak loudly:", str(e))
                finally:
                    total_attempts += 1

            accuracy_rate = correct_count / total_attempts if total_attempts > 0 else 0
            self.db_handler.insert_result(word, correct_count, incorrect_count, total_attempts, accuracy_rate)

        self.highword_speech_results.close()



"""
import speech_recognition as sr # type: ignore
from hyphen import Hyphenator # type: ignore
from eng_to_ipa import ipa_list # type: ignore

import sys
from error_handling import CustomException
from logger import logging

class Split_syllable:
    def __init__(self, word_list, output_handler):
        self.recognizer = sr.Recognizer()
        self.word_list = word_list
        self.hyphenator = Hyphenator('en_US')
        self.output_handler = output_handler
        self.output = ""

    def recognize_speech(self):
        for word in self.word_list:
            pronoun_attempts = 0
            exception_attempts = 0
            while pronoun_attempts < 5:
                with sr.Microphone() as source:
                    self.recognizer.adjust_for_ambient_noise(source)
                    print("Please say the word:", word)
                    audio = self.recognizer.listen(source)
                    try:
                        voice = self.recognizer.recognize_google(audio)
                        print("You said:", voice)
                        self.output += f"You said: {voice}\n"
                        if voice.lower() == word.lower():
                            print("Correct word pronunciation!")
                            self.output += "Correct word pronunciation!\n"
                            break 
                        else:
                            pronoun_attempts += 1
                            self.print_syllables(word)
                            if pronoun_attempts >= 3:
                                break
                    except Exception as e:
                        exception_attempts += 1
                        raise CustomException(e, sys)
                        print("Your Voice too low speak loadly:", str(e))
                        self.output += f"Your Voice too low speak loadly: {str(e)}\n"
                    if exception_attempts >= 3:
                        print("Maximum exception attempts reached for this word.")
                        self.output += "Maximum exception attempts reached for this word.\n"

    def print_syllables(self, word):
        syllables = self.hyphenator.syllables(word)
        pronunciation = ipa_list(word)[0]
        self.output += f"Syllables: {syllables}\n"
        self.output += f"Pronunciation: {pronunciation}\n"
"""

"""
class Split_syllable:
    def __init__(self, word_list):
        self.recognizer = sr.Recognizer()
        self.word_list = word_list
        self.hyphenator = Hyphenator('en_US')

    def recognize_speech(self):
        for word in self.word_list:
            pronoun_attempts = 0
            exception_attempts = 0
            while pronoun_attempts < 5:
                with sr.Microphone() as source:
                    self.recognizer.adjust_for_ambient_noise(source)
                    print("Please say the word:", word)
                    audio = self.recognizer.listen(source)
                    try:
                        voice = self.recognizer.recognize_google(audio)
                        print("You said:", voice)
                        if voice.lower() == word.lower():
                            print("Correct word pronunciation!")
                            break 
                        else:
                            pronoun_attempts += 1
                            print("Incorrect pronunciation.Maximum Attempt 5. Your Pronunciation attempt:", pronoun_attempts)
                            self.print_syllables(word)
                            if pronoun_attempts >= 3:
                                print("Maximum pronunciation attempts reached for this word.")
                                break
                    except Exception as e:
                        exception_attempts += 1
                        print("Your Voice too low speak loadly:", str(e))
                        if exception_attempts >= 3:
                            print("Maximum exception attempts reached for this word.")
                            break
        # syllable split and correct pronunciation show 
    def print_syllables(self, word):
        syllables = self.hyphenator.syllables(word)
        pronunciation = ipa_list(word)[0]
        print("Syllables:", syllables)
        print("Pronunciation:", pronunciation)
"""