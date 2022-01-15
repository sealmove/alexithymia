import spacy

extra_suffixes = [

]

special_cases = {

}

def customize_tokenizer(nlp):
    # Suffixes
    suffixes = nlp.Defaults.suffixes + extra_suffixes
    suffix_regex = spacy.util.compile_suffix_regex(suffixes)
    nlp.tokenizer.suffix_search = suffix_regex.search

    # Special cases
    nlp.tokenizer.rules.update(special_cases)