import os
import pymongo
if os.path.exists("env.py"):
    import env


MONGO_URI = os.environ.get("MONGO_URI")
DATABASE = "<MyFirstMDB>"
COLLECTION = "MyFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB:%s") % e

conn = mongo_connect(MONGO_URI)

coll = conn[DATABASE][COLLECTION]

new_docs = [{'first': 'terry', 'last': 'pratchet', 'dob': '23/08/1972', 'gender': 'm', 'hair_colour': 'blue', 
            'occupation': 'writer', 'nationality': 'british'}, {'first': 'Billy', 'last': 'Bob', 'dob': '23/08/1975',
             'gender': 'm', 'hair_colour': 'Yellow','occupation': 'Actor', 'nationality': 'American'}]

coll.insert_many(new_docs)

documents = coll.find()

for doc in documents:
    print(doc)