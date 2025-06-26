from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017")
db = client["super_xandao_youtube"]
collection = db["videos"]

def insert_video_data(data):
    if collection.find_one({"video_id": data["video_id"]}) is None:
        collection.insert_one(data)
