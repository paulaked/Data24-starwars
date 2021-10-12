import pymongo  # MongoDB python library.
import requests  # API requests module for python.


def get_info(pg_num: int, key_name: str, cat: str):

    # This function is generalised to be used to collect any particular information from
    # the swapi.dev website, using the arguments for the category, in this case being starships
    # and the page number to collect any particular part of the document which in this project
    # will be collecting the name of the starship and continuously looping through to extract all the
    # starship names.

    url = f'https://swapi.dev/api/{cat}/{pg_num}/'  # URL of the information to be extracted.
    info = requests.get(url)
    info_values = info.json()[key_name]
    return info_values


def secondary_number_list(pg_num: int, cat: str, secondary_key_name: str):

    # For this case this function will collect the page numbers of the pilots for the starship
    # inputted as an argument from now the people category.

    secondary_list = []
    list_ = get_info(pg_num, secondary_key_name, cat)

    for i in range(len(list_)):
        secondary_list.append(list_[i].split('/')[5].strip())  # collecting the page number from the URL.

    return secondary_list


def get_pilot(pg_num: int):  # This function simply collects the names of the pilots in a list.

    pilot_number_list = secondary_number_list(pg_num,
                                              'starships',
                                              'pilots'
                                              )
    pilots = []

    for i in pilot_number_list:

        pilots.append(get_info(i,
                               'name',
                               'people')
                      )

    return pilots


def get_pilot_object_ids(pg_num: int):

    # Connects to the StarWars database on MongoDB and matches the name of the pilots collected
    # from the URL to the object id's on the data base, returning the ids in a list.

    client = pymongo.MongoClient()  # Connecting to the mongodb database.
    db = client["StarWars"]

    pilot_list = get_pilot(pg_num)
    pilot_id_list = []

    for i in pilot_list:  # For loop to run through all the initial pilots in the list of names.

        character_id = db.characters.find_one({"name": i},
                                              {"_id": 1}
                                              )

        char_id_num = character_id["_id"]  # collects only the value associated with the _id key.
        pilot_id_list.append(char_id_num)

    return pilot_id_list


def create_collection(database: str, collection_name: str):

    # Simple function to create a new collection in a database depending on the arguments given.

    client = pymongo.MongoClient()  # Connecting to the mongodb database.
    db = client[database]
    db.create_collection(collection_name)


def add_starship_document(database: str, collection: str, name: str, pilots_list: list):

    # Given the name of the starship and the list of object ids for the pilots, creates and adds a document
    # into the collection.

    client = pymongo.MongoClient()  # Connecting to the mongodb database.
    db = client[database]
    insert = db.get_collection(collection)
    insert.insert_one(
        {"starship": name,
         "pilots": pilots_list
         })


def check_collection(database: str, collection: str, starship_name: str):

    # Check to see if the information has been inserted into the MongoDB Database for our case of adding
    # starships and Pilots to the database.

    client = pymongo.MongoClient()  # Connecting to the mongodb database.
    db = client[database]
    det_ = db.get_collection(collection).find(
        {"starship": starship_name}, {'pilots': 1, 'starship': 1, '_id': 0}
        )

    for item in det_:   # For loop so that we see the data and a cursor object isn't returned.
        return item
