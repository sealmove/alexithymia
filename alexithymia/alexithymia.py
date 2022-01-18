import spacy
from spacy.tokens import Doc

from tokenization import customize_tokenizer
from analysis import recognize_sentiment
import greeklish


def feel(message: str):
    # TODO: detect language

    # If greeklish
    nlp = spacy.blank("greeklish")
    doc = nlp(message)

    # Regardless the language detected, add custom tokenizer rules
    customize_tokenizer(nlp)

    Doc.set_extension("emoji_counts", default=dict(POS=0, NEG=0))
    recognize_sentiment(nlp, doc)

    print(doc._.emoji_counts)

    return doc
