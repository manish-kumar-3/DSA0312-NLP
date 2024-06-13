import spacy

# Load the pre-trained English model
nlp = spacy.load("en_core_web_sm")

# Function to extract noun phrases and their meanings
def extract_noun_phrases(sentence):
    doc = nlp(sentence)
    noun_phrases = [(chunk.text, chunk.root.head.text) for chunk in doc.noun_chunks]
    return noun_phrases

# Get input sentence from the user
sentence = input("Enter a sentence: ")

# Extract noun phrases and their meanings
noun_phrases = extract_noun_phrases(sentence)

# Display the results
print("\nNoun Phrases and their meanings:")
for np, meaning in noun_phrases:
    print(f"Noun Phrase: {np}, Head: {meaning}")
