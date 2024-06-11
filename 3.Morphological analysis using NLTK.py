
import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

def analyze(text, stemming=True, lemmatization=True):
  """Analyzes text with stemming/lemmatization (optional)."""
  tokens = nltk.word_tokenize(text)
  results = {"original_text": text}
  if stemming:
    stemmer = PorterStemmer()
    results["stemmed_text"] = " ".join([stemmer.stem(t) for t in tokens])
  if lemmatization:
    lemmatizer = WordNetLemmatizer()
    results["lemmatized_text"] = " ".join([lemmatizer.lemmatize(t) for t in tokens])
  return results

def main():
  while True:
    user_input = input("Enter a sentence (or 'q' to quit): ")
    if user_input.lower() == 'q':
      break
    analysis = analyze(user_input)
    print("Original Text:", analysis["original_text"])
    if "stemmed_text" in analysis:
      print("Stemmed Text:", analysis["stemmed_text"])
    if "lemmatized_text" in analysis:
      print("Lemmatized Text:", analysis["lemmatized_text"])
    print("---")

if __name__ == "__main__":
  main()
