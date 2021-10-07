import pymongo
from starwars.app.requesting_sw import starships_list


# get a list of ships with their pilot APIs. Input argument is a list of ship info in dictionary format from API

def generate_list_of_ships_with_pilot_apis(list_of_dicts: list) -> list:
    ship_and_pilots = []
    for ship in list_of_dicts:
        ship_and_pilots.append(ship["name"])
        ship_and_pilots.append(ship["pilots"])
    return ship_and_pilots

