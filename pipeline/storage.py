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

current_stats_id = None


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
    global current_stats_id

    df = pd.DataFrame(data)

    if not df.empty:
        df.columns = df.columns.astype(str)
        documents = df.to_dict("records")

        result = stats_pln.insert_many(documents)

        if result.inserted_ids:
            current_stats_id = result.inserted_ids[0]

            return (
                f"{len(documents)} documentos inseridos na coleção 'stats' com sucesso. "
            )
        else:
            return "Erro ao inserir documentos na coleção 'stats'."
    else:
        return "Nenhum documento inserido na coleção 'stats'."


def update_stats(payload):
    global current_stats_id
    if current_stats_id:
        stats_pln.update_one({"_id": current_stats_id}, {"$push": payload})
        return "Informação atualizada"
    else:
        return "Erro: ID do documento não encontrado. Insert_stats não foi executado."
