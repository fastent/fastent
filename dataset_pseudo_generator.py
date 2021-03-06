import spacy
import gensim
import traceback
import argparse
import random
from .text_utils import fuzzy_word_remove
from .fast_utils import log_to_text

def spacy_initialize(model_name):
    """
    Initialize a spacy model with name

    Args:
        model_name (str): The designated model name
    Returns:
        model (spacy model object): spacy model
    """
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


def similar_set_spacy(model, word_list, max_similar_amount=100):
    """
    Return the List of similar words using the spacy model and suggested word_list

    Args:
        model (spacy model object): The spacy model
        word_list (list): The list of suggestive words
        max_similar_amount (int): The maximum number of words to look for

    Returns:
        dataset (list): list of similar words
    """
    try:

        similarities = []
        for base_word in word_list:
            word = model.vocab[base_word]
            possible_words = [w for w in word.vocab if w.is_lower == word.is_lower and w.prob >= -20 and not w.is_stop and len(w.text) >1]
            #remove alpha numeral suspicious cases
            #possible_words = set([p for p in possible_words if p.text.isalnum()])
            by_similarity = sorted(possible_words, key=lambda w: word.similarity(w), reverse=True)
            similarities.append(by_similarity)


        '''
        overlaps = None
        for sim_set in similarities:
            if not overlaps:
                overlaps  = sim_set
            else:
                overlaps = overlaps.intersection(sim_set)

        overlaps = list(overlaps)
        while len(overlaps) < max_similar_amount:
            possible_top = random.randint(1, 10)
            possib_addition = similarities[random.randint(0, len(similarities)-1)][possible_top]
            if (possib_addition not in overlaps):
                overlaps.append(possib_addition)
        '''

        overlaps = []
        for synset in similarities:
            overlaps += [w.lower_ for w in synset[:100]]


        '''
        overlaps = []
        i = 1
        while len(overlaps) < max_similar_amount:
            for j in range(len(similarities) - 1):
                overlaps +=  [w.lower_ for w in (similarities[j][10*(i-1):10*i])]

            overlaps = list(set(overlaps))
            i += 1

        overlaps = fuzzy_word_remove(overlaps)

        while len(overlaps) < max_similar_amount:
            for j in range(len(similarities) - 1):
                overlaps +=  [w.lower_ for w in (similarities[j][10*(i-1):10*i])]

            overlaps = list(set(overlaps))
            i += 1

        overlaps = fuzzy_word_remove(overlaps)
        '''

    except RuntimeError as e:
        print(traceback.format_exc())

    dataset = overlaps
    dataset = dataset + word_list

    return dataset


def dataset_generate(model_name = 'en_core_web_sm',suggestions = [], max_similar_amount = 100):

    try:
        model = spacy_initialize(model_name)

        similarity_set = similar_set_spacy(model,suggestions, max_similar_amount)

        log_to_text(', '.join(similarity_set), "raw_data")

    except Exception as e:
        print(e)

    return similarity_set

def train_test_split(dataset = [], test_precent = 20):
    """
    Return the segmented Lists for training and testing

    Args:
        dataset (list): The dataset
        test_precent (int): splitting threshold

    Returns:
        train (list), test (list): splitted lists
    """

    train = []
    test = []

    try:
        test_amount = int(len(dataset)*test_precent/100)
        for i in range(5):
            random.shuffle(dataset)

        test = dataset[:test_amount]
        train = dataset[test_amount:]



    except Exception as e:
        print(e)

    return train, test

if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='API options')
    parser.add_argument('-m', action="store", type=str, dest = 'model_name', help ='designated model name')
    parser.add_argument('-s', action="store", type=str, dest = 'suggestions', help ='entity word sugesstions')
    parser.add_argument('-max', action="store", type=int, dest = 'max_similar_amount', help ='maximum size of resulting dataset')

    results = parser.parse_args()

    suggestions = []
    for sug in results.suggestions.split(","):
        suggestions.append(sug.strip())

    if results.max_similar_amount is not None:
        dataset_generate(results.model_name, suggestions,results.max_similar_amount )
    else:
        dataset_generate(results.model_name, suggestions)
