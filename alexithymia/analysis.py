from os.path import dirname, abspath, join
from functools import lru_cache
import json
from emoji import emojize, demojize
from spacy.tokens.doc import Doc
from spacy.matcher import Matcher


def relpath(*paths, dir=dirname(abspath(__file__))):
    return join(dir, *paths)


@lru_cache(maxsize=1)
def get_emojis():
    emojis = relpath('plutchik.json')
    with open(emojis) as f:
        data = json.load(f)
        return data


def label(matcher, doc, i, matches):
    _, start, end = matches[i]
    emoji = doc[start:end].text
    for emotion in get_emojis()[demojize(emoji)]:
        doc._.emotions[emotion] += 1


def recognize_sentiment(nlp, doc: Doc):
    matcher = Matcher(nlp.vocab)
    emoji_list = [k for k, _ in get_emojis().items()]
    emoji_patterns = [[{"ORTH": emojize(e)}] for e in emoji_list]
    matcher.add('EMOJI', emoji_patterns, on_match=label)
    matcher(doc)
