import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.corpus import stopwords
import string

# Download NLTK data
nltk.download('punkt')
nltk.download('stopwords')

# Predefined dialog acts and heuristics
dialog_acts = {
    'question': ['what', 'how', 'when', 'where', 'why', 'which', 'who', 'is', 'are', 'can', 'do', '?'],
    'statement': ['i', 'my', 'mine', 'we', 'our', 'ours', 'it', 'they', 'he', 'she', 'you'],
    'request': ['please', 'could', 'would', 'can', 'will'],
    'greeting': ['hello', 'hi', 'hey', 'good morning', 'good afternoon', 'good evening'],
    'goodbye': ['bye', 'goodbye', 'see you', 'take care']
}

# Function to classify dialog acts
def classify_dialog_act(sentence):
    tokens = word_tokenize(sentence.lower())
    for act, keywords in dialog_acts.items():
        for word in tokens:
            if word in keywords or sentence.endswith('?'):
                return act
    return 'statement'

# Function to recognize dialog acts in a conversation
def recognize_dialog_acts(conversation):
    sentences = sent_tokenize(conversation)
    acts = [(sentence, classify_dialog_act(sentence)) for sentence in sentences]
    return acts

# Get input dialog from the user
conversation = input("Enter a conversation: ")

# Recognize dialog acts
recognized_acts = recognize_dialog_acts(conversation)

# Display the results
print("\nRecognized Dialog Acts:")
for sentence, act in recognized_acts:
    print(f"Sentence: {sentence}\nDialog Act: {act}\n")
