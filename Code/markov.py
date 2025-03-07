import random 

class Markov_chain:
    def __init__(self):
        self.chain = {}

    def learn(self, words):
        for i in range(len(words) - 1):
            word, next_word = words[i], words[i + 1]
            if word not in self.chain:
                self.chain[word] = {}
            if next_word not in self.chain[word]:
                self.chain[word][next_word] = 1
            else:
                self.chain[word][next_word] +=1

    def generate(self, start_word, length=10):

        if start_word not in self.chain:
            return "Not found"
        
        result = [start_word]
        current_word = start_word

        for _ in range(length - 1):
            next_words = list(self.chain[current_word].keys())
            probabilities = list(self.chain[current_word].values())
            total = sum(probabilities)
            probabilities = [p / total for p in probabilities]

            current_word = random.choices(next_words, probabilities)[0]
            result.append(current_word)

        return " ".join(result)
    