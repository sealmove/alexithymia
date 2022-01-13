from __future__ import unicode_literals
from spacy.language import Language
from spacy.tokens import Doc
from hunspell import HunSpell

@Language.factory('autocorrect')
def hunspell(nlp: Language, name: str, path: tuple[str, str]):
    return SpaCyHunSpell(nlp, path)

class SpaCyHunSpell:
    def __init__(self, nlp: Language, path: tuple[str, str]):
        dic_path, aff_path = path
        self.hobj = HunSpell(dic_path, aff_path)

    def __call__(self, doc: Doc):
        for token in doc:
            original = token.norm_
            try:
                if not self.hobj.spell(original):
                    suggestions = self.hobj.suggest(original)
                    if suggestions:
                        token.norm_ = suggestions[0]
            except UnicodeEncodeError:
                pass
        return doc