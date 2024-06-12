import pyttsx3  # type: ignore

class TextToSpeech:
    def __init__(self):
        self.engine = pyttsx3.init()

    def voice_prefixes(self, prefixes):
        for prefix in prefixes:
            prefix_text = f"Prefix: {prefix[0]}, Examples: {prefix[1]}"
            print(prefix_text)
            self.engine.say(prefix_text)
        self.engine.runAndWait()

    def voice_suffixes(self, suffixes):
        for suffix in suffixes:
            suffix_text = f"Suffix: {suffix[0]}, Examples: {suffix[1]}"
            print(suffix_text)
            self.engine.say(suffix_text)
        self.engine.runAndWait()
