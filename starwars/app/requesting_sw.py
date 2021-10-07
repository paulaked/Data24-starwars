import starwars.config_manager as conf
import requests
from pprint import pprint

sw = requests.get(conf.SWAPI_URL)
sw_json = sw.json()
sw_dict = sw_json["results"]
starships_list = {}

# print(sw_json)
# print(sw_dict)
count = 0
for i in sw_dict:
    name = i["name"]
    starships_list[name] = i
    count += 1


print(starships_list)
print(count)
# print(sw_information['passengers'])
# pprint(sw.content)
# print(sw_information)