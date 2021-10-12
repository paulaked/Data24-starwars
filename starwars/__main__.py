import app.Mongo_Interaction as mongo_interactor
# Only need to import mongo_interaction as this manages the other two used classes
if __name__ == '__main__':

    # Setting the wanted database and collection name - nb this won't change what is pulled as
    # it has been tailored to fit the starships data however this allows for other modules to be written and
    # run from the same main class
    db_name = "starwars"
    collection_name = "starships"

    print(f"Beginning the \"{collection_name}\" data load with the \"{db_name}\" database...\n")

    # As the instantiation is donne in the init function, this is the only line that is needed to pull all data from
    # the API and Mongo:
    mongo = mongo_interactor.Mongo(db_name)

    print("All classes have been instantiated and required data pulled.\n"
          "Now to load the data into the collection.\n")

    # Making and populating the collection:
    mongo.make_collection(collection_name)
    mongo.populate_collection(collection_name)
    print("Process complete")
