import starwars.config_manager as conf
import starwars.app.requesting_sw as rq
import starwars.app.pilotsAPI as papi
import starwars.app.starshipsAPI as sapi




# create a starship based on URL
# takes a list of Pilots' URLs and converts them to list of ObjectIDs from mongo local database
def create_starship(API_starship_dict: dict):
    starship = API_starship_dict
    pilots = starship["pilots"]
    if pilots:
        converted_pilot_list = papi.convert_URL_to_ID_pilots(pilots)
        new_pilots = {"pilots": converted_pilot_list}
        starship.update(new_pilots)
        return starship
    else:
        return starship

# inserts list of starships to database
def insert_to_database(database, starships):
    database.starships.insert_many(starships)


# creates a list of starships to insert and print
def create_list_of_starships():
    JSON = rq.get_request(conf.SWAPI_URL)
    STARSHIPS = sapi.get_starships(JSON["starships"])
    new_list = []
    for i in STARSHIPS:
        new_list.append(create_starship(i))
    return new_list


# prints out the list of starships with ObjectIDs of pilots
def run_app():
    l = create_list_of_starships()
    for i in l:
        print(i)






# database = mc.get_Mongo_Client()
# insert_to_database(database, create_list_of_starships())
#
