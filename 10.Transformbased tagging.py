
import nltk

# Define transformation rules
transformation_rules = {
    'NOUN': [('s', 'NOUN'), ('ly', 'ADV')],
    'VERB': [('ed', 'VERB'), ('ing', 'VERB')],
    'ADJ': [('est', 'ADJ'), ('er', 'ADJ')],
}

# Get input text from user
text = input("Enter a sentence: ")

# Tokenize the input text into words
words = nltk.word_tokenize(text)

# Initialize a list to store the tagged words
pos_tags = []

# Iterate over each word and apply transformation rules
for word in words:
    # Apply rules for each POS tag
    for tag, rules in transformation_rules.items():
        for suffix, new_tag in rules:
            if word.endswith(suffix):
                pos_tags.append((word, new_tag))
                break
        else:
            continue
        break
    else:
        # If no rule matches, assign 'UNK' (unknown) tag
        pos_tags.append((word, 'UNK'))

# Print the tagged words
print("Transformation-based tagging result:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")
