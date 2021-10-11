import pymongo
import requests

import starwars.app.API_Pulling as pulling
import starwars.config_manager as conf


class PilotInteraction:
    def __init__(self, db_name: str):
        # as with previous class, properties are all assigned on initiation so that there will be no errors when
        # calling the class further down the line
        self.__db = self.set_up_mongo(db_name)
        self.__ships_api = pulling.ShipInfo()

        self.__ship_pilot_url_dict = self.create_ship_pilot_url_dict(self.get_api)
        self.__ship_pilot_name_dict = self.create_ship_pilot_name_dict(self.get_url_dict)
        self.__ship_pilot_object_id_dict = self.create_ship_pilot_object_id_dict(self.get_name_dict, self.get_db)

    # Getters for full class - can't say for sure if all of them are used, but having them allows for use in the
    # future:
    @property
    def get_db(self):
        return self.__db

    @property
    def get_api(self):
        return self.__ships_api

    @property
    def get_url_dict(self) -> dict:
        return self.__ship_pilot_url_dict

    @property
    def get_name_dict(self) -> dict:
        return self.__ship_pilot_name_dict

    @property
    def get_object_dict(self) -> dict:
        return self.__ship_pilot_object_id_dict

    # Setters:
    def set_url_dict(self, dictionary):
        self.__ship_pilot_url_dict = dictionary

    def set_name_dict(self, dictionary):
        self.__ship_pilot_name_dict = dictionary

    def set_object_dict(self, dictionary):
        self.__ship_pilot_object_id_dict = dictionary

    # kind of setters, kind of a setter-uppers, allows for both lists top be populated in one line, meaning there
    # won't be one without the other
    @staticmethod
    def set_up_ship(ship_api):
        ship_api.populate_all_ships()
        ship_api.populate_piloted_ships()

    @staticmethod
    def set_up_mongo(database: str):
        client = pymongo.MongoClient(conf.MONGO_URL)
        db = client[database]
        return db

    # Single pilot pulling which gets called to get pilot info from URL - will output a string if there's nothing at
    # the URL and cause an error in the manipulation of the pilot dictionaries/lists later in the code
    @staticmethod
    def pull_single_pilot(url: str) -> dict or str:
        first_pull = requests.get(url)
        dictionary = first_pull.json()
        if "name" not in dictionary:
            return f"URL {url} not found in API."
        else:
            return dictionary

    # We have three dictionaries, each containing a different form of the pilot's info - first just has ship and URL,
    # second one uses this to make an API call and get the name of the pilot, and third one uses this along with
    # the existing monogo characters collection to find their ID number and stores this

    @staticmethod
    def create_ship_pilot_url_dict(ships_api: pulling.ShipInfo()):
        piloted_ship_dict_url = {}
        for ship in ships_api.get_piloted_ships:
            piloted_ship_dict_url[ship["name"]] = []
            for i in ship["pilots"]:
                piloted_ship_dict_url[ship['name']].append(i)
        return piloted_ship_dict_url

    # Calls static method above to create a dictionary with the pilot names instead of urls
    def create_ship_pilot_name_dict(self, url_dict: dict):
        piloted_ship_dict_name = {}
        for key in url_dict.keys():
            piloted_ship_dict_name[key] = []
            for i in url_dict[key]:
                piloted_ship_dict_name[key].append(self.pull_single_pilot(i)["name"])  # It is a key in a dictionary
        return piloted_ship_dict_name

    @staticmethod
    def create_ship_pilot_object_id_dict(name_dict: dict, db: pymongo.MongoClient):
        object_id_dict = {}
        for key in name_dict.keys():
            object_id_dict[key] = []
            for i in name_dict[key]:
                holding_name = i
                holding_cursor = db.characters.find({"name": holding_name}, {"_id": 1})
                for j in holding_cursor:
                    object_id_dict[key].append(str(j)[8::][:-1])        # Only selects ObjectIDs and not punctuation etc
        return object_id_dict
