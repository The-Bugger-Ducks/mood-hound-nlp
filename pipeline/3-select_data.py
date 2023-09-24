# =============================================================================
# Organizando avaliações pelo grau de classificação (positiva, neutra ou negativa)
# =============================================================================
import pandas as pd
import numpy as np

def select_data(df):
  positive = df[df['overall_rating'] >= 4] # 4 e 5 "estrelas"
  neutral = df[df['overall_rating'] == 3] # 3 "estrelas"
  negative = df[df['overall_rating'] <= 2] # 1 e 2 "estrelas"

  df = pd.concat([positive, neutral, negative])
  ratings_maping = {5: 'Positivo',4: 'Positivo', 3: 'Neutro', 2: 'Negativo', 1: 'Negativo'}
  df = df.replace(ratings_maping)

  np.random.seed(seed=100)
  positive = np.random.choice(df['review_text'][df['overall_rating'] == 'Positivo'], 10000, replace=False)
  np.random.seed(seed=100)
  neutral = np.random.choice(df['review_text'][df['overall_rating'] == 'Neutro'], 10000, replace=False)
  np.random.seed(seed=100)
  negative = np.random.choice(df['review_text'][df['overall_rating'] == 'Negativo'], 10000, replace=False)
  select = np.concatenate([positive, neutral, negative])

  df = df[df['review_text'].isin(select)].reset_index(drop=True)
  df = df.sample(frac=1).reset_index(drop=True)

  print('-----------------------------------------------------------------------------')
  print(df['overall_rating'].value_counts(normalize=True))

  return df