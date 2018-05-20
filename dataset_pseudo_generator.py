import spacy
import gensim


def spacy_initialize(model_name):
    try:
        model = spacy.load(model_name)
    except Exception as e:
        print(e)
        return None

    return model


def gensim_initialize(model_name):
    #todo
    try:

        model = spacy.load('en_core_web_lg')
    except Exception as e:
        print(e)
        return None

    return model


def similar_set_spacy(word, max_similar_amount=100):
    try:

        possible_words = [w for w in word.vocab if w.is_lower == word.is_lower and w.prob >= -20 and not w.is_stop and len(w.text) >1]

        #remove alpha numeral suspicious cases
        possible_words = set([p for p in possible_words if p.text.isalnum()])
        by_similarity = sorted(possible_words, key=lambda w: word.similarity(w), reverse=True)

    except Exception as e:
        print(e)

    return by_similarity[:max_similar_amount]
