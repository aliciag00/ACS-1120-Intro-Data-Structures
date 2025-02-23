import sys
import random

# Path to word file from tutorial
WORDS_FILE = "/usr/share/dict/words"

# Opening file, singling out words
def read_words():
    """Reads the system's words file and returns a list of words."""
    try:
        with open(WORDS_FILE, "r") as file:
            words = file.read().splitlines()
            return words
    except FileNotFoundError:
        print(f"Error: The file '{WORDS_FILE}' was not found.")
        sys.exit(1)


def generate_dictionary_words(word_list, num_words): 
    """Randomly selects num_words from word_list."""
    num_words = min(num_words, len(word_list))
    return " ".join(random.sample(word_list, num_words))

if __name__ == "__main__":

    if len(sys.argv) != 2 or not sys.argv[1].isdigit():
        print("Usage: python dictionary_words.py <number_of_words>")
        sys.exit(1)

    num_words = int(sys.argv[1])
    words = read_words()
    sentence = generate_dictionary_words(words, num_words)
    print(sentence)   