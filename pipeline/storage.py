from pymongo import MongoClient
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

# Para produção mude para MONGO_DB_PROD
url_test = os.environ.get("MONGO_DB_TEST")

if url_test is None:
    raise ValueError("A variável de ambiente MONGO_DB_TEST não foi configurada.")

# Conectar ao banco de dados MongoDB
client = MongoClient(url_test)

db = client["mood_hound"]

# Coleção para dados de PLN
global dados_pln
dados_pln = db["comments"]
stats_pln = db["stats"]


def insert(data):
    dados_pln.drop()

    df = pd.DataFrame(data)

    if not df.empty:
        df.columns = df.columns.astype(str)
        documents = df.to_dict("records")
        dados_pln.insert_many(documents)

        return (
            f"{len(documents)} documentos inseridos na coleção 'comments' com sucesso."
        )
    else:
        return "Nenhum documento inserido na coleção 'comments'."


def insert_stats(data):
    df = pd.DataFrame(data)

    if not df.empty:
        df.columns = df.columns.astype(str)
        documents = df.to_dict("records")
        stats_pln.insert_many(documents)

        return (
            f"{len(documents)} documentos inseridos na coleção 'comments' com sucesso."
        )
    else:
        return "Nenhum documento inserido na coleção 'comments'."


def update_stats(time):
    data_exist = stats_pln.find_one({})
    if data_exist:
        stats_pln.update_one(
            {"_id": data_exist["_id"]}, {"$set": {"execution_time": time}}
        )
        return "Informação atualizada"
