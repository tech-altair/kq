from pymongo import MongoClient

def connect_to_mongodb():
    client = MongoClient('mongodb://localhost:27017/')
    db = client['sentiment_db']
    return db

def store_raw_data_in_mongodb(data):
    db = connect_to_mongodb()
    collection = db['raw_data']
    collection.insert_many(data)
