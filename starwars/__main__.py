import starwars.config_manager as conf
from starwars.app import settings
from swapi import swapi as api
from starwars.app.starwarsdb import StarWarsDB
import json
import pymongo

if __name__ == '__main__':
    # 1. Generate a database on localhost
    db = StarWarsDB(db_name=conf.DEFAULT_DB_NAME, overwrite=True)

    # 2. Insert character and starship data from API request
    api_working = True
    try:
        for character in api.get_all(api.settings.CHARACTER):
            db.insert(collection=settings.COLLECTIONS.CHARACTERS, data=character)
    # API not working so retrieve data from saved .json files
    except:
        api_working = False
        with open("../files/characters.json", "r") as character_file:
            for character in json.load(character_file):
                db.insert(collection=settings.COLLECTIONS.CHARACTERS, data=character)

    # 3. Replace pilots field in Starship collection with character reference
    # TODO remove starship collection generating from step 2 and make it step 3
    characters = pymongo.MongoClient()[conf.DEFAULT_DB_NAME]["Characters"]
    for starship in api.get_all(api.settings.STARSHIPS):
        # Replace pilot field with ObjectID
        pilots = list()
        for url in starship['pilots']:
            pilot = api.extract_from_url(url)  # Get the pilot data
            pilot = characters.find_one({"name": pilot["name"]}, {"_id": 1})  # Find this pilot in Characters collection
            pilots.append(pilot['_id'])  # Replace url with reference

        # Then update the starship and insert it into the db
        starship['pilots'] = pilots
        db.insert(collection=settings.COLLECTIONS.STARSHIPS, data=starship)
