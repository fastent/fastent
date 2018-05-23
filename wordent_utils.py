from nltk.corpus import wordnet as wn
from nltk.stem import WordNetLemmatizer
from nltk import pos_tag, word_tokenize
from nltk.corpus import wordnet as wn
from .fast_utils import replace_all
import traceback

def penn_to_wn(tag):
    """
    Convert PENN to WordNet Format

    Args:
        tag (str): PENN Tag

    Returns:
        str: Wordent Representation
    """

    try:

        if tag.startswith('J'):
            return wn.ADJ
        elif tag.startswith('N'):
            return wn.NOUN
        elif tag.startswith('R'):
            return wn.ADV
        elif tag.startswith('V'):
            return wn.VERB

    except Exception as e:
        print(e)

    return None


def word_to_wn(word):
    """
    Convert a string/word to WordNet Format

    Args:
        word (str): an arbitrary word

    Returns:
        str: Wordent Representation
    """

    ans = None
    try:

        tagged = pos_tag(word_tokenize(word))
        synsets = []
        for token in tagged:
            wn_tag = penn_to_wn(token[1])
            if not wn_tag:
                continue

            synsets.append(wn.synsets(token[0], pos=wn_tag)[0])

        reps = {'Synset':'', '(':'', ')':'','\'':''}
        ans = replace_all(str(synsets[0]),reps)

    except Exception as e:
        print(e)
        return None

    return ans



def word_to_hyperTouple(word):

    """
    Given an arbitrary word, return a touple of a word and the closest ancestor hypernym in the hierarchy

    Args:
        word (str): an arbitrary word

    Returns:
        str: Wordent Representation
    """

    ans = None
    try:

        wn_word = word_to_wn(word)
        base_hypernym_closure = wn.synset(wn_word).closure(lambda s:s.hypernyms())
        hypernym_list= set([i for i in base_hypernym_closure])

        #depth calc
        max_depth = max(s.min_depth() for s in hypernym_list)
        base_hypernym_synset= [s for s in hypernym_list if s.min_depth() == max_depth]
        print(base_hypernym_synset)
        if base_hypernym_synset:
            string_hyper= str(base_hypernym_synset[0])
            reps = {'Synset':'', '(':'', ')':'','\'':''}
            base_hypernym = replace_all(string_hyper,reps)
            ans = (wn_word, base_hypernym)

    except Exception as e:
        print(e)
        return None

    return ans

def wordnet_synonyms(word):
    """
    Given an arbitrary word, return the closest WordNet synonym list

    Args:
        word (str): an arbitrary word

    Returns:
        synonyms (list): synonym list
    """
    synonyms = None
    try:
        for syn in wn.synsets(word):
            for l in syn.lemmas():
                synonyms.append(l.name())

    except Exception as e:
        print(e)
        return None

    return synonyms



def wordnet_context(word):
    context = None

    try:
        word_Wnet = word_to_wn(word)

        if not word_Wnet:
            return None

        context = wn.synset(word_Wnet).examples()

    except Exception as e:
        print(traceback.format_exc())
        return None

    return {word:context}
