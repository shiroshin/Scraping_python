from pymongo import MongoClient
import datetime
client = MongoClient('localhost', 27017)

db = client.mongotest
collection = db.test_colleciton

post = {"author": "Mike",
        "text": "My first blog post!",
        "tags": ["mongodb", "python", "pymongo"],
        "date": datetime.datetime.utcnow()}

result1 = collection.insert_one(post)

new_posts = [{"author": "Mike",
              "text": "Another post!",
              "tags":["bulk", "insert"],
              "date": datetime.datetime(2009, 11, 12, 11, 14)},
             {"author": "Eliot",
              "title": "MongoDB is fun",
              "text": "and pretty easy too !",
              "date": datetime.datetime(2009, 11, 10, 10, 45)}]

result2 = collection.insert_many(new_posts)

print(collection.find_one({"author": "Mike"}))

for post in collection.find():
    print(post)
