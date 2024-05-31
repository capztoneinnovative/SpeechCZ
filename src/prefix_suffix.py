
# word_decomposer.py
from prefix_suffix_db import DatabaseLoader

class WordDecomposer:
    def __init__(self, database_loader):
        self.prefixes = database_loader.get_prefixes()
        self.suffixes = database_loader.get_suffixes()
        self.roots = database_loader.get_roots()

    def remove_suffix(self, word):
        for suffix in self.suffixes:
            if word.endswith(suffix):
                base = word[:-len(suffix)]
                return base, suffix
        return word, None

    def remove_prefix(self, word):
        for prefix in self.prefixes:
            if word.startswith(prefix):
                base = word[len(prefix):]
                return prefix, base
        return None, word

    def decompose_word(self, word):
        prefix, base_word = self.remove_prefix(word)
        base_word, suffix = self.remove_suffix(base_word)
        return prefix, base_word, suffix

    def explain_word(self, word):
        prefix, root, suffix = self.decompose_word(word)
        explanation = f"The word '{word}' is composed of:\n"
        if prefix:
            explanation += f"  Prefix: '{prefix}'\n"
        explanation += f"  Root: '{root}'\n"
        if suffix:
            explanation += f"  Suffix: '{suffix}'\n"
        return explanation


