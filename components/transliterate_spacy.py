from __future__ import unicode_literals
from spacy.language import Language
from spacy.tokens import Doc
import json, re

@Language.component('greeklish_to_greek')
def transliterate(doc: Doc):
    with open('rsrc/mappings.json') as f:
        mappings = json.load(f)
        for token in doc:
            word = token.text
            for k, v in mappings.items():
                word = re.sub(k, v, word)
            token.norm_ = word

    return doc