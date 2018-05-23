from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag
from .fast_utils import flatten
from fuzzywuzzy import fuzz

stop_words_cache = stopwords.words("english")



def fuzzy_word_remove(word_list):
    """
    Remove words that are alike from the list

    Args:
        word_list (str): Arbitrary list of words

    Returns:
        list: The cleaned list
    """
    try:
        temp = word_list
        for i in range(len(word_list) -1):
            for j in range(len(word_list) -1):
                if i != j:
                    if (fuzz.token_sort_ratio(temp[i], temp[j]) > 75 ):
                        temp.remove(temp[j])
    except Exception as e:
        print(e)

    return temp

def text_segmentator(full_text):
    """
    Segment the text on word by word basis, while removing stopwords

    Args:
        full_text_list (list): Text split in several lists

    Returns:
        list: The list of segmented words
    """

    try:
        if not full_text:
            return None

        if all(x in [None, ''] for x in full_text):
            return None

        else:
            sentences = stop_word_remove(full_text)
            sentences = sent_tokenize(sentences)
            sentences = [word_tokenize(sent) for sent in sentences]
            sentences = flatten(sentences)

            #REMOVING NEW STEP
            sentences = special_symbols_remove(sentences)

    except Exception as e:
        print("text_segmentator error: "+ str(e))
        return None

    return sentences



def stop_word_remove(full_text_list):
    """
    Remove stopwords from a list of texts and return the list

    Args:
        full_text_list (str): Text split in several lists

    Returns:
        list: The initial list of strings with no stopwords if successful, None if failed
    """

    try:
        full_list = []
        for text in full_text_list:
            if text:
                full_text = " ".join([word for word in text.split() if word not in stop_words_cache])
                full_text = full_text.strip()
                full_list.append(full_text)

    except Exception as e:
        print(e)
        return None

    return full_text


def adverb_remove(full_text_list):
    """
    Remove adverbs from a list of texts and return the list

    Args:
        full_text_list (str): Text split in several lists

    Returns:
        list: The initial list of strings with no adverbs, if successful, None if failed
    """

    try:
        tag_list = "RB"
        full_list = []
        for text in full_text_list:
            if text:
                full_text = " ".join([word for word in text.split() if (tag_list not in pos_tag([word])[0][1])])
                full_text = full_text.strip()
                full_list.append(full_text)

    except Exception as e:
        print(e)
        return None

    return full_list


def verb_remove(full_text_list):
    """
    Remove verbs from a list of texts and return the list

    Args:
        full_text_list (str): Text split in several lists

    Returns:
        str: The initial list of strings with no verbs, if successful, None if failed
    """

    try:
        tag_list = "VB"
        full_list = []
        for text in full_text_list:
            if text:
                full_text = " ".join([word for word in text.split() if (tag_list not in pos_tag([word])[0][1])])
                full_text = full_text.strip()
                full_list.append(full_text)

    except Exception as e:
        print(e)
        return None

    return full_list


def adjective_remove(full_text_list):
    """
    Remove adjectives from a list of texts and return the whole list

    Args:
        full_text_list (str): Text split in several lists

    Returns:
        str: The initial list of strings with no adjectives, if successful, None if failed
    """

    try:
        tag_list = "JJ"
        full_list = []
        for text in full_text_list:
            if text:
                full_text = " ".join([word for word in text.split() if (tag_list not in pos_tag([word])[0][1])])
                full_text = full_text.strip()
                full_list.append(full_text)

    except Exception as e:
        print(e)
        return None

    return full_list

def special_symbols_remove(full_text_list):
    """
    Remove special symbols from a list of texts and return the list. (Few relevant symbols stay)

    Args:
        full_text_list (str): Text split in several lists

    Returns:
        list: The initial list of strings with no adjectives, if successful, None if failed
    """

    try:
        new_value =[]
        keep_char_list = ['-','.',','] #SUBJECT TO CHANGE
        for text in full_text_list:
            new_string = ''.join(e for e in text if (e.isalnum() or e in [x for x in keep_char_list]))
            if new_string:
                new_value.append(new_string)

    except Exception as e:
        print(e)

    return new_value
