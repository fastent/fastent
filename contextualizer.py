import time
import multiprocessing
import traceback
import settings
from .anotatorfast_utils import list_segmentor
from .reddit_utils import find_context_fast
from .reddit_utils import find_context_long
from .wordent_utils import wordnet_context



def contextualize(word = 'none', option = 'fast', dbname = str(time.time())):
    """
    Gettting a context with a speified method and saving in DB

    Args:
        word (str): The word meant for contextualization
        option (str): Type of contextualization we aim for
        dbname (str): The dbname that we save in
    Returns:
         context_dict (dict) : The strucutred dictionary for word and contexts
    """
    try:

        db = settings.couchDB[dbname]

        if word in db:
            return None

#        wNet_dict = wordnet_context(word)
        context_dict = {'context':[],'_id': word}
        if 'fast' in option:
            context = find_context_fast(word)
        if 'long' in option:
            context = find_context_long(word)

        if context:
            context_dict['context'] = context[word]

        #if wNet_dict and context:
         #   context_dict['context'] = wNet_dict[word] + context[word]


        db.save(context_dict)

    except Exception as e:
        print(traceback.format_exc())
        return None

    return context_dict



def list_contextualize(proc_list= [], option = 'fast', iterator = 0, dbname = str(time.time())):
    """
    Gettting a context with a speified method for the given word list

    Args:
        proc_list (list): The word list meant for contextualization
        option (str): Type of contextualization we aim for
        iterator (int): Processing Thread number
        dbname (str): The dbname that we save in
    Returns:
         (void)
    """
    for word in proc_list[iterator]:
        _ = contextualize(word, option, dbname)




def parallel_runner(process_number, proc_list, option, dbname):
    """
    Initialize DB for words. Running Parallel threads for contextualization.

    Args:
        proc_list (list): The word list meant for contextualization
        option (str): Type of contextualization we aim for
        process_number (int): Processing Thread number
        dbname (str): The dbname that we save in
    Returns:
         (void)
    """
    settings.init()
    # Run tasks using processes
    segmented_list = list_segmentor(proc_list, process_number)

    print(segmented_list)
    processes = [multiprocessing.Process(target = list_contextualize, args = ([segmented_list, option, iterator, dbname])) for iterator in range(process_number)]
    [process.start() for process in processes]
    [process.join() for process in processes]
