
import nltk
import random

# Sample tagged corpus
corpus = [
    [('The', 'DET'), ('quick', 'ADJ'), ('brown', 'ADJ'), ('fox', 'NOUN'), ('jumps', 'VERB'), ('over', 'ADP'), ('the', 'DET'), ('lazy', 'ADJ'), ('dog', 'NOUN')],
    [('The', 'DET'), ('brown', 'ADJ'), ('dog', 'NOUN'), ('barks', 'VERB'), ('at', 'ADP'), ('the', 'DET'), ('cat', 'NOUN')],
    [('The', 'DET'), ('cat', 'NOUN'), ('sleeps', 'VERB'), ('peacefully', 'ADV')],
    [('The', 'DET'), ('quick', 'ADJ'), ('brown', 'ADJ'), ('fox', 'NOUN'), ('eats', 'VERB'), ('the', 'DET'), ('rabbit', 'NOUN')],
]

# Calculate transition probabilities
transition_probs = nltk.ConditionalFreqDist()
for sentence in corpus:
    for i in range(len(sentence) - 1):
        current_tag, next_tag = sentence[i][1], sentence[i+1][1]
        transition_probs[current_tag][next_tag] += 1

# Normalize transition probabilities
for current_tag in transition_probs:
    total_count = sum(transition_probs[current_tag].values())
    for next_tag in transition_probs[current_tag]:
        transition_probs[current_tag][next_tag] /= total_count

# Get input text from user
text = input("Enter a sentence: ")
words = nltk.word_tokenize(text)

# Assign POS tags using the stochastic model
pos_tags = []
prev_tag = None
for word in words:
    if prev_tag is None or prev_tag not in transition_probs:
        # Start of sentence or unknown tag
        tag = random.choice(['NOUN', 'VERB', 'ADJ', 'DET', 'ADP', 'ADV'])
    else:
        # Use transition probabilities
        tag = random.choices(list(transition_probs[prev_tag].keys()), list(transition_probs[prev_tag].values()))[0]
    pos_tags.append((word, tag))
    prev_tag = tag

# Print the tagged words
print("Stochastic POS tagging result:")
for word, tag in pos_tags:
    print(f"{word}: {tag}")
