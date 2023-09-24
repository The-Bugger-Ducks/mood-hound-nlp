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

    # batch = 1000
       
    # for documents in range(0, len(data), batch):
    #     batch_data = data[documents:documents+batch].to_dict(orient='records')
    #     dados_pln.insert_many(batch_data)

    df = pd.DataFrame(data)#data is a ndarray we need to transform in dataframe


    if not df.empty:#needs to check if the df is empty
        df.columns = df.columns.astype(str)#Mongo only accepts strings
        documents = df.to_dict('records')#transform df in dictionary 
        dados_pln.insert_many(documents)

    # Fechar a conexão com o MongoDB
    client.close()

    return print(f"{len(documents)} documentos inseridos na coleção 'processed_text' com sucesso.")


