import ExtractShipAndPilotAPIs
import requesting_sw
import starwars.app.ExtractShipAndPilotAPIs as ExtractShipAndPilotApis
import starwars.app.GetPilotName as GetPilotName
import starwars.app.GetID as GetID
import starwars.app.ReplaceAPIsWithIDs as ReplaceAPIsWithIDs
from pprint import pprint


if __name__ == '__main__':
    # start with GetFullSWInfo
    # for each element in list:
    #   input Pilot API into GetPilot to get the name
    #   use this name to search database for ID
    #   Add entry into starships collection in MongoDB
    for ship in requesting_sw.starships_list:
        # print(ship)
        ship_name_and_apis = ExtractShipAndPilotAPIs.extract_ship_pilot_and_apis(ship)
        if len(ship_name_and_apis[1]) > 0:
            id_codes = []
            for api in ship_name_and_apis[1]:
                name = GetPilotName.get_pilot_name(api)
                id_codes.append(GetID.get_ID(name)['_id'])
            updated_ship = ReplaceAPIsWithIDs.replace_apis_with_ids(ship, id_codes)
            pprint(updated_ship)
        else:
            pprint(ship)
