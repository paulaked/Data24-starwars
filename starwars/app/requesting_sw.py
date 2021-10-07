import starwars.config_manager as conf

import API_Pulling as pulling
import requests

trial_API = pulling.ShipInfo()

trial_API.populate_all_ships()
trial_API.populate_piloted_ships()

for ship in trial_API.get_piloted_ships:
    print(ship["name"])
    for i in ship["pilots"]:
        print(i)
