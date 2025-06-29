from pymongo import MongoClient
from config import MONGO_URI, DB_NAME

client = MongoClient(MONGO_URI)
db = client[DB_NAME]

def save_transcript(video_id, transcript):
    db['transcripts'].insert_one({
        'video_id': video_id,
        'transcript': transcript
    })
