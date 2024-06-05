import pyttsx3  # type: ignore

# Text-to-speech handling class
class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def voice_prefixes(self, prefixes):
        for prefix in prefixes:
            prefix_text = f"Prefix: {prefix[0]}, Examples: {prefix[1]}"
            print(prefix_text)
            self.engine.say(prefix_text)
        self.engine.runAndWait()
