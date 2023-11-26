import unittest
import pandas as pd

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

import pipeline.processing as process


class TestDataSelect(unittest.TestCase):
    def test_process_data(self):
        data = {
            "text": [
                "Gostei do produto muito bonito, e pratico para instalar.",
                "Funciona bem, leve, poderia ter mira leser ter vindo também uma serra para ferro",
                "Após inúmeras compras com sucesso na Americanas.com, essa não tive sorte. Produto veio com peça faltando e o vendedor não responde minhas tentativas de contato. Me pediram 2 dias úteis",
                "Entrega rápida, aparelho cilencioso, gela muito. Ainda não tenho valor da conta de energia para opinar consumo.",
                "Estes copos sao de diamante e ouro? Ja foi vendido algum?",
                "Fácil instalação,  acabamento incrível,  entrega dentro do prazo e excelentes condições...",
                "Muito prático e permite pegar maior peso sem sofrer tanto nas mãos.",
                "Chegou antes do previsto para a entrega estão de parabéns",
                "Apenas configurar ela corretamente para aproveitar o máximo da TV!",
                "ótimo produto recomendo! mas a entrega atrasou pelo fato de ter sido feriado no ultimo dia!",
                "Estava com medo de usar toner compatível, mas que experiencia maravilhosa! Otimo produto.",
            ],
        }

        topic_limit = 4
        df_mock = pd.DataFrame(data)
        df_test = process.processing(df_mock, topic_limit)

        self.assertTrue("topic" in df_test.columns)

        topicts = set(
            [
                "QUALIDADE",
                "RECEBIMENTO",
                "ENTREGA",
                "EXPECTATIVA",
                "SATISFAÇÃO",
                "CUSTO BENEFÍCIO",
                "RECOMENDAÇÃO",
            ]
        )

        self.assertTrue(all(label in topicts for label in df_test["topic"]))


if __name__ == "__main__":
    unittest.main()
