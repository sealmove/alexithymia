from __future__ import unicode_literals
from spacy.language import Language
from spacy.tokens import Doc
import json, re

@Language.factory('greeklish_to_greek')
def transliterate(nlp: Language, name: str, path: str):
    return Transliterator(nlp, path)

class Transliterator:
    def __init__(self, nlp: Language, path: str):
        self.path = path

    def __call__(self, doc: Doc):
        with open(self.path) as f:
            mappings = json.load(f)
            for token in doc:
                word = token.text
                for k, v in mappings.items():
                    word = re.sub(k, v, word)
                token.norm_ = word

        return doc