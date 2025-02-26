"""Main script, uses other modules to generate sentences."""
from flask import Flask
import random
import re
import os

app = Flask(__name__)

def create_sentences():
    try:
        with open("book.txt", "r", encoding="utf-8") as file:
            text = file.read()
            sentences = re.split(r'(?<=[.!?])\s+', text)
            return sentences
    except FileNotFoundError:
        return ["Error: book not found."]
    
sentences = create_sentences()

# TODO: Initialize your histogram, hash table, or markov chain here.
# Any code placed here will run only once, when the server starts.


@app.route("/")
def home():
    """Route that returns a web page containing the generated text."""
    random_sentence = random.choice(sentences) if sentences else "No sentences created."
    return f"<h1>{random_sentence}</h1>"
# todo: Return a word here!</p>"


if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))  # Default to 5000 if PORT is not set
    app.run(host="0.0.0.0", port=port)
