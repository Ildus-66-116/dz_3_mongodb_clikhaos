import requests
import json
from pymongo import MongoClient
from pprint import pprint
from pymongo.errors import *

client = MongoClient('localhost', 27017)
db = client['books']
books = db.books
books.delete_many({})

with open('books.json', 'r') as f:
    data = json.load(f)

_id = 0
for book in data:
    _id += 1
    book['_id'] = _id
    try:
        books.insert_one(book)
    except:
        print(book)
