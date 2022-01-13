import spacy
from spacy.tokens import Doc
from components.transliterate_spacy import transliterate
from components.hunspell_spacy import hunspell

# Auxiliary pipeline for converting greeklish to proper greek
g2g = spacy.blank('el')

g2g.add_pipe(
    'greeklish_to_greek',
    config={'path': 'rsrc/maps/spellings.json'}
)

g2g.add_pipe(
    'autocorrect',
    config ={'path': ('rsrc/dict/el_GR.dic', 'rsrc/dict/el_GR.aff')}
)

# Main pipeline
nlp = spacy.load('el_core_news_sm')

def feel(message: str):
    doc = g2g(message)

    words, spaces = [], []
    for token in doc:
        words.append(token.norm_)
        spaces.append(token.whitespace_)

    doc = Doc(nlp.vocab, words = words, spaces = spaces)

    for _, proc in nlp.pipeline:
        doc = proc(doc)

    return doc