import unittest
import pandas as pd

from pipeline.clear_data import clear_data

class TestClearData(unittest.TestCase):
    def mock(self):
        data = {
            "overall_rating": [5, 3, 1, 1],
            "review_text": [
                "Gostei do produto muito bonito, e pratico para instalar.",
                "Funciona bem, leve, poderia ter mira leser ter vindo também uma serra para ferro",
                None,
                "Após inúmeras compras com sucesso na Americanas.com, essa não tive sorte. Produto veio com peça faltando e o vendedor não responde minhas tentativas de contato. Me pediram 2 dias úteis",
            ],
            "submission_date": [
                "2018-04-29T06:01:00.000+00:00",
                "2018-02-28T16:38:41.000+00:00",
                "2018-01-12T13:13:35.000+00:00",
                "2018-05-30T07:06:43.000+00:00",
            ],
            "reviewer_id": None,
            "product_brand": None,
            "site_category_lv1": None,
            "site_category_lv2": None,
            "review_title": None,
            "recommend_to_a_friend": None,
            "reviewer_birth_year": None,
            "reviewer_gender": None,
        }

        self.df = pd.DataFrame(data)

    def test_clear_data(self):
        self.mock()
        df = clear_data(self.df)

        self.assertTrue("sentiment" in df.columns)
        self.assertTrue("created_at" in df.columns)
        self.assertTrue("text" in df.columns)
        self.assertTrue(df["text"].str.contains("\w").sum())
        self.assertTrue((df["text"].str.len() > 3).sum())


if __name__ == "__main__":
    unittest.main()
