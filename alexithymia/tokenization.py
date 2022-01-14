import json, re
from spacy.tokenizer import Tokenizer

def set_greeklish_tokenizer(nlp):
    with open('rsrc/rules/tokenization.json') as f:
        special_cases = json.load(f)

    url_re = re.compile(r'''^https?://''')

    nlp.tokenizer = Tokenizer(nlp.vocab, rules=special_cases,
                                    #  prefix_search=prefix_re.search,
                                    #  suffix_search=suffix_re.search,
                                    #  infix_finditer=infix_re.finditer,
                                     url_match=url_re.match)