import pymongo
from starwars.app.requesting_sw import starships_list


# get a list of ships with their pilot APIs. Input argument is a list of ship info in dictionary format from API

def extract_ship_pilot_and_apis(ship_dict: dict) -> list:
    ship_and_pilots = []
    ship_and_pilots.append(ship_dict["name"])
    ship_and_pilots.append(ship_dict["pilots"])
    return ship_and_pilots

