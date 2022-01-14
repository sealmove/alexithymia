from spacy.language import Language

from os.path import dirname, abspath, join
import json, re

def relpath(*paths, dir=dirname(abspath(__file__))):
    return join(dir, *paths)

@Language.component('greeklish_to_greek')
def transliterate(doc):
    mappings = relpath('greeklish.json')
    with open(mappings) as f:
        mappings = json.load(f)
        for token in doc:
            word = token.text
            for k, v in mappings.items():
                word = re.sub(k, v, word)
            token.norm_ = word

        return doc