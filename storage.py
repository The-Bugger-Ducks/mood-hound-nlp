import pymongo
from datetime import datetime
import uuid

# Conectar ao banco de dados MongoDB
client = pymongo.MongoClient('mongodb+srv://joao:receba@clusterpln.n768zhk.mongodb.net/')  
db = client['pln']

# Coleção para dados de PLN
global dados_pln
dados_pln = db['processed_text']

def insert():
    dados_pln.drop()
    # Lista de documentos pre-processados
    documentos = [
        {
            'id': str(uuid.uuid4()),  
            'text': 'Este é o texto processado 1.',
            'topic': 'Tópico A',
            'sentiment': 'Positivo',
            'rating': 5,
            'product_id': '789asd7d98asasdasd44',
            'product_name': 'Notebook muito foda',
            'created_at': str(datetime.now().timestamp())  
        },
        {
            'id': str(uuid.uuid4()),
            'text': 'Este é o texto processado 2.',
            'topic': 'Tópico B',
            'sentiment': 'Negativo',
            'rating': 3,
            'product_id': '789asd7d98asasdasd44',
            'product_name': 'Galaxy pocket',
            'created_at': str(datetime.now().timestamp()) 
        },
    ]

    dados_pln.insert_many(documentos)

    print(f"{len(documentos)} documentos inseridos na coleção 'dados_pln' com sucesso.")

    # Fechar a conexão com o MongoDB
    client.close()


insert()

