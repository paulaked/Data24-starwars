import pymongo


def create_starships():
    client = pymongo.MongoClient()
    db = client['starwars']
    starships = db["starships"]  # This sets the variable starships to be the starships collection

    starships.drop()  # This drops the existing starships collection
    db.create_collection("starships")  # Creates a new starships collection

    '''This last section inserts a test entry, assigns it to a variable that it returns, deletes the test record
    and returns the test record as proof that it existed and so did the starships collection'''
    db.starships.insert_one({"test": "working"})
    return_value = db.starships.find_one({"test": "working"}, {"test": 1})["test"]
    db.starships.delete_one({"test": "working"})
    return return_value
