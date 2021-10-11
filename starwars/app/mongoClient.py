import pymongo


def get_Mongo_Client():
    client = None
    try:
        client = pymongo.MongoClient()
    except ConnectionError as CE:
        print(CE)
    if client:
        return client['starwars']
    else:
        return False




