import pymongo
import requests


def get_info(pg_num: int, key_name: str, cat: str):

    url = f'https://swapi.dev/api/{cat}/{pg_num}/'
    info = requests.get(url)
    info_values = info.json()[key_name]
    return info_values


def secondary_number_list(pg_num: int, cat: str, secondary_key_name: str):

    secondary_list = []
    list_ = get_info(pg_num, secondary_key_name, cat)

    for i in range(len(list_)):
        secondary_list.append(list_[i].split('/')[5].strip())

    return secondary_list


def get_pilot(pg_num: int):

    pilot_number_list = secondary_number_list(pg_num, 'starships', 'pilots')
    pilots = []

    for i in pilot_number_list:

        pilots.append(get_info(i, 'name', 'people'))

    return pilots


def get_pilot_object_ids(pg_num: int):

    client = pymongo.MongoClient()
    db = client["StarWars"]

    pilot_list = get_pilot(pg_num)
    p_id_list = []
    pilot_id_list = []

    for i in pilot_list:

        character_id = db.characters.find_one({"name": i}, {"_id": 1})
        char_id_num = str(character_id["_id"])
        pilot_id_list.append(char_id_num)

    return pilot_id_list


#
# list = get_info(10,'pilots','starships')
# print(list[0].split('/')[5].strip())
# print(secondary_number_list(10,'starships','pilots'))
print(get_pilot_object_ids(10))
