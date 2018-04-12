import subprocess
import threading
import multiprocessing
import couchdb
import traceback
from fast_utils import list_segmentor

#couchDB = couchdb.Server("http://127.0.0.1:5984/")

couchDB = couchdb.Server("http://%s:%s@127.0.0.1:5984/" % ('admin', 'erikdzya'))

def db_initialize(dbname):
    try:
        if dbname in couchDB:
            db = couchDB[dbname]
        else:
            db = couchDB.create(dbname)

    except Exception as e:
        print(e)

def contextualize(word = 'none', option = 'fast', dbname = str(time.time())):
    try:

        db = couchDB[dbname]

        if word in db:
            #self._logger_(username + " present in DB")
            return None

        start = time.time()
        wNet_dict = wordnet_context(word)
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
    for word in proc_list[iterator]:
        _ = contextualize(word, option, dbname)




def parallel_runner(process_number, proc_list, option, dbname):

    # Run tasks using processes
    segmented_list = list_segmentor(proc_list, process_number)

    print(segmented_list)
    processes = [multiprocessing.Process(target = list_contextualize, args = ([segmented_list, option, iterator, dbname])) for iterator in range(process_number)]
    [process.start() for process in processes]
    [process.join() for process in processes]
