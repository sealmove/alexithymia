from hunspell import HunSpell

from spacy.language import Language
from spacy.tokens import Doc

from os.path import dirname, abspath, join

def relpath(*paths, dir=dirname(abspath(__file__))):
    return join(dir, *paths)

@Language.component('autocorrect')
def hunspell(doc):
    dic, aff = relpath('dict', 'el_GR.dic'), relpath('dict', 'el_GR.aff')
    hs = HunSpell(dic, aff)
    for token in doc:
        original = token.norm_
        try:
            if not token.is_punct and not hs.spell(original):
                # Handle first token of sentence in a special way
                if token.is_sent_start:
                    original = original[0].lower() + original[1:]
                    suggestions = hs.suggest(original)
                    if suggestions:
                        token.norm_ = suggestions[0].capitalize()
                else:
                    suggestions = hs.suggest(original)
                    if suggestions:
                        token.norm_ = suggestions[0]
        except UnicodeEncodeError:
            pass

    return doc