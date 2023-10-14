import unittest
import pandas as pd

import os
import sys

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

import pipeline.access_data as access

class TestDataAcess(unittest.TestCase):
  
  def acess_data_test(self):
    try:
      data = access.access_data()
    except Exception as e:
      self.fail(f"Não foi possível acessar:{e} ")
    self.assertIsInstance(data,pd.DataFrame)
    

if __name__ == '__main__':
    unittest.main()
