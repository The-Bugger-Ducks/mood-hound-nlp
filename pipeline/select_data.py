# =============================================================================
# Organizando avaliações pelo grau de classificação (positiva ou negativa)
# =============================================================================
import pandas as pd
import numpy as np
import os
import sys
utils_path = os.getcwd() + '/utils'
sys.path.insert(0, utils_path)
import random_select

def select_data(df):
  positive = random_select.select(100, df, 'POSITIVO', 100)
  neutral = random_select.select(100, df, 'NEUTRO', 100)
  negative = random_select.select(100, df, 'NEGATIVO', 100)
  select = np.concatenate([positive, neutral, negative])

  df = df[df['text'].isin(select)].reset_index(drop=True)
  df = df.sample(frac=1).reset_index(drop=True)

  # print('-----------------------------------------------------------------------------')
  # print(df['stars'].value_counts(normalize=True))

  return df


def select_training_data(df):
  positive = random_select.select(100, df, 'POSITIVO', 15)
  neutral = random_select.select(100, df, 'NEUTRO', 45)
  negative = random_select.select(100, df, 'NEGATIVO', 20)

  select = np.concatenate([positive, neutral, negative])
  df = df[df['text'].isin(select)].reset_index(drop=True)
  df = df.sample(frac=1).reset_index(drop=True)

  return df