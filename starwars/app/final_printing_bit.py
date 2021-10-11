import pymongo


def print_starships():
    client = pymongo.MongoClient()
    db = client['starwars']

    starships = db.starships.find({})
    '''Goes through all of the starships found in the starships collection and prints out their names and pilots'''
    for i in starships:
        print(i["name"])
        print(i["pilots"])
