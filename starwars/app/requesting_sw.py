import starwars.config_manager as conf

import requests
import ast                          # Decoding the byte pulled from the API


sw = requests.get(conf.SWAPI_URL + "/people/1")

i = 1

while i <= 10:
    sw = requests.get(conf.SWAPI_URL + "/starships/" + str(i))
    sw_content = sw.content
    sw_data = ast.literal_eval(sw_content.decode("UTF-8"))
    if "detail" not in sw_data:
        print(sw_data)
    else:
        print("not found")
    i += 1