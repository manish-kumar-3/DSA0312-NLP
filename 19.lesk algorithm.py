import nltk
from nltk.corpus import wordnet as wn
from nltk.tokenize import word_tokenize
from collections import Counter

# Function to get the definition of a synset as a set of words
def get_gloss_set(synset):
    gloss = synset.definition()
    examples = ' '.join(synset.examples())
    return set(word_tokenize(gloss + ' ' + examples))

# Function to perform Lesk algorithm
def lesk_algorithm(context_sentence, ambiguous_word):
    max_overlap = 0
    best_sense = None
    context = set(word_tokenize(context_sentence))
    
    for synset in wn.synsets(ambiguous_word):
        gloss_set = get_gloss_set(synset)
        overlap = len(context.intersection(gloss_set))
        
        if overlap > max_overlap:
            max_overlap = overlap
            best_sense = synset
            
    return best_sense

# Example usage
if __name__ == "__main__":
    sentence = "I went to the bank to deposit some money."
    ambiguous_word = "bank"
    
    best_sense = lesk_algorithm(sentence, ambiguous_word)
    
    if best_sense:
        print(f"Best sense: {best_sense.name()}")
        print(f"Definition: {best_sense.definition()}")
    else:
        print("No sense found")

# Interactive input from user
    context_sentence = input("Enter a sentence: ")
    ambiguous_word = input("Enter the word to disambiguate: ")
    
    best_sense = lesk_algorithm(context_sentence, ambiguous_word)
    
    if best_sense:
        print(f"Best sense: {best_sense.name()}")
        print(f"Definition: {best_sense.definition()}")
    else:
        print("No sense found")
