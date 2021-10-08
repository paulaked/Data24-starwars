import starwars.config_manager as conf
import requests
import json


#               This is here to correctly run a test.

def requests_data_from_url():
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


def dictionary_of_ships_with_pilots_URL():
    dict_of_ships_and_pilots = {}
    for keys in dictionary_of_all_ships():
        dict_of_ships_and_pilots[keys] = dictionary_of_all_ships()[keys]["pilots"]
        # print(dictionary_of_all_ships()[keys]["pilots"])
    return dict_of_ships_and_pilots


# print(type(dictionary_of_ships_with_pilots_URL()))


def generate_txt_file_with_data(input):
    data = open(r"C:\Users\Sully\Documents\SpartaGlobal\NoSQL\Data24-starwars\starwars\app\data.json", "w")
    json.dump(input, data)


file = open(r"C:\Users\Sully\Documents\SpartaGlobal\NoSQL\Data24-starwars\starwars\app\data.json", "r")
data_file = file.readlines()


# print(type(data_file))

def converting_shipnames_to_dict():  # returns a dictionary of 'name of ship' : 'pilots urls'
    for keys in data_file:
        conversion = json.loads(keys)
        return conversion


def requests_data_from_pilots_url():  # returns a dict of 'pilot urls' : 'pilot name'
    pilot_names_urls = {}
    for keys in converting_shipnames_to_dict():
        if converting_shipnames_to_dict()[keys]:
            for piloturls in converting_shipnames_to_dict()[keys]:
                pilot = requests.get(str(piloturls))
                pilot_json = pilot.json()["name"]
                pilot_names_urls[piloturls] = pilot_json
    return pilot_names_urls


def generate_txt_file_with_pilots_url(input):
    pilots_url_data = open(r"C:\Users\Sully\Documents\SpartaGlobal\NoSQL\Data24-starwars\starwars\app\pilots_urls.json",
                           "w")
    json.dump(input, pilots_url_data)


pilot_file = open(r"C:\Users\Sully\Documents\SpartaGlobal\NoSQL\Data24-starwars\starwars\app\pilots_urls.json",
                  "r")  # Opens the pilots_urls file essentially to run times quicker.
pilots_urls = pilot_file.readlines()


def converting_pilots_to_dict():  # returns a dictionary of 'name of ship' : 'pilots urls'
    for keys in pilots_urls:
        pilot_conversion = json.loads(keys)
        return pilot_conversion


print(1)

print(converting_pilots_to_dict())
# ----- working here.----------------------- # keys: converting_to_dict()[urls]

def combine_shipname_pilotname():
    shipname_pilotname = {}
    for keys in converting_shipnames_to_dict():  # Keys are the ship name
        shipname_pilotname[keys] = []
        for urls in converting_shipnames_to_dict()[keys]:  # urls are pilot urls
            for values in converting_pilots_to_dict():
                if urls == values:
                    shipname_pilotname[keys].append(converting_pilots_to_dict()[values])
    return shipname_pilotname


print(combine_shipname_pilotname())

file.close()
pilot_file.close()
