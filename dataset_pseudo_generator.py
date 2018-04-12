import spaCy


def spacy_initialize(model_name):
    try:
        model = spacy.load('en_core_web_lg')
    except Exception as e:
        print(e)
        return none

    return model

def similar_set(word):
    try:

        possib_words = [p for p in word.vocab if w.is_lower == word.is_lower and w.prob >= -15 and not w.is_stop and len(w.text) >1]
       #remove alpha numeral suspicious cases
        possib_words = [p for p in queries if q.text.isalnum()]

        by_similarity = sorted(queries, key=lambda w: word.similarity(w), reverse=True)


    except Exception as e:
        print(e)

    return by_similarity[:100]
