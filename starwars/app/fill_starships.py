import pymongo
from starwars.app.miniproject import make_starship_dicts


def fill_starships():
    client = pymongo.MongoClient()  # Opens our pymongo server and assigns it to variable client
    db = client['starwars']  # Assigns the 'starwars' database to the variable db

    '''Gets back a list containing all the dictionaries for each starship'''
    list_of_starship_dictionaries = make_starship_dicts()

    # Inserts each of the starship dictionaries into the starships collection
    for starship in list_of_starship_dictionaries:
        db.starships.insert_one(starship)

    # This searches the starships database for the cost_in_credits of the CR90 corvette to prove that the record has
    # been correctly inserted
    return db.starships.find_one({"name": "CR90 corvette"}, {"cost_in_credits": 1})["cost_in_credits"]
