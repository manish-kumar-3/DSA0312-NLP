import nltk
from nltk.tokenize import word_tokenize

# Download NLTK data if not already downloaded
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

# Get input text from user
text = input("Enter a sentence: ")

# Tokenize the text into words
words = word_tokenize(text)

# Perform POS tagging
pos_tags = nltk.pos_tag(words)

# Print the tagged words
print("POS tagging result:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")
