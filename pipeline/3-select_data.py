# =============================================================================
# Organizando avaliações pelo grau de classificação (positiva, neutra ou negativa)
# =============================================================================
import pandas as pd
import numpy as np
import os
import sys
utils_path = os.getcwd() + '/utils'
sys.path.insert(0, utils_path)
import random_select

def select_data(df):
  positive = random_select.select(100, df, 'POSITIVO', 3000)
  negative = random_select.select(100, df, 'NEGATIVO', 3000)
  select = np.concatenate([positive, negative])

  df = df[df['text'].isin(select)].reset_index(drop=True)
  df = df.sample(frac=1).reset_index(drop=True)

  print('-----------------------------------------------------------------------------')
  print(df['sentiment'].value_counts(normalize=True))

  return df

def select_training_data(df):
  positive = random_select.select(21, df, 'POSITIVO', 60)
  negative = random_select.select(21, df, 'NEGATIVO', 40)
  select = np.concatenate([positive, negative])

  df = df[df['text'].isin(select)].reset_index(drop=True)
  df = df.sample(frac=1).reset_index(drop=True)

  print('-----------------------------------------------------------------------------')
  print(df['sentiment'].value_counts(normalize=True))

  return df