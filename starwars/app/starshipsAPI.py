import starwars.config_manager as conf
import starwars.app.requesting_sw as rq

# initialisation of JSON main file and list to store data
JSON = rq.get_request(conf.SWAPI_URL)
starships_list = []

# returns a list of starships
def get_starships(URL):
    this_dict = rq.get_request(URL)
    NEXT_PAGE_URL = this_dict["next"]
    for item in this_dict["results"]:
        starships_list.append(item)
    if NEXT_PAGE_URL:
        # recursive approach to extract the next list of starships
        # works until NEXT_PAGE is empty what means that there are no more starships to store
        get_starships(NEXT_PAGE_URL)
    return starships_list

