from pymongo import MongoClient

def get_db():
    uri = "mongodb+srv://Misael:m988168455@cluster0.iovvghc.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
    client = MongoClient(uri)
    db = client["biblioteca_digital"]
    return db
