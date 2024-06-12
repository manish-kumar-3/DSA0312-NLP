import nltk
from nltk.corpus import wordnet


# Function to get synsets and definitions of a word
def get_word_synsets(word):
    synsets = wordnet.synsets(word)
    if synsets:
        print(f"Synsets for '{word}':")
        for synset in synsets:
            print(f" - {synset.name()}: {synset.definition()}")
    else:
        print(f"No synsets found for '{word}'.")

# Get user input
user_input = input("Enter a word to explore its meanings: ")
get_word_synsets(user_input)
