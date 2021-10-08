# import starwars.config_manager as conf
# import requests
#
# # Instead theres a nice function that converts it to json/python dict, so:
#
# req = requests.get(conf.SWAPI_URL)
# json.
# if 'json' in req.headers.get('Content-Type'):
#     js = req.json()
# else:
#     print('Response content is not in JSON format.')
#     js = 'spam'
# # req = req.json()
# print(js)

import requests
import json

results = []
for x in range(1, 9):
    response = requests.get("https://swapi.co/api/people/?page="+str(x))
    data = response.json()

    next_page = data["next"]
    results.extend(data["results"])

with open('data.json', 'w') as outfile:
    json.dump(results, outfile)