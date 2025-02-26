import random

phrase = ['one', 'dog', 'two', 'dog', 'big', 'dog', 'small', 'dog']
def sample(words):
    index = random.randint(0, len(words)-1)
    return words[index]

print(sample(phrase))

text = 'one dog two dog big dog small dog'

word_counts = {'one': 1, 'dog': 4, 'two':1, 'big': 1, 'small': 1}

def sample_by_frequency(histogram):
    total = sum(histogram.values())
    random_value = random.randint(1, total)

    cumulative_count = 0
    for word, count in histogram.items():
        cumulative_count +=count
        if cumulative_count >= random_value:
            return word
        
selected_word = sample_by_frequency(word_counts)
print(f"{selected_word}")


