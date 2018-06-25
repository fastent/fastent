import spacy
from spacy.gold import GoldParse
from spacy.scorer import Scorer

def spacy_evaluator(ner_model, examples):
    """
    Evaluate the created NER model using different metrics

    Args:
        ner_model (spacy model object): The dataset
        examples (list): testing examples

    Returns:
        score_object (score object): object with different scoring metrics
    """

    try:
        score_object = Scorer()
        for base_input, annotations in examples:
            doc_for_gold = ner_model.make_doc(base_input)
            gold = GoldParse(doc_for_gold, entities=annotations)
            prediction = ner_model(base_input)
            #evaluation
            score_object.score(prediction, gold)
            
    except Exception as e:
        print("Unable to evaluate model with error: " + str(e))
        return None
    return score_object.scores
