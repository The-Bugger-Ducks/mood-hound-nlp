import pymongo
from datetime import datetime
import uuid

# Conectar ao banco de dados MongoDB
client = pymongo.MongoClient('mongodb+srv://joao:receba@clusterpln.n768zhk.mongodb.net/')  
db = client['pln']

# Coleção para dados de PLN
global dados_pln
dados_pln = db['processed_text']


class DadoPLN:
    def __init__(self, id:str ,text:str ,topic:str,sentiment:str,rating:int , product_id:str, product_name:str, created_at:str):
        self.id = str(uuid.uuid4()) 
        self.text = text
        self.topic = topic
        self.sentiment = sentiment
        self.rating = rating
        self.product_id = product_id
        self.product_name = product_name
        self.created_at = str(datetime.now().timestamp())


def insert():
    dados_pln.drop()
    # Lista de documentos pre-processados
    # documentos = [
    #     {
    #         'id': str(uuid.uuid4()),  
    #         'text': 'Este é o texto processado 1.',
    #         'topic': 'Tópico A',
    #         'sentiment': 'Positivo',
    #         'rating': 5,
    #         'product_id': '789asd7d98asasdasd44',
    #         'product_name': 'Notebook muito foda',
    #         'created_at': str(datetime.now().timestamp())  
    #     },
    #     {
    #         'id': str(uuid.uuid4()),
    #         'text': 'Este é o texto processado 2.',
    #         'topic': 'Tópico B',
    #         'sentiment': 'Negativo',
    #         'rating': 3,
    #         'product_id': '789asd7d98asasdasd44',
    #         'product_name': 'Galaxy pocket',
    #         'created_at': str(datetime.now().timestamp()) 
    #     },
    # ]

    documentos = DadoPLN(id=1, text= 'Este é o texto processado 2.',topic= 'Tópico B',sentiment= 'Negativo', rating= 3, product_id= '789asd7d98asasdasd44',product_name= 'Galaxy pocket',created_at= str(datetime.now().timestamp()))
    var = vars(documentos)
    print(var)

    # dados_pln.insert_many(documentos)

    # print(f"{len(documentos)} documentos inseridos na coleção 'dados_pln' com sucesso.")

    # Fechar a conexão com o MongoDB
    client.close()




insert()

