import random

"""Word Finder: finds random words from a dictionary."""


class WordFinder:
    def __init__(self, filePath):
        '''Reads a dictionary and reports number of words'''

        dict_file = open(filePath)
        self.words = self.parse(self.parse(dict_file))
        print(f"{len(self.words)} words read")

    def parse(self, dict_file):
        '''Goes through each line of .txt and returns list of each word'''
        
        return [word.strip() for word in dict_file]
    
    def random(self):
        '''Returns random word using 'random` library'''

        return self.words[random.randint(0, len(self.words) - 1)]
    
