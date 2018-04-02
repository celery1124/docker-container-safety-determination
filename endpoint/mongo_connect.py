import pymongo
import constants

def connectMongo():
	url = "mongodb://" + constants.host + "/" + constants.db
	print(url)
	client = pymongo.MongoClient(url)
	print(client)
	db = client[constants.db]
	collection = db[constants.collection]
	return collection

