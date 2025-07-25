from pymongo import MongoClient

MONGO_URI = "mongodb://localhost:27017/"
DB_NAME = "mlops_db"
COLLECTION_NAME = "customers"

client = MongoClient(MONGO_URI)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]