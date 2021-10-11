import pymongo

import starwars.app.Pilot_Interaction as pilot
import starwars.app.API_Pulling as pulling
import starwars.config_manager as conf


class Mongo:
    def __init__(self, db_name: str):
        self.__client = pymongo.MongoClient(conf.MONGO_URL)
        self.__db = self.__client[db_name]
        self.__ship_API = pulling.ShipInfo()
        #print("API Puller class instantiated.")

        self.__pilot_class = pilot.PilotInteraction(db_name)
        #print("Pilot manipulation class has been instantiated.")

        self.__ship_keys = []
        self.populate_ship_keys()

        self.__update_many_list = []
        self.__update_many_string = ""

        self.set_full_string(self.get_ship_API)

    @property
    def get_ship_API(self):
        return self.__ship_API

    @property
    def get_db(self):
        return self.__db

    @property
    def get_pilot_class(self):
        return self.__pilot_class

    @property
    def get_ship_keys(self):
        return self.__ship_keys

    @property
    def get_update_list(self):
        return self.__update_many_list

    @property
    def get_update_string(self):
        return self.__update_many_string

    def populate_ship_keys(self):
        for key in list(self.get_ship_API.get_all_ships[0].keys()):
            self.__ship_keys.append(key)

    @staticmethod
    def single_non_piloted_ship_string(ship_dict):
        importing_string = {}
        for key in list(ship_dict.keys()):
            importing_string[key] = ship_dict[key]
        return importing_string

    def single_piloted_ship_string(self, ship_dict):
        importing_string = {}
        for key in list(ship_dict.keys()):
            if key == "pilots":
                importing_string[key] = self.get_pilot_class.get_object_dict[ship_dict["name"]]
            else:
                importing_string[key] = ship_dict[key]
        return importing_string

    def set_full_string(self, ship_API: pulling.ShipInfo()):
        for ship in ship_API.get_piloted_ships:
            self.__update_many_list.append(self.single_piloted_ship_string(ship))

        for ship in ship_API.get_non_piloted_ships:
            self.__update_many_list.append(self.single_non_piloted_ship_string(ship))

        self.__update_many_string = str(self.__update_many_list)

    def make_collection(self, string: str):
        self.get_db[string].drop()
        self.get_db.create_collection(string)

    def insert_in_single_data(self, db_name, update_one):
        self.get_db[db_name].update_one(update_one, {"$set": update_one}, upsert=True)

    def populate_collection(self, db_name: str):
        for i in self.get_update_list:
            self.insert_in_single_data(db_name, i)
        print("Data set loaded.")
