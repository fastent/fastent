import subprocess
import threading
import multiprocessing
import couchdb
import traceback

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

        print(dbname)
        db = couchDB[dbname]

        if word in db:
            #self._logger_(username + " present in DB")
            return None

        start = time.time()
        wNet_dict = wordnet_context(word)
        context_dict = {}
        if 'fast' in option:
            context_dict = find_context_fast(word)
        if 'long' in option:
            context_dict = find_context_long(word)

        end = time.time()
        print(str(end - start))


        if wNet_dict and context_dict:
            context_dict[word] = wNet_dict[word] + context_dict[word]

        end = time.time()
        print(str(end - start))

        context_dict['_id'] = word


        db.save(context_dict)

        end = time.time()
        print(str(end - start))

    except Exception as e:
        print(traceback.format_exc())
        return None

    return context_dict



def list_contextualize(proc_list= [], option = 'fast', iterator = 0, dbname = str(time.time())):
    for url in proc_list[iterator]:
        print(url)
        _ = contextualize(url, option, dbname)



def list_segmentor(seq, size):
    newseq = []
    splitsize = 1.0/max(1,size)*len(seq)
    for i in range(size):
            newseq.append(seq[int(round(i*splitsize)):int(round((i+1)*splitsize))])
    return newseq


def parallel_runner(process_number, proc_list, option, dbname):

    # Run tasks using processes
    segmented_list = list_segmentor(proc_list, process_number)

    print(segmented_list)
    processes = [multiprocessing.Process(target = list_contextualize, args = ([segmented_list, option, iterator, dbname])) for iterator in range(process_number)]
    [process.start() for process in processes]
    [process.join() for process in processes]
