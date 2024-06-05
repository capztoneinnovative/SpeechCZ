import pyttsx3  # type: ignore

# Text-to-speech handling class
class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def voice_suffixes(self, suffixes):
        for suffix in suffixes:
            suffix_text = f"Suffix: {suffix[0]}, Examples: {suffix[1]}"
            print(suffix_text)
            self.engine.say(suffix_text)
        self.engine.runAndWait()
