from pymongo import MongoClient
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGODB_URL")

client = MongoClient(MONGO_URL)
db = client["edura_users"]


admin_tb = db["admins"]
teacher_tb = db["teachers"]
student_tb = db["students"]