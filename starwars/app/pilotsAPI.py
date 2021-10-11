import starwars.config_manager as conf
import starwars.app.starshipsAPI as sapi
import starwars.app.requesting_sw as rq
import starwars.app.mongoClient as mc


JSON = rq.get_request(conf.SWAPI_URL)

# Returns a list of pilots' URLS that directs to the content and information about sppecific pilot
def get_pilots_URLs(URL):
    # get a starships collection to extract pilots info
    pilots_list = []
    starships = sapi.get_starships(URL['starships'])
    for item in starships:
        for j in item["pilots"]:
            pilots_list.append(j)
    return pilots_list



# Returns a dict of specific pilot from URL
def get_pilot_name(pilot_URL):
    pilot = rq.get_request(pilot_URL)
    return pilot['name']


# Returns a collection of characters from local starwars database
def get_pilots_list_mongo(database):
    return database.characters.find({})



# Returns a ID from local mongo starwars database with matching name
def get_pilot_ID(name: str):
    database = mc.get_Mongo_Client()
    characters = get_pilots_list_mongo(database)
    for item in characters:
        if item['name'] == name:
            string = "ObjectId(\'" + str(item["_id"]) + "\')"
            return string

# converts URLs to dicts
def convert_URL_to_ID_pilots(pilots_URLs_List: list):
    pilots_list = []
    for i in range(len(pilots_URLs_List)):
        pilot_URL = pilots_URLs_List[i]
        name = get_pilot_name(pilot_URL)
        id = get_pilot_ID(name)
        pilots_list.append(id)

    return pilots_list


