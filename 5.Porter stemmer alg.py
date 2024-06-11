from nltk.stem import PorterStemmer

def stem_word(word):
  """Stems a word using the Porter Stemmer."""
  stemmer = PorterStemmer()
  return stemmer.stem(word)

# Example usage with user input
while True:
  user_input = input("Enter a word (or 'q' to quit): ")
  if user_input.lower() == 'q':
    break
  stemmed_word = stem_word(user_input)
  print(f"Original: {user_input} - Stemmed: {stemmed_word}")
