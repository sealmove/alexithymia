import spacy
from tokenization import customize_tokenizer
import greeklish 

def feel(message: str):
    # TODO: detect language

    # If greeklish
    nlp = spacy.blank("greeklish")
    doc = nlp(message)

    # Regardless the language detected, add custom tokenizer rules
    customize_tokenizer(nlp)

    return doc