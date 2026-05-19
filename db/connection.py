from pymongo import MongoClient # pyright: ignore[reportMissingImports]
# import dotenv
import os

def get_db():
   
    client = MongoClient(os.getenv('MONGO_URI'))
    db = client['TalentTrend']
    print("Connected to MongoDB")
    return db

get_db()