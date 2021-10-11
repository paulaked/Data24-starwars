import starwars.app.requesting_sw as rqst


# Please run this file.

print(rqst.complete_ship_information_with_pilot_ids())

# Only run this function if you would like to insert documents into mongodb.

# rqst.insert_into_mongo()

# ------------------------------------ Need to call these function if you get new data ----------------------

# generate_txt_file_with_data(dictionary_of_ships_with_pilots_URL())

# generate_txt_file_with_pilots_url(requests_data_from_pilots_url())

# generate_txt_file_with_ship_information(dictionary_of_all_ships())
