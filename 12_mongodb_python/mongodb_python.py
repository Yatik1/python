# jn1WjawKoUoV4d5Y

import pymongo

client = pymongo.MongoClient("mongodb+srv://yatiksrivastava1:jn1WjawKoUoV4d5Y@python-database.zaa1n.mongodb.net/?retryWrites=true&w=majority&appName=Python-database")

# print(client)

db = client["videosmanager"]
collection = db["vedios"]

print(collection)