import requesting_sw as rqstsw
import starwars.config_manager as conf
import requests


data = rqstsw.dictionary_of_all_ships()

file = open("data.json", "w")


for num in range(1, 5):
    sw1 = requests.get(conf.SWAPI_URL + str(num))
    sw_json = sw1.json()
    sw_data = sw_json["results"]
    file.write(str(sw_json))


print(4)
