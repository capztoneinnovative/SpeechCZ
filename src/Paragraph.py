import pyttsx3
import speech_recognition as sr
import re


#with wordlist
import pyttsx3
import speech_recognition as sr
import re

class SpeechRecognition:
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
    # this function used to user reading the paragraph
    def speech_to_text(self):
        recognizer = sr.Recognizer()

        while True:
            with sr.Microphone() as source:
                #print("--------Please read the paragraph-----:")
                recognizer.adjust_for_ambient_noise(source)
                audio = recognizer.listen(source)

            try:
                text = recognizer.recognize_google(audio)
                print("You said: ", text)
                return text
            except sr.UnknownValueError:
                pass
                #print("Sorry, Your voice is too low. Please speak loudly and try again.")
            except sr.RequestError as e:
                pass
                #print("Could not request results from Google Speech Recognition service; {0}".format(e))

    def run(self):
        while True:
            spoken_sentence = self.speech_to_text()
            if spoken_sentence:
                wrong_words = self.compare_sentences(spoken_sentence)
                if wrong_words:
                   # showing correct word and spoken words
                    for printed_word, spoken_word in wrong_words:
                        pass
                        #print("Sentence Word:", printed_word, "        Spoken Word:", spoken_word)    
                    # listed all incorrected words
                    wrong_words_list = [word[0] for word in wrong_words]
                    #print("List of wrong words:", wrong_words_list)
                    return wrong_words_list
                    
                    #return wrong_words  # Return the list of wrong words
                
                else:
                    print("You pronounced all words correctly!")
                    return []  # Return an empty list if all words are pronounced correctly