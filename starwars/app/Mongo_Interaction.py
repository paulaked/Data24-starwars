import pymongo

import starwars.app.Pilot_Interaction as pilot
import starwars.app.API_Pulling as pulling
import starwars.config_manager as conf


class Mongo:
    def __init__(self, db_name: str):
        self.__client = pymongo.MongoClient(conf.MONGO_URL)
        self.__db = self.__client[db_name]
        self.__ship_API = pulling.ShipInfo()

        self.__pilot_class = pilot.PilotInteraction(db_name)

        self.__ship_keys = []
        self.populate_ship_keys()

        self.__update_many_list = []
        self.__update_many_string = ""

        self.set_full_string(self.get_ship_api)

    # Getters:
    @property
    def get_ship_api(self) -> pulling.ShipInfo:
        return self.__ship_API

    @property
    def get_db(self) -> pymongo.MongoClient:
        return self.__db

    @property
    def get_pilot_class(self) -> pilot.PilotInteraction:
        return self.__pilot_class

    @property
    def get_ship_keys(self) -> list:
        return self.__ship_keys

    @property
    def get_update_list(self) -> list:
        return self.__update_many_list

    @property
    def get_update_string(self) -> str:
        return self.__update_many_string

    # "Setters" as they might be
    def populate_ship_keys(self) -> None:
        for key in list(self.get_ship_api.get_all_ships[0].keys()):
            self.__ship_keys.append(key)

    def set_full_string(self, ship_api: pulling.ShipInfo()) -> None:
        for ship in ship_api.get_piloted_ships:
            self.__update_many_list.append(self.single_piloted_ship_dict(ship))

        for ship in ship_api.get_non_piloted_ships:
            self.__update_many_list.append(self.single_non_piloted_ship_dict(ship))
        self.__update_many_string = str(self.__update_many_list)

    @staticmethod
    def single_non_piloted_ship_dict(ship_dict: dict) -> dict:
        importing_dict = {}
        for key in list(ship_dict.keys()):
            importing_dict[key] = ship_dict[key]
        return importing_dict

    # Prepping dictionaries (with pilot urls replaced where needed):
    def single_piloted_ship_dict(self, ship_dict: dict) -> dict:
        importing_dict = {}
        for key in list(ship_dict.keys()):
            if key == "pilots":
                importing_dict[key] = self.get_pilot_class.get_object_dict[ship_dict["name"]]
            else:
                importing_dict[key] = ship_dict[key]
        return importing_dict

    # Interactions with mongo and database:
    def make_collection(self, string: str) -> None:
        self.get_db[string].drop()
        self.get_db.create_collection(string)

    def insert_in_single_data(self, db_name, update_one) -> None:
        self.get_db[db_name].update_one(update_one, {"$set": update_one}, upsert=True)

    def populate_collection(self, db_name: str) -> None:
        for i in self.get_update_list:
            self.insert_in_single_data(db_name, i)
        print("Data set loaded.")

# This class acts as the engine of the whole code, but is not quite clean enough to be the main class
# It inherits from the others and instantiates them (and as such populates their variables) but still has
# some "heavy machinery" that needs to be abstracted.
