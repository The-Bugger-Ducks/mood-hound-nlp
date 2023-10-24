import unittest
from pymongo import MongoClient
import pandas as pd

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import pipeline.storage as store

#Banco para testes unitários
global client
client = MongoClient('mongodb+srv://joao:Mck9WH61qPA40dZe@clusterpln.n768zhk.mongodb.net/') 


class TestStoreData(unittest.TestCase):
  def test_insert_with_valid_data(self):
    data = {
      "sentiment":['POSITIVE','NEUTRAL','NEGATIVE'],
      "text":[
        'Gostei do produto muito bonito, e pratico para instalar.', 
        'Funciona bem, leve, poderia ter mira leser ter vindo também uma serra para ferro',
        'Após inúmeras compras com sucesso na Americanas.com, essa não tive sorte. Produto veio com peça faltando e o vendedor não responde minhas tentativas de contato. Me pediram 2 dias úteis'
      ]
    }
    df = pd.DataFrame(data)
    result = store.insert(df, client)

    self.assertEqual(result, "3 documentos inseridos na coleção 'comments' com sucesso.")

  def test_insert_with_empty_data(self):
    data = []  
    result = store.insert(data, client)
    self.assertEqual(result, "Nenhum documento inserido na coleção 'comments'.")

if __name__ == '__main__':
    unittest.main()
  




