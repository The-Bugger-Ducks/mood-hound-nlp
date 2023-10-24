from pymongo import MongoClient
import pandas as pd

def insert(data, default_client = MongoClient('mongoDatabaseURL') ):
  # Conectar ao banco de dados MongoDB
  client = default_client

  # Coleção para dados de PLN
  db = client['mood_hound']
  dados_pln = db['comments']
  
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
