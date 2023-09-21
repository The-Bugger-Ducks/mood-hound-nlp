# =============================================================================
# Organizando avaliações pelo grau de classificação (positiva, neutra ou negativa)
# =============================================================================
import print_topic
import pandas as pd
import numpy as np

def organize_rating(df):
  print_topic.init('Organizando avaliações pelo grau de classificação...')

  positive = df[['review_text', 'overall_rating']][df['overall_rating'] >= 4] # 4 e 5 "estrelas"
  neutral = df[['review_text', 'overall_rating']][df['overall_rating'] == 3] # 3 "estrelas"
  negative = df[['review_text', 'overall_rating']][df['overall_rating'] <= 2] # 1 e 2 "estrelas"

  df = pd.concat([positive, neutral, negative])
  ratings_maping = {5: 'Positivo',4: 'Positivo', 3: 'Neutro', 2: 'Negativo', 1: 'Negativo'}
  df = df.replace(ratings_maping)
  
  np.random.seed(seed=100)
  positive = np.random.choice(df['review_text'][df['overall_rating'] == 'Positivo'], 10000, replace=False)
  neutral = np.random.choice(df['review_text'][df['overall_rating'] == 'Neutro'], 10000, replace=False)
  negative = np.random.choice(df['review_text'][df['overall_rating'] == 'Negativo'], 10000, replace=False)
  select = np.concatenate([positive, neutral, negative])

  df = df[df['review_text'].isin(select)].reset_index(drop=True)
  df = df.sample(frac=1).reset_index(drop=True)

  print_topic.finish_variation()
  print('-----------------------------------------------------------------------------')
  print(df['overall_rating'].value_counts(normalize=True))
  print('=============================================================================')

  return df