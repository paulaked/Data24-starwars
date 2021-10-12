import starwars.config_manager as conf
from starwars.app import settings
from swapi import swapi as api
from starwars.app.starwarsdb import StarWarsDB
import json

if __name__ == '__main__':
    # 1. Generate a database on localhost
    db = StarWarsDB(db_name=conf.DEFAULT_DB_NAME, overwrite=True)

    # 2. Insert character and starship data from API request
    api_working = True
    try:
        for character in api.get_all(api.settings.CHARACTER):
            db.insert(collection=settings.COLLECTIONS.CHARACTERS, data=character)

        for starship in api.get_all(api.settings.STARSHIPS):
            db.insert(collection=settings.COLLECTIONS.STARSHIPS, data=starship)
    # API not working so retrieve data from saved .json files
    except:
        api_working = False
        with open("../files/characters.json", "r") as character_file:
            for character in json.load(character_file):
                db.insert(collection=settings.COLLECTIONS.CHARACTERS, data=character)

        with open("../files/starships.json", "r") as starship_file:
            for starship in json.load(starship_file):
                db.insert(collection=settings.COLLECTIONS.STARSHIPS, data=starship)

    # 3. Replace pilots field in Starship collection with character reference
    # TODO remove starship collection generating from step 2 and make it step 3
    # for starship in api.get_all(api.settings.STARSHIPS):
    #     # Replace pilot field with ObjectID
    #     for url in starship['pilots']:
    #         pilot = api.extract_from_url(url)
    #
    #
    #     db.insert(collection=settings.COLLECTIONS.STARSHIPS, data=starship)
