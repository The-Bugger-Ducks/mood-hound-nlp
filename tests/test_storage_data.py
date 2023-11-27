import unittest
from pymongo import MongoClient
import pandas as pd

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

import pipeline.storage as store


class TestStoreData(unittest.TestCase):
    def test_insert_with_valid_data(self):
        data = {
            "sentiment": ["POSITIVE", "NEUTRAL", "NEGATIVE"],
            "text": [
                "Gostei do produto muito bonito, e pratico para instalar.",
                "Funciona bem, leve, poderia ter mira leser ter vindo também uma serra para ferro",
                "Após inúmeras compras com sucesso na Americanas.com, essa não tive sorte. Produto veio com peça faltando e o vendedor não responde minhas tentativas de contato. Me pediram 2 dias úteis",
            ],
        }
        df = pd.DataFrame(data)
        result = store.insert(df)

        self.assertEqual(
            result, "3 documentos inseridos na coleção 'comments' com sucesso."
        )

    def test_insert_with_empty_data(self):
        data = []
        result = store.insert(data)
        self.assertEqual(result, "Nenhum documento inserido na coleção 'comments'.")

    def test_insert_stats(self):
        data = {
            "model_accuracy": [0.3],
            "model_precision":[0.3], 
        }

        result = store.insert_stats(data)

        self.assertEqual(
            result, "1 documentos inseridos na coleção 'stats' com sucesso."
        )

    def test_update_stats(self):
        result = store.update_stats(10)

        
        self.assertEqual(
            result, "Informação atualizada"
        )



if __name__ == "__main__":
    unittest.main()
