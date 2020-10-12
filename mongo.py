import pymongo
import os
if os.path.exists("env.py"):
    import env

MONGODB_URI = os.environ.get("MONGO_URI")
DBS_NAME = "myTestDB"
COLLECTION = "myFirstMDB"


def mongo_connect(url):
    try:
        conn = pymongo.MongoClient(url)
        print("Mongo is connected!")
        return conn
    except pymongo.errors.ConnectionFailure as e:
        print("Could not connect to MongoDB: %s") % e
        

conn = mongo_connect(MONGODB_URI)

coll = conn[DBS_NAME][COLLECTION]

documents = coll.find()

for doc in documents:
    print(doc)