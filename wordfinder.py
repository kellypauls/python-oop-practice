"""Word Finder: finds random words from a dictionary."""
import random

class WordFinder:
    """class to find randomg words from a dictionary"""

    def __init__(self, file):
       """reading the file and returning number of words in file"""
       dict_file = open(file)
       self.words = self.parse(dict_file)
       print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        """turning items in dict_file into list of words"""
        return [word.strip() for word in dict_file]
    
    def random(self):
        """randomizing word to be returned"""
        return random.choice(self.words)
    

class SpecialWordFinder(WordFinder):
    """sub class to find only words that excludes blank lines or comments"""

    def parse(self, dict_file):
        return [word.strip() for word in dict_file
                if word.strip() and not word.startswith("#")]
