import json
from pymongo import MongoClient

client = MongoClient('localhost', 27017)
db = client['books']
books = db.books

# books.delete_many({})
# with open('books.json', 'r') as f:
#     data = json.load(f)
#
# _id = 0
# for book in data:
#     _id += 1
#     book['_id'] = _id
#     try:
#         books.insert_one(book)
#     except:
#         print(book)

"""Изменения стоимости с str на float"""
count = 0
bad_count = 0

for book in books.find({}):
    try:
        old_price = book["price"]
        new_price = {'price': float(book["price"])}
        books.update_one({'price': old_price}, {'$set': new_price})
        count += 1
    except:
        bad_count += 1

print(f'Количество измененных документов {count}')
print(f'Количество неизмененных документов {bad_count}')
