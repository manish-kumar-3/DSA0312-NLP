import nltk
import gensim
from gensim import corpora
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from gensim.models.coherencemodel import CoherenceModel

# Download NLTK stopwords
nltk.download('stopwords')
nltk.download('punkt')

# Function to preprocess text
def preprocess(text):
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    filtered_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return filtered_tokens

# Function to evaluate coherence of a text
def evaluate_coherence(text):
    # Split text into sentences
    sentences = nltk.sent_tokenize(text)
    
    # Preprocess each sentence
    processed_sentences = [preprocess(sentence) for sentence in sentences]
    
    # Create a dictionary and corpus for topic modeling
    dictionary = corpora.Dictionary(processed_sentences)
    corpus = [dictionary.doc2bow(sentence) for sentence in processed_sentences]
    
    # Train an LDA model
    lda_model = gensim.models.ldamodel.LdaModel(corpus, num_topics=5, id2word=dictionary, passes=15)
    
    # Compute coherence score
    coherence_model_lda = CoherenceModel(model=lda_model, texts=processed_sentences, dictionary=dictionary, coherence='c_v')
    coherence_score = coherence_model_lda.get_coherence()
    
    return coherence_score

# Get input text from the user
text = input("Enter a text: ")

# Evaluate coherence
coherence_score = evaluate_coherence(text)

# Display the results
print("\nCoherence Score:")
print(coherence_score)
