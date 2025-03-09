from collections import defaultdict
import random 

class Markov_chain:
    def __init__(self):
        self.chain = defaultdict(list)

    def build(self, words):
        
        for i in range(len(words) - 1):
            self.chain[words[i]].append(words[i + 1])

    def generate(self, start_word=None, length=10):

        if not self.chain:
            return "Not found."
        
        if start_word is None or start_word not in self.chain:
            start_word = random.choice(list(self.chain.keys()))

        sentence = [start_word]
        word = start_word

        for _ in range(length - 1):
            next_words = self.chain.get(word, [])
            if not next_words:
                break
            word = random.choice(next_words)
            sentence.append(word)

        return ' '.join(sentence)
    
def read_file(BOOK):
    with open(BOOK, 'r', encoding='utf-8') as file:
        text = file.read()
    return text.split()
        
if __name__ == "__main__":
    words = read_file('book.txt')

    markov = Markov_chain()
    markov.build(words)

    start_word = random.choice(words)
    print(markov.generate(start_word, 20))

    