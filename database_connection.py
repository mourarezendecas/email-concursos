import os 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi


client = MongoClient(os.getenv("ATLAS_URI"), server_api=ServerApi('1'))

collection = client['users-mail']['usuarios']

def insert(usuario): 
    try:
        inserted_data = collection.insert_one(usuario)
        client.close
        return inserted_data.inserted_id
    except Exception as e:
        client.close
        print(e)
        return None
    

def get_users():
    try:
        users = collection.find()
        client.close
        return users
    except Exception as e:
        client.close
        print(e)
        return None
    
def get_emails():
    users = get_users()
    email_list = []
    for user in users:
        email_list.append(user.get('email'))
    return email_list