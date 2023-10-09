# =============================================================================
# Organizando avaliações pelo grau de classificação (positiva, neutra ou negativa)
# =============================================================================
import pandas as pd
import numpy as np

def select_data(df):
  positive = df[df['sentiment'] >= 4] # 4 e 5 "estrelas"
  neutral = df[df['sentiment'] == 3] # 3 "estrelas"
  negative = df[df['sentiment'] <= 2] # 1 e 2 "estrelas"

  df = pd.concat([positive, neutral, negative])
  ratings_maping = {5: 'POSITIVE',4: 'POSITIVE', 3: 'NEUTRAL', 2: 'NEGATIVE', 1: 'NEGATIVE'}
  df = df.replace(ratings_maping)

  np.random.seed(seed=100)
  positive = np.random.choice(df['text'][df['sentiment'] == 'POSITIVE'], 10000, replace=False)
  np.random.seed(seed=100)
  neutral = np.random.choice(df['text'][df['sentiment'] == 'NEUTRAL'], 10000, replace=False)
  np.random.seed(seed=100)
  negative = np.random.choice(df['text'][df['sentiment'] == 'NEGATIVE'], 10000, replace=False)
  select = np.concatenate([positive, neutral, negative])

  df = df[df['text'].isin(select)].reset_index(drop=True)
  df = df.sample(frac=1).reset_index(drop=True)

  print('-----------------------------------------------------------------------------')
  print(df['sentiment'].value_counts(normalize=True))

  return df