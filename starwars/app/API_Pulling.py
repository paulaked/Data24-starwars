import starwars.config_manager as conf

import requests
import ast                          # Decoding the byte pulled from the API


class ShipInfo:
    def __init__(self):
        self.__all_ships = []
        self.__piloted_ships = []
        self.__non_piloted_ships = []
        self.__ship_count = self.pull_ship_count()

        self.populate_all_ships()
        self.populate_piloted_ships()
        self.populate_non_piloted_ships()
# Getters for class properties

    @property
    def get_all_ships(self):
        return self.__all_ships

    @property
    def get_piloted_ships(self):
        return self.__piloted_ships

    @property
    def get_non_piloted_ships(self):
        return self.__non_piloted_ships

    @property
    def get_ship_count(self):
        return self.__ship_count

# Essentially these are setters, but everything is self-contained - essentially to be called in main that runs
# the whole thing. Not declared in the init as pull all ships is not fast

    def populate_all_ships(self):
        self.__all_ships = self.pull_all_ships()

    def populate_piloted_ships(self):
        self.__piloted_ships = self.pull_piloted_ships(self.get_all_ships)[0]

    def populate_non_piloted_ships(self):
        self.__non_piloted_ships = self.pull_piloted_ships(self.get_all_ships)[1]
# Static Methods

    @staticmethod
    def convert_to_dict(pull) -> dict:
        pulled_content = pull.content
        pulled_dict = ast.literal_eval(pulled_content.decode("UTF-8"))
        return pulled_dict

    @staticmethod
    def convert_to_dict_json(pull) -> dict:
        d = pull.json()
        return d

    @staticmethod
    def pull_piloted_ships(ship_list: list):
        piloted_list = []
        unpiloted_list = []
        for ship in ship_list:
            if len(ship["pilots"]) > 0:
                piloted_list.append(ship)
            else:
                unpiloted_list.append(ship)
        return [piloted_list, unpiloted_list]

# Dynamic Methods

    def pull_single_ship(self, ship_no: int) -> dict or str:
        first_pull = requests.get(conf.SWAPI_URL+"/starships/" + str(ship_no))
        dictionary = self.convert_to_dict(first_pull)
        if "name" not in dictionary:
            return f"Object with url number {ship_no} not found."
        else:
            return dictionary

    def pull_ship_count(self) -> int:
        pull = requests.get(conf.SWAPI_URL+"/starships/")
        dictionary = self.convert_to_dict_json(pull)
        return dictionary["count"]

    def pull_all_ships(self) -> list:
        i = 1
        ship_list = []
        while len(ship_list) < self.pull_ship_count():
            temp_ship = self.pull_single_ship(i)
            if type(temp_ship) is dict:
                ship_list.append(temp_ship)
            i += 1
        return ship_list

# So an instance of this class will contain all the API info on ships
