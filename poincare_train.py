import argparse
import logging
from wordent_utils import word_to_wn
from gensim.models.poincare import PoincareModel, PoincareKeyedVectors, PoincareRelations

logging.basicConfig(level=logging.INFO)


def poincare_train(hypertouple_dataset, size=2, burn_in=0, epochs = 5, print_freq = 100):
    poincare_model = None
    try:

        #poincare_model = PoincareModel(train_data = hypertouple_dataset)
        poincare_model = PoincareModel(train_data=hypertouple_dataset, size = size, burn_in = burn_in)
        poincare_model.train(epochs=epochs, print_every = print_freq)

    except Exception as e:
        print(e)
    return poincare_model



def poincare_simmilar(poincare_model, word):
    most_simmilar_set = None
    try:
        wnet_word = word_to_wn(word)
        most_simmilar_set = poincare_model.kv.most_similar(wnet_word)
    except Exception as e:
        print(e)

    return most_simmilar_set


def poincare_closer_then(poincare_model, word1, word2):
    """
    Return the list of words closer to word1 in comparison with word2
    Args:
        word1 (str): first word
        word2 (str): second word

    Returns:
        closer_list (list) : The list of segmented words
    """


    closer_list = None
    try:
        wnet_word1 = word_to_wn(word1)
        wnet_word2 = word_to_wn(word2)

        closer_list = poincare_model.kv.closer_than(wnet_word1, wnet_word2)
    except Exception as e :
        print(e)

    return closer_list


def poincare_word_dist(poincare_model, word1, word2):
    """
    Return the distance of words between word1 and word2
    Args:
        word1 (str): first word
        word2 (str): second word

    Returns:
        dist (float) : The list of segmented words
    """


    dist = None
    try:
        wnet_word1 = word_to_wn(word1)
        wnet_word2 = word_to_wn(word2)
        dist = poincare_model.kv.distance(wnet_word1, wnet_word2)
    except Exception as e :
        print(e)

    return dist


def poincare_closest_child(poincare_model, word):
    """
    Return the closet child node for a given word
    Args:
        word (str): arbitrary word

    Returns:
        child_word (str) : The closest child word in Wordnet format
    """

    child_word = None
    try:
        wnet_word = word_to_wn(word)
        child_word = poincare_model.kv.closest_child(wnet_word)
    except Exception as e :
        print(e)

    return child_word


def poincare_closest_parent(poincare_model, word):
    """
    Return the closet parent node for a given word
    Args:
        word (str): arbitrary word

    Returns:
        child_word (str) : The closest parent word in Wordnet format
    """

    parent_word = None
    try:
        wnet_word = word_to_wn(word)
        parent_word = poincare_model.kv.closest_parent(wnet_word)
    except Exception as e :
        print(e)

    return parent_word



if __name__ == '__main__':

    parser = argparse.ArgumentParser(description='Anotator options')
    parser.add_argument('-p', action="store", type=str, dest = 'dataset_path', help ='designated dataset path', default = None)
    parser.add_argument('-d', action="store", type=str, dest = 'delimiter', help ='the split for the hyper touples', default = '\t')

    path = parser.path

    dataset = PoincareRelations(file_path=path, delimiter='\t')

    model = poincare_train(dataset)
