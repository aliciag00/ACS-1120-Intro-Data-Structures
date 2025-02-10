import sys
import random

def rearrange_words(words):
    random.shuffle(words)
    return " ".join(words)

if __name__ == "__main__":
    words = sys.argv[1:]

    if not words:
        print("Usage: python rearrange.py <word1> <word2> <word3> ...")
    else:
        print(rearrange_words(words))
            
