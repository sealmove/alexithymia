from spacy.tokens.doc import Doc
from spacy.matcher import Matcher
import constants


positive_emojis = [[{"ORTH": emoji}] for emoji in constants.positive_emojis]
negative_emojis = [[{"ORTH": emoji}] for emoji in constants.negative_emojis]


def label(matcher, doc, i, matches):
    match_id, start, end = matches[i]
    key = doc.vocab.strings[match_id]
    doc._.emoji_counts[key] += 1


def recognize_sentiment(nlp, doc: Doc):
    matcher = Matcher(nlp.vocab)
    matcher.add('POS', positive_emojis, on_match=label)
    matcher.add('NEG', negative_emojis, on_match=label)
    matches = matcher(doc)
    for match_id, start, end in matches:
        string_id = doc.vocab.strings[match_id]
        span = doc[start:end]
        print(string_id, span.text)
