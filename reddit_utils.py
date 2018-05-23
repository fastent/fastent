import praw
import traceback
from .fast_utils import exact_word_match

r = praw.Reddit(client_id='jaFBw59_YwZq2g',
                client_secret='NX8gsx7NAppehlUJH3B3Db1yH7w',
                user_agent='Anotator', username='fastent_reddit',
                password='fastent2017')


def random_find_context_comments_depth(word):

    answer_list = []
    try:
        subreddit = r.subreddit('AskReddit')
        comment_iterator = 0
        for submission in subreddit.stream.submissions():
            submission.comments.replace_more(limit=None)
            kyanq = submission.comments.list()
            for comment in kyanq:

                comment_iterator += 1
                if comment_iterator >= 100:
                    return {word: answer_list}

                if exact_word_match(word, comment.body):
                    answer_list.append(comment.body)

                if len(answer_list) >= 2:
                    return {word: answer_list}

    except Exception as e:
        print(e)

    return {word: answer_list}


def radom_find_context_comments(word):

    answer_list = []
    try:
        subreddit = r.subreddit('AskReddit')
        comment_iterator = 0
        for submission in subreddit.stream.submissions():

            submission.comments.replace_more(limit=None)
            for comment in submission.comments:

                comment_iterator += 1
                if comment_iterator >= 100:
                    return {word: answer_list}

                if exact_word_match(word, comment.body):
                    answer_list.append(comment.body)

                if len(answer_list) >= 2:
                    return {word: answer_list}

    except Exception as e:
        print(e)

    return {word: answer_list}


def find_context_fast(word, min_context_amount=5):
    """
    Return a context for a word after fast title traverse

    Args:
        word (str): The word that needs context
        min_context_amount (int): maximum number of contexts to find_context_fast
    Returns:
         (dict) : {word (str): context (list)} the resulting pair of word:contexts
    """
    answer_list = []
    try:
        comment_iterator = 0
        for submission in r.subreddit('all').search(word):
            comment_iterator += 1
            if exact_word_match(word, submission.title):
                answer_list.append(submission.title)

            if len(answer_list) >= min_context_amount:
                return {word: answer_list}

    except Exception as e:
        print(traceback.format_exc())
        return None

    return {word: answer_list}


def find_context_long(word, min_context_amount=5, comment_depth=100):
    """
    Return a context for a word after long comment traverse

    Args:
        word (str): The word that needs context
        min_context_amount (int): maximum number of contexts to find_context_fast
        comment_depth (int): Maximum comment depth for traversal

    Returns:
         (dict) : {word (str): context (list)} the resulting pair of word:contexts
    """

    answer_list = []
    try:
        for submission in r.subreddit('all').search(word):
            comment_iterator = 0
            if len(answer_list) >= min_context_amount:
                return {word: answer_list}

            if exact_word_match(word, submission.title):
                    answer_list.append(submission.title)

            submission.comments.replace_more(limit=0)
            for comment in submission.comments:
                comment_iterator += 1
                if comment_iterator >= comment_depth:
                    break  #dont wont to use break really

                if exact_word_match(word, comment.body):
                    print("good comment")
                    answer_list.append(comment.body)

                if len(answer_list) >= min_context_amount:
                    return {word: answer_list}

    except Exception as e:
        print(traceback.format_exc())

    return {word: answer_list}
