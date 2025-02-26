import random
import sys
import string

# Path to Winnie the Pooh
BOOK = "book.txt"

# Opening BOOK and splitting into words
def histogram():
    try:
        with open(BOOK, "r") as file:
            text = file.read().lower()
            text = text.translate(str.maketrans("", "", string.punctuation))
            words = text.split()

            word_counter = {}
            for word in words:
                word_counter[word] = word_counter.get(word, 0) + 1

            return word_counter
    except FileNotFoundError:
        print(f"Error: '{BOOK}' was not found.")
        sys.exit(1)

def unique_words(histogram):
    return len(histogram)

hist = histogram()
print(f"Total unique words: {unique_words(hist)}")

def frequency(word, histogram):
    word = word.lower()
    return histogram.get(word, 0)

hist = histogram()

for word, count in hist.items():
    print(f"{word} {count}")

user_input = input("Enter a word: ")
print(f"The word '{user_input}' appears {frequency(user_input, hist)} times.")

def random_word(histogram):
    words = list(histogram.keys())  # Get a list of words
    return random.choice(words)