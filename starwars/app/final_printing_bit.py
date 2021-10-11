import pymongo


def print_starships():
    client = pymongo.MongoClient()  # Opens our pymongo server and assigns it to variable client
    db = client['starwars']

    starships = db.starships.find({})
    for i in starships:
        print(i["name"])
        print(i["pilots"])
