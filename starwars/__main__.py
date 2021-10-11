import app.Mongo_Interaction as mongo_interactor

if __name__ == '__main__':

    db_name = "starwars"
    collection_name = "starships"

    print(f"Beginning the \"{collection_name}\" data load with the \"{db_name}\" database...\n")

    mongo = mongo_interactor.Mongo(db_name)

    print("All classes have been instantiated and required data pulled."
          "Now to load the data into the collection.")

    mongo.make_collection(collection_name)
    mongo.populate_collection(db_name)
    print("Process complete")
