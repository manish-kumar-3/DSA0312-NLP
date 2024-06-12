
import re

# Define rules for each POS tag using regular expressions
pos_rules = {
    'NOUN': r'\b(?:cat|dog|rabbit|fox|quick|brown|lazy)\b',
    'VERB': r'\b(?:jumps|barks|sleeps|eats)\b',
    'ADJ': r'\b(?:quick|brown|lazy)\b',
    'DET': r'\b(?:The|the|a)\b',
    'ADP': r'\b(?:over|at)\b',
    'ADV': r'\b(?:peacefully)\b'
}

# Get input text from user
text = input("Enter a sentence: ")

# Tokenize the input text into words
words = text.split()

# Initialize a list to store the tagged words
pos_tags = []

# Iterate over each word and apply POS tagging based on rules
for word in words:
    for pos, rule in pos_rules.items():
        if re.match(rule, word):
            pos_tags.append((word, pos))
            break
    else:
        # If no rule matches, assign 'UNK' (unknown) tag
        pos_tags.append((word, 'UNK'))

# Print the tagged words
print("Rule-based POS tagging result:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")
