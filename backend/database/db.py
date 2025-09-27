import os
from dotenv import load_dotenv
load_dotenv()

from pymongo import MongoClient

URL = os.getenv("MONGODB_URL")

client = MongoClient(URL)
database = client["dsms"]

def mongodb(collection: str):
    db = database[collection]

    return db