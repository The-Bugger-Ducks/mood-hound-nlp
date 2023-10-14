import unittest
import pandas as pd

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '../'))
sys.path.insert(0, project_root)

import pipeline.clear_data as clear


class TestDataAcess(unittest.TestCase):
  def mock(self):
    data: {
      "overall_rating":[5,3,1,1],
      "review_text":[
        'Gostei do produto muito bonito, e pratico para instalar.', 
        'Funciona bem, leve, poderia ter mira leser ter vindo também uma serra para ferro',
        None,
        'Após inúmeras compras com sucesso na Americanas.com, essa não tive sorte. Produto veio com peça faltando e o vendedor não responde minhas tentativas de contato. Me pediram 2 dias úteis'
      ],
      "submission_date":['2018-05-08T19', '2018-03-27T08',' 2018-03-05T08', '2018-05-25T10']    
    }

    self.df = pd.DataFrame(data)
    


  def clear_data_test(self):
    df = clear.clear_data(self.df)


    self.assertTrue('sentiment' in df.columns)
    self.assertTrue('created_at' in df.columns)
    self.assertTrue('text' in df.columns)
    self.assertTrue(df['text'].isnull().sum())
    self.assertTrue(df['text'].str.contains("\w").sum())
    self.assertTrue((df['text'].str.len() > 3).sum())

    

if __name__ == '__main__':
    unittest.main()



    

  
  