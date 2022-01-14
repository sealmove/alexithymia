import spacy
from spacy.language import Language

from .stop_words import STOP_WORDS

class GreeklishDefaults(Language.Defaults):
    stop_words = STOP_WORDS

@spacy.registry.languages("greeklish")
class Greeklish(Language):
    lang = "greeklish"
    Defaults = GreeklishDefaults