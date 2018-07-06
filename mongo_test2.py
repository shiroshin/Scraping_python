from pymongo import MongoClient
import sys

args = sys.argv
client = MongoClient('localhost',27017)

db = client.mongocsv

collection = db.test_colleciton
print(collection.count())
for result in collection.find({"name": args[1]}):
    print(result)
