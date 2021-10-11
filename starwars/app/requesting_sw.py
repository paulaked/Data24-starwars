import starwars.config_manager as conf
import requests
import json
import pymongo
from pprint import pprint

client = pymongo.MongoClient()
db = client['starwars']


# This is here to run a test.

def requests_data_from_url():
    for num in range(1, 5):
        sw = requests.get(conf.SWAPI_URL + str(num))
        return sw


#  Function pulls all of ship information from the SWAPI.

def list_of_all_ships():
    sw_data = []
    for num in range(1, 5):
        sw1 = requests.get(conf.SWAPI_URL + str(num))
        sw_json = sw1.json()
        sw_data = sw_data + sw_json["results"]
    return sw_data


# Changes format of the ship data so that the key is now the ship name and the data is the value for each ship.

def dictionary_of_all_ships():
    starships_list = {}
    for i in list_of_all_ships():
        name = i["name"]
        starships_list[name] = i
    return starships_list


# Creates a dict with ship name: URL of pilots who fly the ship.

def dictionary_of_ships_with_pilots_URL():
    dict_of_ships_and_pilots = {}
    for keys in dictionary_of_all_ships():
        dict_of_ships_and_pilots[keys] = dictionary_of_all_ships()[keys]["pilots"]
        # print(dictionary_of_all_ships()[keys]["pilots"])
    return dict_of_ships_and_pilots


# Following functions are responsible for making and transforming .json files into usable formats.
#                                                       3 .json files were created. 1 was made redundant.

def generate_txt_file_with_data(input):
    data = open(r"C:\Users\Sully\Documents\SpartaGlobal\NoSQL\Data24-starwars\starwars\app\data.json", "w")
    json.dump(input, data)


file = open(r"C:\Users\Sully\Documents\SpartaGlobal\NoSQL\Data24-starwars\starwars\app\data.json", "r")
data_file = file.readlines()


def generate_txt_file_with_ship_information(input):
    data = open(r"C:\Users\Sully\Documents\SpartaGlobal\NoSQL\Data24-starwars\starwars\app\ship_data.json", "w")
    json.dump(input, data)


ship_data = open(r"C:\Users\Sully\Documents\SpartaGlobal\NoSQL\Data24-starwars\starwars\app\ship_data.json", "r")
ship_data_file = ship_data.readlines()


def converting_ships_to_dict():  # returns a dictionary of 'name of ship' : 'pilots urls'
    for ships in ship_data_file:
        ship_conversion = json.loads(ships)
        return ship_conversion


def converting_ship_names_to_dict():  # returns a dictionary of 'name of ship' : 'pilots urls'
    for keys in data_file:
        conversion = json.loads(keys)
        return conversion


def requests_data_from_pilots_url():  # returns a dict of 'pilot urls' : 'pilot name'
    pilot_names_urls = {}
    for keys in converting_ship_names_to_dict():
        if converting_ship_names_to_dict()[keys]:
            for piloturls in converting_ship_names_to_dict()[keys]:
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


# These functions produces a dictionary of ship names and pilot names. Was made redundant  after refactoring.

def combine_ship_name_pilot_name():  # ship names with pilot names
    shipname_pilotname = {}
    for keys in converting_ship_names_to_dict():  # Keys are the ship name
        shipname_pilotname[keys] = []
        for urls in converting_ship_names_to_dict()[keys]:  # urls are pilot urls
            for values in converting_pilots_to_dict():
                if urls == values:
                    shipname_pilotname[keys].append(converting_pilots_to_dict()[values])
    return shipname_pilotname


# Function first replaces pilot urls into names and then uses those names to look up objects
#                                                          and replaces pilot names with objectIDs.

def complete_ship_information_with_pilot_ids():
    ships_information = {}
    for ships in converting_ships_to_dict():
        ships_information[ships] = converting_ships_to_dict()[ships]
        ships_information[ships]['pilots'] = []
        ships_information[ships]['pilots'] = combine_ship_name_pilot_name()[ships]
    for keys in ships_information:
        objectids = db.characters.find({})
        for names in objectids:
            if names['name'] in ships_information[keys]['pilots']:
                for i in range(len(ships_information[keys]['pilots'])):
                    ships_information[keys]['pilots'][i] = 'ObjectID:' + str(names['_id'])
    return ships_information


# Function inserts a document into the starships collection.

def insert_into_mongo():
    for keys in complete_ship_information_with_pilot_ids():
        insert = db.starships.insert_one(complete_ship_information_with_pilot_ids()[keys])
        return insert


# These are required to close all of the files.

file.close()
pilot_file.close()
ship_data.close()
