import pymongo
import pprint
import requests

import starwars.app.API_Pulling as pulling


class PilotInteraction:
    def __init__(self):
        self.__db = self.set_up_mongo("starwars")
        self.__ships_api = pulling.ShipInfo()
        self.__ship_pilot_url_dict = self.create_ship_pilot_url_dict(self.get_api)
        self.__ship_pilot_name_dict = self.create_ship_pilot_name_dict(self.get_url_dict)
        self.__ship_pilot_object_id_dict = self.create_ship_pilot_objectID_dict(self.get_name_dict, self.get_db)
        print(f"name dict: {self.__ship_pilot_name_dict}")
        print(f"Also should be name dict: {self.get_name_dict}")



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

    def set_url_dict(self, dictionary):
        self.__ship_pilot_url_dict = dictionary

    def set_name_dict(self, dictionary):
        self.__ship_pilot_name_dict = dictionary

    def set_object_dict(self, dictionary):
        self.__ship_pilot_object_id_dict = dictionary

    @staticmethod
    def pull_single_pilot(url: str) -> dict or str:
        first_pull = requests.get(url)
        dictionary = first_pull.json()
        if "name" not in dictionary:
            return f"URL {url} not found in API."
        else:
            return dictionary

    def set_up_ship(self, ship_API):
        ship_API.populate_all_ships()
        ship_API.populate_piloted_ships()

    def set_up_mongo(self, database: str):
        client = pymongo.MongoClient("mongodb://localhost:27017/")
        db = client[database]
        return db

    @staticmethod
    def create_ship_pilot_url_dict(ships_API: pulling.ShipInfo()):
        piloted_ship_dict_url = {}
        for ship in ships_API.get_piloted_ships:
            piloted_ship_dict_url[ship["name"]] = []
            for i in ship["pilots"]:
                piloted_ship_dict_url[ship['name']].append(i)
        return piloted_ship_dict_url


    def create_ship_pilot_name_dict(self, url_dict: dict):
        piloted_ship_dict_name = {}
        for key in url_dict.keys():
            piloted_ship_dict_name[key] = []
            for i in url_dict[key]:
                piloted_ship_dict_name[key].append(self.pull_single_pilot(i)["name"])
        return piloted_ship_dict_name

    @staticmethod
    def create_ship_pilot_objectID_dict(name_dict: dict, db: pymongo.MongoClient):
        object_id_dict = {}
        for key in name_dict.keys():
            object_id_dict[key] = []
            for i in name_dict[key]:
                holding_name = i
                holding_cursor = db.characters.find({"name": holding_name}, {"_id": 1})
                for j in holding_cursor:
                    object_id_dict[key].append(str(j)[8::][:-1])
        return object_id_dict

    
    print(f"Also also should be name dict: {get_name_dict}")

Testing_Pilot = PilotInteraction()
name_dict = PilotInteraction.get_name_dict
url_dict = PilotInteraction.get_url_dict
id_dict = PilotInteraction.get_object_dict
pprint.pprint(f"name dict: {name_dict}")
pprint.pprint(f"url dict: {url_dict}")
pprint.pprint(f"id_dict: {id_dict}")
