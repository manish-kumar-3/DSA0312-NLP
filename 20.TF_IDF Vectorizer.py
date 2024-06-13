import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import nltk

# Download NLTK stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Sample documents
documents = [
    "The cat in the hat.",
    "A quick brown fox jumps over the lazy dog.",
    "The sky is blue and beautiful.",
    "Love this blue and bright sky!",
    "The cat is playing with the dog."
]

# Function to preprocess documents
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return " ".join(filtered_tokens)

# Preprocess the documents
processed_docs = [preprocess(doc) for doc in documents]

# Initialize the TF-IDF Vectorizer
vectorizer = TfidfVectorizer()

# Fit and transform the documents
tfidf_matrix = vectorizer.fit_transform(processed_docs)

# Function to rank documents based on a query
def rank_documents(query):
    query = preprocess(query)
    query_vec = vectorizer.transform([query])
    similarity = cosine_similarity(query_vec, tfidf_matrix).flatten()
    ranked_indices = np.argsort(-similarity)
    return ranked_indices, similarity

# Get the query from the user
query = input("Enter the query: ")

# Rank the documents based on the query
ranked_indices, similarity = rank_documents(query)

# Display the results
print("\nQuery:", query)
print("\nRanked Documents:")
for idx in ranked_indices:
    print(f"Document {idx + 1}: {documents[idx]} (Similarity: {similarity[idx]:.4f})")
