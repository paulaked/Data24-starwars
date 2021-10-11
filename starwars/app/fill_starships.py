import pymongo
from starwars.app.miniproject import make_starship_dicts, add_to_list_of_ids


def fill_starships():
    client = pymongo.MongoClient()
    db = client['starwars']

    list_of_starship_dictionaries = make_starship_dicts()

    for starship in list_of_starship_dictionaries:
        db.starships.insert_one(starship)

    return db.starships.find_one({"name": "CR90 corvette"}, {"cost_in_credits": 1})
