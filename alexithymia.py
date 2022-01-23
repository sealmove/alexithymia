import spacy
from spacy.tokens import Doc
from tokenization import customize_tokenizer
from analysis import recognize_sentiment
import greeklish


DEFAULT_EMOTIONS = dict(joy=0, trust=0, fear=0, surprise=0,
                            sadness=0, disgust=0, anger=0, anticipation=0)

                  
def score(emotions: dict) -> dict:
    '''Assigns a score to each emotion based on all extracted information.

    The score is a decimal number in range [0, 3] corresponding to the levels
    of Plutchik's Wheel of Emotions model.
    '''

    def evaluate(x):
        return float(min(x, 3))

    return {emotion: evaluate(count) for emotion, count in emotions.items()}


def feel(message: str) -> dict:
    # TODO: detect language

    # If greeklish
    nlp = spacy.blank("greeklish")
    doc = nlp(message)

    # Regardless the language detected, add custom tokenizer rules
    customize_tokenizer(nlp)

    # Extract emotions from emojis
    Doc.set_extension("emotions", default=DEFAULT_EMOTIONS)
    recognize_sentiment(nlp, doc)

    return score(doc._.emotions)
