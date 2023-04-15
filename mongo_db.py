from pymongo import MongoClient
class MongoDB:
    def __init__(self, uri, db_name, collection_name):
        self.client = MongoClient("mongodb://127.0.0.1:27017")
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def insert_one(self, document):
        self.collection.insert_one(document)

    def find_one(self, query):
        return self.collection.find_one(query)






