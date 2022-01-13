from __future__ import unicode_literals
from spacy.language import Language
from spacy.tokens import Doc
from transliterate import translit

@Language.component('greeklish_to_greek')
def transliterate(doc: Doc):
    for token in doc:
        try:
            token.norm_ = translit(token.text, 'el')
        except UnicodeEncodeError:
            pass

    return doc