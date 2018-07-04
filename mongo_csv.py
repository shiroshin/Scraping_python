# -*- coding:utf^8 -*-
import csv
from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client.mongocsv
collection = db.test_colleciton

datafile = open('import.csv' , 'r')
fieldnames =('name', 'Prefectoral capital')

line = csv.DictReader(datafile, fieldnames = fieldnames,delimiter = ','  )

for data in line:
    collection.insert(data)

datafile.close()

for na in collection.find():
    print(na)
