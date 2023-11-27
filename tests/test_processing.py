# import unittest
# import pandas as pd
# import os
# import sys

# project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
# sys.path.insert(0, project_root)

# from pipeline.processing import processing


# class TestProcessing(unittest.TestCase):
#     def test_processing(self):
#         data = pd.DataFrame(
#             {
#               'corpus': ["Gostei do produto muito bonito, e pratico para instalar", "Chegou antes do previsto para a entrega estão de parabéns"],
#               'text':["Gostei do produto muito bonito, e pratico para instalar", "Chegou antes do previsto para a entrega estão de parabéns"],
#               'stars': [5, 5]
#             }
#         )
        
#         result_df = processing(data)

#         self.assertIn("sentiment", result_df.columns)
#         self.assertIn("topic", result_df.columns)

#         self.assertEqual(len(result_df), len(data))


# if __name__ == "__main__":
#     unittest.main()
