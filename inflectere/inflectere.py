

class Inflectere:

    def __init__(self):
        self.vowels = "aeiou"
        self.consonants = "bcdfghjklmnpqrstvwxyz"
        self.letters = self.vowels + self.consonants

    def singularize(self, word):
        raise NotImplementedError

    def pluralize(self, word):
        raise NotImplementedError

    def is_singular(self):
        raise NotImplementedError

    def is_plural(self):
        raise NotImplementedError

