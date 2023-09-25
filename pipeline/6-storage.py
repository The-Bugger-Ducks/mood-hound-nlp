import pymongo
from datetime import datetime
import pandas as pd

# Conectar ao banco de dados MongoDB
client = pymongo.MongoClient('mongodb+srv://joao:receba@clusterpln.n768zhk.mongodb.net/')  
db = client['pln']

# Coleção para dados de PLN
global dados_pln
dados_pln = db['processed_text']

def insert(data):
    dados_pln.drop()

    df = pd.DataFrame(data)

    if not df.empty:#needs to check if the df is empty
        df.columns = df.columns.astype(str)#Mongo only accepts strings
        documents = df.to_dict('records')#transform df in dictionary 
        dados_pln.insert_many(documents)

    # Fechar a conexão com o MongoDB
    client.close()

    return print(f"{len(documents)} documentos inseridos na coleção 'processed_text' com sucesso.")


