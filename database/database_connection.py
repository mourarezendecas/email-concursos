import os 
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

client = MongoClient(os.getenv("ATLAS_URI"), server_api=ServerApi('1'))

collection = client['users-mail']['usuarios']

def insert(usuario): 
    print("Inserindo usuario na base de dados")
    try:
        inserted_data = collection.insert_one(usuario)
        client.close
        print("Usuario inserido com sucesso!!!")
        return inserted_data.inserted_id
    except Exception as e:
        client.close
        print(f"Nao foi possivel inserir o usuario na base dados: {e}!!!")
        return None
    

def get_users():
    print("Solicitando a lista de usuarios da base de dados")
    try:
        users = collection.find()
        client.close
        print("Lista de usuarios da base de dados obtida com sucesso!!!")
        return users
    except Exception as e:
        client.close
        print(f"Nao foi possivel obter a lista de usuarios: {e}!!!")
        return None
    
def get_emails():
    users = get_users()
    email_list = []
    for user in users:
        email_list.append(user.get('email'))
    print(f"{len(email_list)} usuarios encontrados...")
    return email_list


# usuario = {
#     "name" : "",
#     "email" : ""
# }

# insert(usuario)