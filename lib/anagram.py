class Anagram:
    def __init__(self, word):
        self.word = word
    
    def match(self, words):
        self.words = words

        return [e for e in self.words if sorted(self.word) == sorted(e)]
    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana']))