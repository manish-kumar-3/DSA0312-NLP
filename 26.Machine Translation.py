from transformers import MarianMTModel, MarianTokenizer

# Load the pre-trained MarianMT model and tokenizer for English to French translation
model_name = 'Helsinki-NLP/opus-mt-en-fr'
tokenizer = MarianTokenizer.from_pretrained(model_name)
model = MarianMTModel.from_pretrained(model_name)

def translate(text, src_lang="en", tgt_lang="fr"):
    # Tokenize the input text
    inputs = tokenizer(text, return_tensors="pt", padding=True)
    
    # Perform the translation and decode the output
    translated = model.generate(**inputs)
    translated_text = tokenizer.batch_decode(translated, skip_special_tokens=True)
    
    return translated_text[0]

# Get input text from the user
text = input("Enter text to translate from English to French: ")

# Translate the text
translated_text = translate(text)

# Display the results
print("\nTranslated Text:")
print(translated_text)
