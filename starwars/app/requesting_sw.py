import starwars.config_manager as conf
import requests
from pprint import pprint


def Requests_Data_From_URL():
    for num in range(1, 5):
        sw = requests.get(conf.SWAPI_URL + str(num))
        return sw


def list_of_all_ships():
    sw_data = []
    for num in range(1, 5):
        sw1 = requests.get(conf.SWAPI_URL + str(num))
        sw_json = sw1.json()
        sw_data = sw_data + sw_json["results"]
    return sw_data


def dictionary_of_all_ships():
    starships_list = {}
    for i in list_of_all_ships():
        name = i["name"]
        starships_list[name] = i
    return starships_list


def number_of_ships():
    counter = 0
    for keys in dictionary_of_all_ships():
        counter += 1
    return counter


print(number_of_ships())
print(dictionary_of_all_ships())
# print(sw_information['passengers'])
# pprint(sw.content)
# print(sw_information)
