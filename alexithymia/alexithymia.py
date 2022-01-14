import spacy
import tokenization

def feel(message: str):
    nlp = spacy.blank("en")
    tokenization.set_greeklish_tokenizer(nlp)

    doc = nlp(message)

    return doc