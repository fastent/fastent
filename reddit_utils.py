import praw
import time
r = praw.Reddit(client_id='ZwZuLIlsP9XRHw',
                     client_secret='xISrJFcW5RQvqH27T3RZeWzwoZw',
                     user_agent='Anotator', username='ManOfAUA', password='erik97931')


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
                if comment_iterator >=100:
                    return {word:answer_list}

                if exact_word_match(word,comment.body):
                    answer_list.append(comment.body)

                if len(answer_list) >=2:
                    return {word:answer_list}

    except Exception as e:
        print(e)

    return {word:answer_list}


def radom_find_context_comments(word):

    answer_list = []
    try:
        subreddit = r.subreddit('AskReddit')
        comment_iterator = 0
        for submission in subreddit.stream.submissions():


            submission.comments.replace_more(limit=None)
            for comment in submission.comments:

                comment_iterator += 1
                if comment_iterator >=100:
                    return {word:answer_list}

                if exact_word_match(word,comment.body):
                    answer_list.append(comment.body)

                if len(answer_list) >= 2:
                    return {word:answer_list}

    except Exception as e:
        print(e)

    return {word:answer_list}

def find_context_fast(word, min_context_amount = 5):

    answer_list = []
    try:
        comment_iterator = 0
        for submission in r.subreddit('all').search(word):
            comment_iterator += 1
            if exact_word_match(word,submission.title):
                answer_list.append(submission.title)

            if len(answer_list) >= min_context_amount:
                return {word:answer_list}

    except Exception as e:
        print(e)
        return None

    return {word:answer_list}


def find_context_long(word, min_context_amount = 5, comment_depth = 100):

    answer_list = []
    try:
        for submission in r.subreddit('all').search(word):
            comment_iterator = 0
            if len(answer_list) >= min_context_amount:
                return {word:answer_list}

            if exact_word_match(word,submission.title):
                    answer_list.append(submission.title)

            submission.comments.replace_more(limit=0)
            for comment in submission.comments:
                comment_iterator += 1
                if comment_iterator >= comment_depth:
                    break #dont wont to use break really

                if exact_word_match(word,comment.body):
                    print("good comment")
                    answer_list.append(comment.body)

                if len(answer_list) >= min_context_amount:
                    return {word:answer_list}

    except Exception as e:
        print(e)

    return {word:answer_list}
 
