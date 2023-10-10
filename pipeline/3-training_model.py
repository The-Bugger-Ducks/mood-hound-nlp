# =============================================================================
# Treinando o modelo
# =============================================================================
import pandas as pd
import numpy as np
select = __import__('3-select_data')

def training(df):
  training_data = select.select_training_data(df)
  print('-----------------------------------------------------------------------------')
  print(training_data['text'])