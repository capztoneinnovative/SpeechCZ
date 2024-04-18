import pyttsx3
import speech_recognition as sr
import re


class Paragraph_Reading:
    def __init__(self, printed_sentence):
        self.printed_sentence = printed_sentence

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
                print("--------Please read the paragraph-----:")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                print("You said: ", text)
                return text
            except sr.UnknownValueError:
                print("Sorry, Your voice is too low. Please speak loudly and try again.")
            except sr.RequestError as e:
                print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def run(self):
        while True:
            spoken_sentence = self.speech_to_text()
            if spoken_sentence:
                wrong_words = self.compare_sentences(spoken_sentence)
                if wrong_words:
                    print("You pronounced the following words incorrectly:")
                    for printed_word, spoken_word in wrong_words:
                        print("Sentence Word:", printed_word, "        Spoken Word:", spoken_word)
                    if len(wrong_words) > 10:
                        print("You pronounced more than 10 words incorrectly. Please try again.")
                    else:
                        break  
                else:
                    print("You pronounced all words correctly!")
                    break  
