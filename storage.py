import pymongo
from datetime import datetime
import uuid

# Conectar ao banco de dados MongoDB
client = pymongo.MongoClient('mongo cluster connection')  
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
            'text': 'Notebook de boa qualidade',
            'topic': 'Tópico A',
            'sentiment': 'Positivo',
            'rating': 5,
            'product_id': 'w3i4578tu',
            'product_name': 'Notebook',
            'created_at': '2018-01-01',  
            'added_at': str(datetime.now().timestamp())  
        },
        {
            'id': str(uuid.uuid4()),
            'text': 'Não durou muito',
            'topic': 'Tópico B',
            'sentiment': 'Negativo',
            'rating': 3,
            'product_id': '789wetg',
            'product_name': 'Galaxy pocket',
            'created_at': '2018-04-05',  
            'added_at': str(datetime.now().timestamp()) 
        },
        {
            'id': str(uuid.uuid4()),  
            'text': 'Fez o que era pedido',
            'topic': 'Tópico A',
            'sentiment': 'Mediano',
            'rating': 3,
            'product_id': 'btye45yb',
            'product_name': 'Betobeira',
            'created_at': '2018-09-07',  
            'added_at': str(datetime.now().timestamp())  
        },
        {
            'id': str(uuid.uuid4()),
            'text': 'Otima qualidade',
            'topic': 'Tópico B',
            'sentiment': 'Positivo',
            'rating': 4,
            'product_id': 'b54yb5y4',
            'product_name': 'Relogio',
            'created_at': '2019-03-03',  
            'added_at': str(datetime.now().timestamp()) 
        },
        {
            'id': str(uuid.uuid4()),  
            'text': 'Tecido fraco',
            'topic': 'Tópico A',
            'sentiment': 'Negativo',
            'rating': 2,
            'product_id': 'b4545b',
            'product_name': 'Sapatos',
            'created_at': '2019-10-11',  
            'added_at': str(datetime.now().timestamp())  
        },
        {
            'id': str(uuid.uuid4()),
            'text': 'Veio arranhado',
            'topic': 'Tópico B',
            'sentiment': 'Negativo',
            'rating': 1,
            'product_id': 'b4545b',
            'product_name': 'Monitor',
            'created_at': '2019-12-23',  
            'added_at': str(datetime.now().timestamp()) 
        },
        {
            'id': str(uuid.uuid4()),  
            'text': 'Grande e firme',
            'topic': 'Tópico A',
            'sentiment': 'Positivo',
            'rating': 5,
            'product_id': 'b3434bb5a',
            'product_name': 'Mesa',
            'created_at': '2020-01-15',  
            'added_at': str(datetime.now().timestamp())  
        },
        {
            'id': str(uuid.uuid4()),
            'text': 'Está trincado',
            'topic': 'Tópico B',
            'sentiment': 'Negativo',
            'rating': 2,
            'product_id': 'qb5yq5ybq5',
            'product_name': 'Copo',
            'created_at': '2020-06-04',  
            'added_at': str(datetime.now().timestamp()) 
        },
        {
            'id': str(uuid.uuid4()),  
            'text': 'Bom material',
            'topic': 'Tópico A',
            'sentiment': 'Positivo',
            'rating': 4,
            'product_id': 'qb453yq5b',
            'product_name': 'Guarrafa',
            'created_at': '2020-11-11',  
            'added_at': str(datetime.now().timestamp())  
        },
        {
            'id': str(uuid.uuid4()),
            'text': 'Muito curto',
            'topic': 'Tópico A',
            'sentiment': 'Negativo',
            'rating': 2,
            'product_id': 'rabrbgbg',
            'product_name': 'Cabo',
            'created_at': '2021-02-17',  
            'added_at': str(datetime.now().timestamp()) 
        },
        {
            'id': str(uuid.uuid4()),  
            'text': 'Esperava mais, mas até que é legal',
            'topic': 'Tópico A',
            'sentiment': 'Mediano',
            'rating': 3,
            'product_id': 'ab5byabyb',
            'product_name': 'Tapete',
            'created_at': '2021-05-10',  
            'added_at': str(datetime.now().timestamp())  
        },
        {
            'id': str(uuid.uuid4()),
            'text': 'Cola não durou',
            'topic': 'Tópico B',
            'sentiment': 'Negativo',
            'rating': 1,
            'product_id': 'ab6b45yba',
            'product_name': 'Adesivo',
            'created_at': '2021-09-01',  
            'added_at': str(datetime.now().timestamp()) 
        },
        {
            'id': str(uuid.uuid4()),  
            'text': 'Melhor console, tudo OK',
            'topic': 'Tópico A',
            'sentiment': 'Positivo',
            'rating': 4,
            'product_id': 'ab5by5by',
            'product_name': 'Xbox 360',
            'created_at': '2022-04-01',  
            'added_at': str(datetime.now().timestamp())  
        },
        {
            'id': str(uuid.uuid4()),
            'text': 'Pessimo qualidade abaixo do esperado',
            'topic': 'Tópico B',
            'sentiment': 'Negativo',
            'rating': 1,
            'product_id': 'ab5bybab',
            'product_name': 'PS4',
            'created_at': '2022-07-10',  
            'added_at': str(datetime.now().timestamp()) 
        },
        {
            'id': str(uuid.uuid4()),  
            'text': 'Qualidade absurda',
            'topic': 'Tópico A',
            'sentiment': 'Positivo',
            'rating': 5,
            'product_id': 'ba5yb5yb',
            'product_name': 'Tv AOC',
            'created_at': '2022-08-20',  
            'added_at': str(datetime.now().timestamp())  
        },
        {
            'id': str(uuid.uuid4()),
            'text': 'Muito pequena, mas serviu',
            'topic': 'Tópico B',
            'sentiment': 'Mediano',
            'rating': 3,
            'product_id': 'ba5yba pocket',
            'product_name': 'Caixa Inox',
            'created_at': '2023-02-14',  
            'added_at': str(datetime.now().timestamp()) 
        },
        {
            'id': str(uuid.uuid4()),  
            'text': 'Otimo vendedor',
            'topic': 'Tópico A',
            'sentiment': 'Positivo',
            'rating': 5,
            'product_id': 'brgbrgbgb',
            'product_name': 'Pringles',
            'created_at': '2023-06-13',   
            'added_at': str(datetime.now().timestamp())  
        },
        {
            'id': str(uuid.uuid4()),
            'text': 'Veio rasgado, demora na entrega',
            'topic': 'Tópico B',
            'sentiment': 'Negativo',
            'rating': 2,
            'product_id': 'ab5y5b5yba',
            'product_name': 'Livro',
            'created_at': '2023-08-12',  
            'added_at': str(datetime.now().timestamp()) 
        },
    ]

    dados_pln.insert_many(documentos)

    print(f"{len(documentos)} documentos inseridos na coleção 'dados_pln' com sucesso.")

    # Fechar a conexão com o MongoDB
    client.close()


insert()

