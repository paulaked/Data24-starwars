import pymongo

# get_ID


def get_ID(name: str) -> str:
    client = pymongo.MongoClient()
    db = client['starwars']
    return db.characters.find_one({"name": name}, {"_id": 1})


# print((str(get_ID("Chewbacca")['_id'])))
