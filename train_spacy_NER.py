from __future__ import unicode_literals, print_function
import os
import random
from pathlib import Path
import spacy


# training data
# Note: If you're using an existing model, make sure to mix in examples of
# other entity types that spaCy correctly recognized before. Otherwise, your
# model might learn the new type, but "forget" what it previously knew.
# https://explosion.ai/blog/pseudo-rehearsal-catastrophic-forgetting


def pseudo_rehersal(model):
    #TODO add the rehersal
    return 0


def train(dataset=[], model=None, new_model_name=None, output_dir=os.getcwd()+"/models", n_iter=10, Label="random_ent", verbose=False):
    """Set up the pipeline and entity recognizer, and train the new entity."""

    if not dataset:
        return None

    if model is not None:
        nlp = spacy.load(model)  # load existing spaCy model

        if verbose:
            print("Loaded model '%s'" % model)
    else:
        nlp = spacy.blank('en')  # create blank Language class

        if verbose:
            print("Created blank 'en' model")

    # Add entity recognizer to model if it's not in the pipeline
    # nlp.create_pipe works for built-ins that are registered with spaCy
    if 'ner' not in nlp.pipe_names:
        ner = nlp.create_pipe('ner')
        nlp.add_pipe(ner)
    # otherwise, get it, so we can add labels to it
    else:
        ner = nlp.get_pipe('ner')

    ner.add_label(Label)   # add new entity label to entity recognizer

    # get names of other pipes to disable them during training
    other_pipes = [pipe for pipe in nlp.pipe_names if pipe != 'ner']

    with nlp.disable_pipes(*other_pipes):  # only train NER
        optimizer = nlp.begin_training()
        for itn in range(n_iter):
            random.shuffle(dataset)
            losses = {}
            for text, annotations in dataset:
                nlp.update([text], [annotations], sgd = optimizer, drop=0.35,losses=losses)
            print(losses)

    '''
    # test the trained model
    test_text = 'Do you like MIT?'
    doc = nlp(test_text)
    print("Entities in '%s'" % test_text)
    for ent in doc.ents:
        print(ent.label_, ent.text)
    '''

    # save model to output directory
    if output_dir is not None:
        output_dir = Path(output_dir)
        if not output_dir.exists():
            output_dir.mkdir()
        nlp.meta['name'] = new_model_name  # rename model
        nlp.to_disk(output_dir)
        print("Saved model to", output_dir)

        '''
        # test the saved model
        print("Loading from", output_dir)
        nlp2 = spacy.load(output_dir)
        doc2 = nlp2(test_text)
        for ent in doc2.ents:
            print(ent.label_, ent.text)
        '''

        return nlp
