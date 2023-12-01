import unittest
import pandas as pd
import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, project_root)

from pipeline.pre_processing import pre_processing


class TestPreProcessing(unittest.TestCase):
  def test_pre_processing(self):
   data = pd.DataFrame({"text": ["Gostei do produto muito bonito, e pratico para instalar", "Chegou antes do previsto para a entrega estão de parabéns"]})

   result_df = pre_processing(data)

   self.assertIn("corpus", result_df.columns)

   self.assertEqual(len(result_df), len(data))

   expected_corpus = ["gostar produto bonito pratico instalar", "chegar prever entregar parabéns"]
   actual_corpus = result_df["corpus"].tolist()
   self.assertEqual(actual_corpus, expected_corpus)


if __name__ == "__main__":
    unittest.main()
