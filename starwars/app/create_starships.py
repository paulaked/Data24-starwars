import pymongo


def create_starships():
    client = pymongo.MongoClient()
    db = client['starwars']
    starships = db["starships"]

    starships.drop()
    db.create_collection("starships")

    db.starships.insert_one({"test": "working"})
    return_value = db.starships.find_one({"test": "working"}, {"test": 1})
    db.starships.delete_one({"test": "working"})
    return return_value
