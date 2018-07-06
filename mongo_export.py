import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mongocsv
collection = db.test_colleciton

with open('export.csv', 'w', newline = '') as csvfile:
    fieldnames = ['_id','name', 'Prefectoral capital']
    writer = csv.DictWriter(csvfile, fieldnames = fieldnames)

    for city in collection.find():
        writer.writerow(city)
