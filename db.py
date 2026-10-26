import os
from dotenv import load_dotenv
from pymongo import MongoClient

load_dotenv()

client = MongoClient(os.getenv("MONGO_URI"))
db = client[os.getenv("DB_NAME")]

restaurants = db.restaurants
dishes = db.dishes
users = db.users
reports = db.reports