from .text_utils import stop_word_remove
from .text_utils import adverb_remove
from .text_utils import verb_remove
from .text_utils import adjective_remove
from .text_utils import special_symbols_remove
from .fast_utils import split_with_indices
import settings
import argparse
import time

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


def dataset_to_spacy(db, entity_label):
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
        #anyone missing context ??
        for word in db[entity_label]:
            if not db[entity_label][word]['context']:
                continue

            for contexted_example in db[entity_label][word]['context']:
                entities = []

                if len(word.split(" ")) > 1 :
                    start = contexted_example.lower().find(word.lower())
                    end = start+len(word)
                    entities.append((start, end, entity_label))

                else:
                    splits = list(split_with_indices(contexted_example))
                    for touple in splits:
                        if word.lower() in contexted_example[touple[0]:touple[1]].lower():
                            entities.append((touple[0], touple[0] + len(word), entity_label))

                train_data.append((contexted_example, {'entities': entities}))

    except Exception as e:
        print(e)
        return None

    return train_data


if __name__ == '__main__':

    settings.init()

    parser = argparse.ArgumentParser(description='Anotator options')
    entity_label = 'random_ent_' + str(time.time)
    parser.add_argument('-e', action="store", type=str, dest = 'entity_label', help ='designated entity label', default=entity_label)
    entity_label = parser.entity_label

    couchdb = settings.couchdb

    dataset_to_spacy(couchdb, entity_label)
