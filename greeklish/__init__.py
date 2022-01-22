import spacy
from spacy.util import update_exc
from spacy.language import Language
from spacy.lang.tokenizer_exceptions import BASE_EXCEPTIONS

from .tokenizer_exceptions import TOKENIZER_EXCEPTIONS
from .stop_words import STOP_WORDS

class GreeklishDefaults(Language.Defaults):
    stop_words = STOP_WORDS
    tokenizer_exceptions = update_exc(BASE_EXCEPTIONS, TOKENIZER_EXCEPTIONS)

@spacy.registry.languages("greeklish")
class Greeklish(Language):
    lang = "greeklish"
    Defaults = GreeklishDefaults