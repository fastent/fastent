import couchdb


def init(username = None, password = None):
    """
    Global Initialization of settings

    Return the list of words closer to word1 in comparison with word2
    Args:
        word1 (str): first word
        word2 (str): second word

    Returns:
        void: As it is global settings init nothing is returned
    """

    global couchDB

    if not username:
        couchDB = couchdb.Server("http://127.0.0.1:5984/")
    else:
        couchDB = couchdb.Server("http://%s:%s@127.0.0.1:5984/" % (username, password))

def db_initialize(dbname):
    """
    Return of single db from cauchDB server if present or creates if not present

    Args:
        dbname (str): The designated database name

    Returns:
        db (Database object): the created or retrieved database
    """
    try:
        if dbname in couchDB:
            db = couchDB[dbname]
        else:
            db = couchDB.create(dbname)

    except Exception as e:
        print(e)
        return None

    return db
