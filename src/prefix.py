from error_handling import CustomException
from logger import logging

class PrefixApplication:
    def __init__(self, db_manager, tts):
        self.db_manager = db_manager
        self.tts = tts

    def run(self):
        try:
            random_prefixes = self.db_manager.retrieve_random_prefix()
            self.tts.voice_prefixes(random_prefixes)
        except CustomException as e:
            logging.error(f"An error occurred: {e}")
        finally:
            self.db_manager.close()
