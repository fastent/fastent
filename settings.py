import couchdb


def init():
    global couchDB
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

    return db
