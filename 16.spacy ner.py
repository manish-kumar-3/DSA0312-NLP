import spacy

# Load the pre-trained English model
nlp = spacy.load("en_core_web_sm")

# Get input text from the user
text = input("Enter the text for Named Entity Recognition: ")

# Process the text with SpaCy to create a Doc object
doc = nlp(text)

# Extract and display named entities
print(f"{'Entity':<20} {'Label':<10} {'Description':<30}")
print("="*60)
for ent in doc.ents:
    print(f"{ent.text:<20} {ent.label_:<10} {spacy.explain(ent.label_):<30}")

# Optionally, visualize named entities using SpaCy's displaCy
from spacy import displacy

# Render the text with named entities highlighted
displacy.render(doc, style="ent", jupyter=True)
