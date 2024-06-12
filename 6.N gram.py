
import random

def create_bigram_model(text):
    words = text.split()
    model = {}
    for i in range(len(words) - 1):
        if words[i] not in model:
            model[words[i]] = []
        model[words[i]].append(words[i + 1])
    return model

def generate_text(model, start_word, num_words):
    current_word = start_word
    text = [current_word]
    for _ in range(num_words - 1):
        if current_word not in model:
            break
        next_word = random.choice(model[current_word])
        text.append(next_word)
        current_word = next_word
    return ' '.join(text)

# Get user input for text
text = input("Enter some text: ")
start_word = input("Enter a starting word: ")
num_words = int(input("Enter the number of words to generate: "))

# Create bigram model
model = create_bigram_model(text)

# Generate text
generated_text = generate_text(model, start_word, num_words)
print("Generated text:", generated_text)
