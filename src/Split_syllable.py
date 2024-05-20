# split_syllable.py
import speech_recognition as sr  # type: ignore
from hyphen import Hyphenator  # type: ignore
from eng_to_ipa import ipa_list  # type: ignore
from error_handling import CustomException

class Split_syllable:
    def __init__(self, word_list):
        self.word_list = word_list
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
        results = []
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
            results.append({
                'high_freq_word': word,
                'correct_count': correct_count,
                'incorrect_count': incorrect_count,
                'total_attempts': total_attempts,
                'accuracy_rate': accuracy_rate
            })
        return results

