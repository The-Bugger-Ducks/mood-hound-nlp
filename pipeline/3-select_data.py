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
  positive = df[df['sentiment'] >= 4] # 4 e 5 "estrelas"
  neutral = df[df['sentiment'] == 3] # 3 "estrelas"
  negative = df[df['sentiment'] <= 2] # 1 e 2 "estrelas"

  df = pd.concat([positive, neutral, negative])
  ratings_maping = {
    5: 'POSITIVO', 
    4: 'POSITIVO', 
    3: 'NEUTRO', 
    2: 'NEGATIVO', 
    1: 'NEGATIVO'
  }
  df = df.replace(ratings_maping)

  positive = random_select.select(100, df, 'POSITIVO', 15000)
  neutral = random_select.select(100, df, 'NEUTRO', 15000)
  negative = random_select.select(100, df, 'NEGATIVO', 15000)
  select = np.concatenate([positive, neutral, negative])

  df = df[df['text'].isin(select)].reset_index(drop=True)
  df = df.sample(frac=1).reset_index(drop=True)

  print('-----------------------------------------------------------------------------')
  print(df['sentiment'].value_counts(normalize=True))

  return df

def select_training_data(df):
  positive = random_select.select(21, df, 'POSITIVO', 60)
  neutral = random_select.select(21, df, 'NEUTRO', 10)
  negative = random_select.select(21, df, 'NEGATIVO', 30)
  select = np.concatenate([positive, neutral, negative])

  df = df[df['text'].isin(select)].reset_index(drop=True)
  df = df.sample(frac=1).reset_index(drop=True)

  print('-----------------------------------------------------------------------------')
  print(df['sentiment'].value_counts(normalize=True))

  return df