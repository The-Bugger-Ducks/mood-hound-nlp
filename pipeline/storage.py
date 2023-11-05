from pymongo import MongoClient
import pandas as pd

# Conectar ao banco de dados MongoDB
client = MongoClient('mongoDatabaseURL')  

db = client['mood_hound']

# Coleção para dados de PLN
global dados_pln
dados_pln = db['comments']

def insert(data):
  dados_pln.drop()

  df = pd.DataFrame(data)

  if not df.empty: 
    df.columns = df.columns.astype(str) 
    documents = df.to_dict('records')
    dados_pln.insert_many(documents)

    # Fechar a conexão com o MongoDB
    client.close()

    return f"{len(documents)} documentos inseridos na coleção 'comments' com sucesso."
  else:
    return "Nenhum documento inserido na coleção 'comments'."