import numpy as np

def select(seedNumber, df, sentiment, quantity):
  condition = df['stars'] >= 4 # 4 e 5 "estrelas"
  if(sentiment == 'NEGATIVO'):
    condition = df['stars'] <= 3 # 1, 2 e 3 "estrelas"

  np.random.seed(seed=seedNumber)
  return np.random.choice(df['text'][condition], quantity, replace=False)