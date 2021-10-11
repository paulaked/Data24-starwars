# takes in a dictionary of the ship info and replaces the pilot value with the list obtained prior

def replace_apis_with_ids(ship_dict, pilots_list) -> dict:
    ship_dict["pilots"] = pilots_list
    return ship_dict


# print(replace_apis_with_ids({"pilots": []}, ["1","2","3"]))