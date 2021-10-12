from file1 import *  # File with functions to extract and upload data to MongoDB database.

Database = 'StarWars'  # Naming the Database and Collection that I want to access
Collection = 'starships'

create_collection(Database, Collection)  # Create Collection in Database

for i in range(100):

    # Cycles through all the records on the URL to collect all the names of starships.

    try:

        starship = get_info(i, 'name', 'starships')
        pilot = get_pilot_object_ids(i)
        add_starship_document(Database, Collection, starship, pilot)

        # Main bulk of program, where the information selected is extracted from the URL and
        # added to the MongoDB database.

    except Exception:

        # If the page number has no associated data with it continues to next page.

        pass
