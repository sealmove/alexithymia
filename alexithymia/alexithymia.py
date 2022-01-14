import spacy

def feel(message: str):
    # TODO: detect language

    # If greeklish
    nlp = spacy.blank("greeklish")
    doc = nlp(message)
    return doc