import re
import sys
from text_utils import stop_word_remove
from text_utils import adverb_remove
from text_utils import verb_remove
from text_utils import adjective_remove
from text_utils import special_symbols_remove

from fast_utils import getopts
from fast_utils import getopts


def dataset_NER_prepocess(dataset):
    """
    Preprocess a dataset before training NER.

    Assuming That a clean dataset of Entities should not contain
    verbs, adverbs, adjectives and random symbols

    Args:
        dataset (list): list of strings for NER trainging
    Returns:
        list: processed dataset if Sucessful, None otherwise
    """
    preprocessed = []

    try:
        preprocessed = stop_word_remove(dataset)

        if not preprocessed:
            preprocessed = dataset

        preprocessed = adverb_remove(dataset)

        if not preprocessed:
            preprocessed = dataset

        preprocessed = verb_remove(dataset)

        if not preprocessed:
            preprocessed = dataset
        preprocessed = adjective_remove(dataset)

        if not preprocessed:
            preprocessed = dataset

        preprocessed = special_symbols_remove(dataset)

    except Exception as e:
        print(e)
        return None

    return preprocessed



def dataset_to_spacy(dataset, entity_label):
    """
    Bring a dataset to a spacy trainable state

    Args:
        dataset (list): list of strings for NER trainging
        entity_label (str): designated label for the Entity
    Returns:
        list: The spacy training ready list if Sucessful, None otherwise
    """

    train_data = []
    try:

        for name in dataset:
            name.strip()
            annotations = list(split_with_indices(name))
            entities = []

            complete_touple = [(annotations[0][0] ,annotations[-1][1])]

            #assume that the whole string is a part of the entity
            for touple in complete_touple:
                if touple[1] - touple[0] > 1:
                    entities.append((touple[0], touple[1], entity_label))
            '''
            # if need arises for split Entities

            for touple in annotations:
                if touple[1] - touple[0] > 1:
                    entities.append((touple[0], touple[1], entity_label))
            '''

            train_data.append((str(name),{'entities':entities}))

    except Exception as e:
        print(e)
        return None


if __name__ == '__main__':

	myargs = getopts(argv)
	timeout = None

    dataset_path = ''
	if '-d' in myargs:
		dataset_path = int(myargs['-d'])
