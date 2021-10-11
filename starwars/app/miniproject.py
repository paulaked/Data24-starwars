import starwars.config_manager as conf
import requests
import pymongo


def add_to_list_of_ids(list_of_pilot_urls, list_of_pilot_ids, db):
    for pilot_url in list_of_pilot_urls:                            # Goes through the list of pilot URLs
        pilot_info_request = requests.get(pilot_url).json()         # Gets the json of the pilot from the API
        pilot_name = pilot_info_request["name"]                     # Extracts the pilot's name
        pilot_id = db.characters.find_one({"name": pilot_name})     # Searches the characters DB for the entry with
        #                                                             the matching name
        pilot_id = pilot_id["_id"]                                  # Extracts the pilot's ObjectID
        list_of_pilot_ids.append(pilot_id)                          # Appends the ID to the starship's list of IDs

    return list_of_pilot_ids


def make_starship_dicts():
    highest_page_number = 75  # Change this to the highest page
    list_of_starship_dictionaries = []

    client = pymongo.MongoClient()  # Opens our pymongo server and assigns it to variable client
    db = client['starwars']  # Assigns the 'starwars' database to the variable db

    for i in range(highest_page_number + 1):  # Range 0-75, the highest page number in the starships collection
        list_of_pilot_ids = []

        # This gets the dictionary for the starship number i, and converts it to a nice json for us
        starship_req = requests.get(f'{conf.SWAPI_URL}/api/starships/{i}/').json()

        # Here we don't want to do anything if there's no starship at number i
        try:
            if starship_req["detail"] == 'Not found':
                continue

        # But if there is a starship there then req["detail"] doesn't exist and throws up a KeyError,
        # so we do our stuff here
        except KeyError:
            list_of_pilot_urls = starship_req["pilots"]  # Find the list of pilots who pilot that starship

            list_of_pilot_ids = add_to_list_of_ids(list_of_pilot_urls, list_of_pilot_ids, db)

            starship_req["pilots"] = list_of_pilot_ids            # Sets the 'pilots' entry in the starship JSON to
            #                                                          be the list of IDs, not the list of URLs
            list_of_starship_dictionaries.append(starship_req)    # Adds the starship JSON to the list to get sent away
            #                                                       to another file and made into a collection in the DB
    return list_of_starship_dictionaries
