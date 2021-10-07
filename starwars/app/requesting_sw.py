import starwars.config_manager as conf
import requests
from pprint import pprint

sw_data = []
for num in range(1, 5):
    sw = requests.get(conf.SWAPI_URL + str(num))
    sw_json = sw.json()
    sw_data = sw_data + sw_json["results"]

starships_list = {}

count = 0
for i in sw_data:
    name = i["name"]
    starships_list[name] = i
    count += 1

print(starships_list)
print(count)
# print(sw_information['passengers'])
# pprint(sw.content)
# print(sw_information)
